"""Central font metrics and build configuration."""

FAMILY_NAME = "Kibernetyk Mono"
ROUNDED_FAMILY_NAME = f"{FAMILY_NAME} Rounded"
RELEASE_VERSION = "0.9.1"
# OpenType name ID 5 and head.fontRevision use MAJOR.MINOR notation.
# Version 0.901 corresponds to the project release tag v0.9.1.
VERSION = "0.901"

# Editable OpenType name-table metadata. Fill in the blank values before a
# public release; blank entries are omitted from generated fonts.
FONT_METADATA = {
    "designer": "Pavlo Kilko",       # Your name or the name you publish under.
    "designerURL": "https://www.linkedin.com/in/pavlo-kilko",    # Your portfolio or project URL.
    "manufacturer": "Pavlo Kilko",   # Your foundry name; may be the same as designer.
    "vendorURL": "https://github.com/PavloKilko/KibernetykMono", # github.com      # Foundry or project URL.
    "copyright": "Copyright 2026 The Kibernetyk Mono Project Authors (https://github.com/PavloKilko/KibernetykMono)",      # Example: "Copyright 2026 Your Name".
    "description": "",    # A short description of the typeface.
    "licenseDescription": (
        "This Font Software is licensed under the SIL Open Font License, "
        "Version 1.1. This license is available with a FAQ at: "
        "https://openfontlicense.org"
    ),
    "licenseInfoURL": "https://openfontlicense.org",      # Example: "https://openfontlicense.org".
}

UNITS_PER_EM = 1000
X_HEIGHT = 600
CAP_HEIGHT = 800
# Vertical cell metrics include room for accents; they do not scale outlines.
ASCENDER = 848
DESCENDER = -200
# The monospaced cell width. Rendered outlines are centered inside this cell;
# increasing it adds equal left/right space without changing glyph geometry.
ADVANCE_WIDTH = 720
GLYPH_CENTER_X = 300
VERTICAL_BOX_TOP = 1000
VERTICAL_BOX_BOTTOM = -200
LINE_GAP = 1200 - (ASCENDER - DESCENDER)

# Rounded-outline controls. The radius follows the selected stroke width, and
# the curve is sampled because the reference renderer outputs polygons.
CORNER_RADIUS_RATIO = 0.20
CORNER_CURVE_STEPS = 6

# Comma-shaped diacritics are intentionally smaller than the punctuation
# comma. Keep one scale for combining marks and hardcoded composite glyphs.
COMMA_ACCENT_SCALE = 0.75
# Use tcaron's original visible comma top for dcaron/lcaron/tcaron/Lcaron.
COMMA_CARON_TOP = 900

WEIGHT_WIDTHS = {
    "thin": 64,         # -36
    "extralight": 76,   # -24
    "light": 88,        # -12
    "regular": 100,     #   0
    "medium": 112,      # +12
    "semibold": 124,    # +24
    "bold": 136,        # +36
    # "extrabold": 148,   # +48
}

WEIGHT_CLASSES = {
    "thin": 100,
    "extralight": 200,
    "light": 300,
    "regular": 400,
    "medium": 500,
    "semibold": 600,
    "bold": 700,
    # "extrabold": 800,
}

WEIGHT_STYLE_NAMES = {
    "thin": "Thin",
    "extralight": "ExtraLight",
    "light": "Light",
    "regular": "Regular",
    "medium": "Medium",
    "semibold": "SemiBold",
    "bold": "Bold",
    # "extrabold": "ExtraBold",
}

FONT_FILE_STEM = FAMILY_NAME.replace(" ", "")
