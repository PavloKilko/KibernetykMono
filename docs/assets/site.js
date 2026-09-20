/* Self-hosted fonts and static specimens. */
(() => {
  "use strict";
  const data = window.KIBERNETYK_SITE;
  const $ = (selector) => document.querySelector(selector);
  const $$ = (selector) => [...document.querySelectorAll(selector)];
  const root = document.documentElement;
  const weight = $("#weight");
  const editor = $("#code-example");
  const highlightedCode = $("#code-highlight code");
  const codeSamples = {
    rust: [
      "fn process(samples: &[f64]) -> Vec<f64> {",
      "    samples.iter()",
      "        .copied()",
      "        .filter(|&x| x >= 0.0 && x <= 100.0)",
      "        .map(|x| (x * 2.54).round())",
      "        .collect()",
      "}",
      "",
      "fn main() {",
      "    let readings = [0.0, 12.5, 42.0, 89.1];",
      '    println!("Signal: {:?}", process(&readings));',
      "}",
    ],
    cpp: [
      "#include <cmath>",
      "#include <iostream>",
      "#include <vector>",
      "",
      "std::vector<double> process(const std::vector<double>& samples) {",
      "    std::vector<double> result;",
      "    for (const auto x : samples) {",
      "        if (x >= 0.0 && x <= 100.0) {",
      "            result.push_back(std::round(x * 2.54));",
      "        }",
      "    }",
      "    return result;",
      "}",
      "",
      "int main() {",
      "    for (const auto x : process({0.0, 12.5, 42.0, 89.1})) {",
      "        std::cout << x << '\\n';",
      "    }",
      "}",
    ],
    python: [
      "def process(samples: list[float]) -> list[float]:",
      "    return [",
      "        round(x * 2.54)",
      "        for x in samples",
      "        if 0.0 <= x <= 100.0",
      "    ]",
      "",
      "",
      'if __name__ == "__main__":',
      "    readings = [0.0, 12.5, 42.0, 89.1]",
      '    print("Signal:", process(readings))',
    ],
    typescript: [
      "type Signal = { value: number; unit: string };",
      "",
      "function process(samples: readonly number[]): Signal[] {",
      "  return samples",
      "    .filter((x) => x >= 0.0 && x <= 100.0)",
      '    .map((x) => ({ value: Math.round(x * 2.54), unit: "cm" }));',
      "}",
      "",
      "const readings = [0.0, 12.5, 42.0, 89.1];",
      "console.log(process(readings));",
    ],
    go: [
      "package main",
      "",
      'import ("fmt"; "math")',
      "",
      "func process(samples []float64) []float64 {",
      "    result := make([]float64, 0, len(samples))",
      "    for _, x := range samples {",
      "        if x >= 0.0 && x <= 100.0 {",
      "            result = append(result, math.Round(x * 2.54))",
      "        }",
      "    }",
      "    return result",
      "}",
      "",
      "func main() {",
      "    fmt.Println(process([]float64{0.0, 12.5, 42.0, 89.1}))",
      "}",
    ],
    kotlin: [
      "import kotlin.math.roundToInt",
      "",
      "fun process(samples: List<Double>): List<Int> =",
      "    samples",
      "        .filter { it >= 0.0 && it <= 100.0 }",
      "        .map { (it * 2.54).roundToInt() }",
      "",
      "fun main() {",
      "    val readings = listOf(0.0, 12.5, 42.0, 89.1)",
      "    println(process(readings))",
      "}",
    ],
    swift: [
      "func process(_ samples: [Double]) -> [Double] {",
      "    samples",
      "        .filter { $0 >= 0.0 && $0 <= 100.0 }",
      "        .map { ($0 * 2.54).rounded() }",
      "}",
      "",
      "let readings = [0.0, 12.5, 42.0, 89.1]",
      "print(process(readings))",
    ],
    haskell: [
      "process :: [Double] -> [Integer]",
      "process samples =",
      "    [ round (x * 2.54)",
      "    | x <- samples",
      "    , x >= 0.0 && x <= 100.0",
      "    ]",
      "",
      "main :: IO ()",
      "main = print (process [0.0, 12.5, 42.0, 89.1])",
    ],
  };
  const keywords = new Set(("fn let mut const if else return for in use pub struct impl match async await " +
    "type function readonly def import from class with as lambda and or not package func range " +
    "auto int double void include fun val do where main make append").split(" "));
  const types = new Set(("Vec String Signal number string float float64 bool Double Int Integer List IO " +
    "Math Result Option Some None std vector").split(" "));
  let language = "rust";
  let category = "latin";
  let selected;
  let fontRequest = 0;

  function escapeHTML(value) {
    return value
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function highlightLine(line) {
    if (language === "cpp" && /^\s*#/.test(line)) {
      const leading = line.match(/^\s*/)[0];
      const directive = line.slice(leading.length).match(/^#[A-Za-z_]+/)[0];
      return escapeHTML(leading) + '<span class="syntax-keyword">' +
        escapeHTML(directive) + "</span>" + escapeHTML(line.slice(leading.length + directive.length));
    }
    const tokens = /"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\/\/.*|--.*|#.*|\b\d+(?:\.\d+)?\b|\b[A-Za-z_][A-Za-z_0-9]*\b/g;
    let result = "";
    let cursor = 0;
    for (const match of line.matchAll(tokens)) {
      result += escapeHTML(line.slice(cursor, match.index));
      const token = match[0];
      let syntax = "";
      if (token.startsWith("//") || (language === "haskell" && token.startsWith("--")) ||
          (language === "python" && token.startsWith("#"))) {
        syntax = "comment";
      } else if (/^["']/.test(token)) {
        syntax = "string";
      } else if (/^\d/.test(token)) {
        syntax = "number";
      } else if (keywords.has(token)) {
        syntax = "keyword";
      } else if (types.has(token) || /^[A-Z][A-Za-z0-9_]*$/.test(token)) {
        syntax = "type";
      }
      result += syntax
        ? '<span class="syntax-' + syntax + '">' + escapeHTML(token) + "</span>"
        : escapeHTML(token);
      cursor = match.index + token.length;
    }
    return result + escapeHTML(line.slice(cursor));
  }

  function updateCodeDisplay() {
    const lines = editor.value.split("\n");
    $("#code-lines").textContent = lines.map(
      (_, index) => String(index + 1).padStart(2, "0")
    ).join("\n");
    highlightedCode.innerHTML = lines.map(highlightLine).join("\n") +
      (editor.value.endsWith("\n") ? " " : "");
    syncCodeScroll();
  }

  function syncCodeScroll() {
    $("#code-lines").scrollTop = editor.scrollTop;
    $("#code-highlight").scrollTop = editor.scrollTop;
    $("#code-highlight").scrollLeft = editor.scrollLeft;
  }

  function renderCode() {
    editor.value = codeSamples[language].join("\n");
    updateCodeDisplay();
    $$("[data-language]").forEach((button) => {
      button.setAttribute("aria-pressed", String(button.dataset.language === language));
      if (button.dataset.language === language) {
        editor.setAttribute("aria-label", "Editable " + button.textContent + " code example");
      }
    });
  }

  async function copyText(text, button) {
    button.dataset.label ||= button.textContent;
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(text);
      } else {
        const temporary = document.createElement("textarea");
        temporary.value = text;
        temporary.className = "sr-only";
        document.body.append(temporary);
        temporary.select();
        const copied = document.execCommand("copy");
        temporary.remove();
        button.focus();
        if (!copied) throw new Error("Copy unavailable");
      }
      button.textContent = "Copied";
      $("#announcement").textContent = "Copied to clipboard.";
    } catch {
      button.textContent = "Copy unavailable";
      $("#announcement").textContent = "Clipboard unavailable. Select the text to copy it.";
    }
    window.setTimeout(() => { button.textContent = button.dataset.label; }, 1600);
  }

  function displayedCharacter(glyph) {
    return glyph.category === "marks" ? "a" + glyph.character : glyph.character;
  }

  function fitGlyph() {
    const text = $("#selected-glyph");
    text.removeAttribute("transform");
    text.setAttribute("x", "0");
    text.setAttribute("y", "0");
    const box = text.getBBox();
    if (!box.width || !box.height) return;
    const scale = Math.min(300 / box.width, 340 / box.height, 2.8);
    const x = 210 - (box.x + box.width / 2) * scale;
    const y = 240 - (box.y + box.height / 2) * scale;
    text.setAttribute("transform", "translate(" + x + " " + y + ") scale(" + scale + ")");
  }

  function selectGlyph(glyph) {
    selected = glyph;
    $("#selected-glyph").textContent = displayedCharacter(glyph);
    $("#glyph-preview").setAttribute("aria-label", glyph.name + ", " + glyph.unicode);
    $("#glyph-unicode").textContent = glyph.unicode;
    $$(".glyph-cell").forEach((button) => button.setAttribute(
      "aria-pressed",
      String(Number(button.dataset.codepoint) === glyph.codepoint)
    ));
    requestAnimationFrame(fitGlyph);
  }

  function renderGlyphs() {
    const query = $("#glyph-search").value.trim().toLowerCase();
    const glyphs = data.characters.filter((glyph) =>
      (category === "all" || glyph.category === category) &&
      (!query || glyph.character.toLowerCase() === query ||
        [glyph.unicode, glyph.name, glyph.glyphName].some((name) => name.toLowerCase().includes(query)))
    );
    const grid = $("#glyph-grid");
    grid.replaceChildren();
    for (const glyph of glyphs) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "glyph-cell font-sample";
      button.dataset.codepoint = glyph.codepoint;
      button.title = glyph.unicode + " · " + glyph.name;
      button.setAttribute("aria-label", button.title);
      button.setAttribute("aria-pressed", String(glyph.codepoint === selected?.codepoint));
      if (/^\s$/.test(glyph.character)) {
        const label = document.createElement("small");
        label.textContent = glyph.codepoint === 32 ? "SP" : "NBSP";
        button.append(label);
      } else {
        button.textContent = displayedCharacter(glyph);
      }
      button.addEventListener("click", () => selectGlyph(glyph));
      grid.append(button);
    }
    if (!glyphs.length) {
      const empty = document.createElement("p");
      empty.className = "no-results";
      empty.textContent = "No matching characters.";
      grid.append(empty);
    }
    grid.scrollTop = 0;
    $("#glyph-count").textContent = glyphs.length + " characters.";
    $$("[data-category]").forEach((button) =>
      button.setAttribute("aria-pressed", String(button.dataset.category === category))
    );
  }

  async function applyFont() {
    const request = ++fontRequest;
    const font = data.fonts.find((item) => item.weight === Number(weight.value));
    if (!font) return;
    root.style.setProperty("--font", JSON.stringify(font.family));
    root.style.setProperty("--weight", font.weight);
    root.dataset.fontReady = "false";
    try {
      const faces = await document.fonts.load(font.weight + ' 100px "' + font.family + '"', "Aa");
      if (request !== fontRequest) return;
      if (!faces.length) throw new Error("No font loaded");
      $("#font-error").hidden = true;
      root.dataset.fontReady = "true";
      requestAnimationFrame(fitGlyph);
    } catch {
      if (request !== fontRequest) return;
      $("#font-error").textContent = "The font could not load. Refresh the page or rebuild the website assets.";
      $("#font-error").hidden = false;
    }
  }

  $$("[data-language]").forEach((button) => button.addEventListener("click", () => {
    language = button.dataset.language;
    renderCode();
  }));
  editor.addEventListener("input", updateCodeDisplay);
  editor.addEventListener("scroll", syncCodeScroll);
  editor.addEventListener("keydown", (event) => {
    if (event.key !== "Tab") return;
    event.preventDefault();
    editor.setRangeText("    ", editor.selectionStart, editor.selectionEnd, "end");
    updateCodeDisplay();
  });
  $("#copy-code").addEventListener("click", (event) => copyText(editor.value, event.currentTarget));
  renderCode();

  if (!data) {
    $("#font-error").textContent = "The character index is missing. Run python scripts/build_site.py.";
    $("#font-error").hidden = false;
    return;
  }

  $("#weight-count").textContent = data.fonts.length;
  $("#glyph-total").textContent = data.glyphCount;
  $("#script-count").textContent = data.scripts.length;
  $("#script-count").title = data.scripts.join(" and ");
  $("#download-family").href = data.download;
  $("#download-description").textContent = data.downloadDescription;
  weight.replaceChildren(...data.fonts.map((font) => {
    const option = document.createElement("option");
    option.value = font.weight;
    option.textContent = font.style;
    option.selected = font.weight === 400;
    return option;
  }));
  weight.addEventListener("change", applyFont);
  $("#glyph-search").addEventListener("input", renderGlyphs);
  $$("[data-category]").forEach((button) => button.addEventListener("click", () => {
    category = button.dataset.category;
    renderGlyphs();
  }));
  $("#copy-glyph").addEventListener("click", (event) => {
    if (selected) copyText(selected.character, event.currentTarget);
  });
  selectGlyph(data.characters.find((glyph) => glyph.character === "Ж") || data.characters[0]);
  renderGlyphs();
  applyFont();
})();

