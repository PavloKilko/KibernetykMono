"""Composable, collision-safe registries for independently maintained glyph groups."""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from types import MappingProxyType
from typing import Callable

from .model import GlyphDefinition

GlyphBuilder = Callable[[float], GlyphDefinition]


@dataclass(frozen=True)
class GlyphGroup:
    name: str
    builders: Mapping[str, GlyphBuilder]

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("Glyph group name cannot be empty")
        if not self.builders:
            raise ValueError(f"Glyph group {self.name!r} cannot be empty")

        copied_builders = dict(self.builders)
        for selector, builder in copied_builders.items():
            if not isinstance(selector, str) or not selector:
                raise ValueError(
                    f"Glyph group {self.name!r} contains an invalid selector: "
                    f"{selector!r}"
                )
            if not callable(builder):
                raise TypeError(
                    f"Builder for {selector!r} in {self.name!r} is not callable"
                )
        object.__setattr__(self, "builders", MappingProxyType(copied_builders))


class GlyphRegistry(Mapping[str, GlyphBuilder]):
    def __init__(self, groups: Iterable[GlyphGroup]) -> None:
        self._groups: dict[str, GlyphGroup] = {}
        self._builders: dict[str, GlyphBuilder] = {}
        self._selector_groups: dict[str, str] = {}

        for group in groups:
            if group.name in self._groups:
                raise ValueError(f"Duplicate glyph group: {group.name!r}")
            self._groups[group.name] = group

            for selector, builder in group.builders.items():
                previous_group = self._selector_groups.get(selector)
                if previous_group is not None:
                    raise ValueError(
                        f"Duplicate glyph selector {selector!r} in groups "
                        f"{previous_group!r} and {group.name!r}"
                    )
                self._builders[selector] = builder
                self._selector_groups[selector] = group.name

        self._readonly_builders = MappingProxyType(self._builders)
        self._readonly_groups = MappingProxyType(self._groups)

    def __getitem__(self, selector: str) -> GlyphBuilder:
        return self._builders[selector]

    def __iter__(self) -> Iterator[str]:
        return iter(self._builders)

    def __len__(self) -> int:
        return len(self._builders)

    @property
    def builders(self) -> Mapping[str, GlyphBuilder]:
        return self._readonly_builders

    @property
    def groups(self) -> Mapping[str, GlyphGroup]:
        return self._readonly_groups

    @property
    def group_names(self) -> tuple[str, ...]:
        return tuple(self._groups)

    def build(
        self,
        width: float,
        names: Sequence[str] | None = None,
        group_names: Sequence[str] | None = None,
    ) -> list[GlyphDefinition]:
        if names is not None and group_names is not None:
            raise ValueError("Select glyph names or glyph groups, not both")

        if names is not None:
            selected_names = tuple(names)
            if not selected_names:
                raise ValueError("Select at least one glyph")
            unknown = [name for name in selected_names if name not in self._builders]
            if unknown:
                formatted = ", ".join(repr(name) for name in unknown)
                raise ValueError(f"Unknown glyph builder(s): {formatted}")
            return [self._builders[name](width) for name in selected_names]

        if group_names is not None:
            selected_groups = tuple(group_names)
            if not selected_groups:
                raise ValueError("Select at least one glyph group")
            unknown = [name for name in selected_groups if name not in self._groups]
            if unknown:
                formatted = ", ".join(repr(name) for name in unknown)
                raise ValueError(f"Unknown glyph group(s): {formatted}")
            if len(set(selected_groups)) != len(selected_groups):
                raise ValueError("Glyph groups cannot be selected more than once")

            return [
                builder(width)
                for group_name in selected_groups
                for builder in self._groups[group_name].builders.values()
            ]

        return [builder(width) for builder in self._builders.values()]

