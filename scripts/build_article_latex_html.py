#!/usr/bin/env python3
"""Build article assets through a LaTeX -> HTML pipeline.

Pipeline:
1. Read the Markdown first draft.
2. Generate a simple article-style LaTeX source.
3. Convert that LaTeX source into styled HTML.

The final PDF is produced from the HTML with LibreOffice headless.
"""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MD = ROOT / "paper" / "MAP_States_Governance_T3_First_Draft.md"
ARTICLE_TEX = ROOT / "paper" / "MAP_States_Governance_T3_Article.tex"
ARTICLE_HTML = ROOT / "paper" / "MAP_States_Governance_T3_Article.html"


LATEX_ESCAPES = {
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def tex_escape(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"\*(.+?)\*", r"\\emph{\1}", text)
    parts: list[str] = []
    command_spans: list[tuple[int, int]] = []
    for match in re.finditer(r"\\(?:textbf|emph)\{[^{}]*\}", text):
        command_spans.append(match.span())
    i = 0
    for start, end in command_spans:
        parts.append("".join(LATEX_ESCAPES.get(ch, ch) for ch in text[i:start]))
        parts.append(text[start:end])
        i = end
    parts.append("".join(LATEX_ESCAPES.get(ch, ch) for ch in text[i:]))
    return "".join(parts).replace("->", r"$\rightarrow$")


def tex_unescape(text: str) -> str:
    text = text.replace(r"$\rightarrow$", "->")
    text = re.sub(r"\\textbf\{([^{}]*)\}", r"<strong>\1</strong>", text)
    text = re.sub(r"\\emph\{([^{}]*)\}", r"<em>\1</em>", text)
    replacements = {
        r"\&": "&",
        r"\%": "%",
        r"\$": "$",
        r"\#": "#",
        r"\_": "_",
        r"\{": "{",
        r"\}": "}",
        r"\textbackslash{}": "\\",
        r"\textasciitilde{}": "~",
        r"\textasciicircum{}": "^",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def parse_md(md: str) -> tuple[str, list[tuple[str, object]]]:
    title = ""
    blocks: list[tuple[str, object]] = []
    para: list[str] = []
    table: list[str] = []

    def flush_para() -> None:
        if para:
            blocks.append(("p", " ".join(para).strip()))
            para.clear()

    def flush_table() -> None:
        if table:
            rows = []
            for line in table:
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                    continue
                rows.append(cells)
            if rows:
                blocks.append(("table", rows))
            table.clear()

    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("# "):
            flush_para()
            flush_table()
            title = line[2:].strip()
        elif line == "---":
            flush_para()
            flush_table()
        elif line.startswith("## "):
            flush_para()
            flush_table()
            blocks.append(("section", line[3:].strip()))
        elif line.startswith("### "):
            flush_para()
            flush_table()
            blocks.append(("subsection", line[4:].strip()))
        elif line.startswith("|") and line.endswith("|"):
            flush_para()
            table.append(line)
        elif not line.strip():
            flush_para()
            flush_table()
        else:
            para.append(line.strip())
    flush_para()
    flush_table()
    return title, blocks


def build_tex(title: str, blocks: list[tuple[str, object]]) -> str:
    out = [
        r"\documentclass[11pt]{article}",
        r"\usepackage[letterpaper,margin=0.85in]{geometry}",
        r"\usepackage{booktabs}",
        r"\usepackage{array}",
        r"\usepackage{hyperref}",
        r"\usepackage{times}",
        r"\usepackage{setspace}",
        r"\setstretch{1.08}",
        r"\title{" + tex_escape(title) + "}",
        r"\author{Dylan D. Mobley\\The Heart AI Foundation\\ORCID: 0009-0002-3560-3955}",
        r"\date{2026}",
        r"\begin{document}",
        r"\maketitle",
    ]
    in_abstract = False
    for kind, value in blocks:
        if kind == "section":
            if value == "Abstract":
                out.append(r"\begin{abstract}")
                in_abstract = True
            else:
                if in_abstract:
                    out.append(r"\end{abstract}")
                    in_abstract = False
                out.append(r"\section{" + tex_escape(str(value)) + "}")
        elif kind == "subsection":
            out.append(r"\subsection{" + tex_escape(str(value)) + "}")
        elif kind == "p":
            out.append(tex_escape(str(value)))
            out.append("")
        elif kind == "table":
            rows = value  # type: ignore[assignment]
            max_cols = max(len(row) for row in rows)
            colspec = ">{\\raggedright\\arraybackslash}p{0.42\\linewidth}" + " ".join(
                [">{\\raggedright\\arraybackslash}p{0.18\\linewidth}" for _ in range(max_cols - 1)]
            )
            out.append(r"\begin{center}")
            out.append(r"\begin{tabular}{" + colspec + "}")
            out.append(r"\toprule")
            for idx, row in enumerate(rows):
                padded = row + [""] * (max_cols - len(row))
                out.append(" & ".join(tex_escape(cell) for cell in padded) + r" \\")
                if idx == 0:
                    out.append(r"\midrule")
            out.append(r"\bottomrule")
            out.append(r"\end{tabular}")
            out.append(r"\end{center}")
    if in_abstract:
        out.append(r"\end{abstract}")
    out.append(r"\end{document}")
    return "\n".join(out) + "\n"


def inline_html(text: str) -> str:
    unescaped = tex_unescape(text)
    escaped = html.escape(unescaped)
    escaped = escaped.replace("&lt;strong&gt;", "<strong>").replace("&lt;/strong&gt;", "</strong>")
    escaped = escaped.replace("&lt;em&gt;", "<em>").replace("&lt;/em&gt;", "</em>")
    escaped = re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', escaped)
    return escaped


def latex_to_html(tex: str) -> tuple[str, str]:
    title = re.search(r"\\title\{(.+?)\}", tex)
    article_title = tex_unescape(title.group(1)) if title else "Article"
    body_tex = tex.split(r"\maketitle", 1)[1].rsplit(r"\end{document}", 1)[0]
    lines = body_tex.splitlines()
    html_blocks: list[str] = []
    para: list[str] = []
    in_abs = False
    in_tabular = False
    table_rows: list[list[str]] = []

    def flush_para() -> None:
        if para:
            tag = "div" if in_abs else "p"
            cls = ' class="abstract-text"' if in_abs else ""
            html_blocks.append(f"<{tag}{cls}>{inline_html(' '.join(para).strip())}</{tag}>")
            para.clear()

    def flush_table() -> None:
        nonlocal table_rows
        if not table_rows:
            return
        out = ["<table>", "<thead><tr>"]
        for cell in table_rows[0]:
            out.append(f"<th>{inline_html(cell)}</th>")
        out.append("</tr></thead><tbody>")
        for row in table_rows[1:]:
            out.append("<tr>")
            for cell in row:
                out.append(f"<td>{inline_html(cell)}</td>")
            out.append("</tr>")
        out.append("</tbody></table>")
        html_blocks.append("\n".join(out))
        table_rows = []

    for raw in lines:
        line = raw.strip()
        if not line:
            flush_para()
            continue
        if line == r"\begin{abstract}":
            flush_para()
            html_blocks.append("<h2>Abstract</h2>")
            in_abs = True
            continue
        if line == r"\end{abstract}":
            flush_para()
            in_abs = False
            continue
        sec = re.fullmatch(r"\\section\{(.+)\}", line)
        if sec:
            flush_para()
            html_blocks.append(f"<h2>{inline_html(sec.group(1))}</h2>")
            continue
        sub = re.fullmatch(r"\\subsection\{(.+)\}", line)
        if sub:
            flush_para()
            html_blocks.append(f"<h3>{inline_html(sub.group(1))}</h3>")
            continue
        if line.startswith(r"\begin{tabular}"):
            flush_para()
            in_tabular = True
            table_rows = []
            continue
        if line == r"\end{tabular}":
            in_tabular = False
            flush_table()
            continue
        if in_tabular:
            if line in {r"\toprule", r"\midrule", r"\bottomrule"}:
                continue
            if line.endswith(r"\\"):
                line = line[:-2].strip()
            table_rows.append([cell.strip() for cell in line.split("&")])
            continue
        if line.startswith("\\"):
            continue
        para.append(line)
    flush_para()
    return article_title, "\n".join(html_blocks)


def build_html(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
    @page {{ size: Letter; margin: 0.7in 0.8in 0.8in 0.8in; }}
    body {{
      max-width: 7.2in;
      margin: 0 auto;
      color: #181818;
      background: white;
      font-family: "Liberation Serif", "Times New Roman", serif;
      font-size: 11pt;
      line-height: 1.34;
    }}
    header {{
      text-align: center;
      border-bottom: 1.5px solid #111;
      margin-bottom: 1rem;
      padding-bottom: 0.75rem;
    }}
    h1 {{ font-size: 18pt; line-height: 1.12; margin: 0 0 0.55rem 0; }}
    .byline {{ font-size: 10.5pt; line-height: 1.35; }}
    h2 {{
      font-size: 13pt;
      border-bottom: 0.6px solid #c8c8c8;
      padding-bottom: 0.1rem;
      margin: 1.05rem 0 0.4rem 0;
      break-after: avoid;
    }}
    h3 {{ font-size: 11.7pt; font-style: italic; margin: 0.8rem 0 0.3rem 0; }}
    p, .abstract-text {{ margin: 0 0 0.55rem 0; text-align: justify; orphans: 3; widows: 3; }}
    .abstract-text {{ font-size: 10.4pt; }}
    table {{ border-collapse: collapse; width: 90%; margin: 0.65rem auto 0.9rem auto; font-size: 9.4pt; break-inside: avoid; }}
    th {{ border-bottom: 1px solid #111; padding: 0.2rem 0.35rem; text-align: left; }}
    td {{ border-bottom: 0.5px solid #ddd; padding: 0.2rem 0.35rem; vertical-align: top; }}
    a {{ color: #111; text-decoration: none; }}
    footer {{ border-top: 0.6px solid #bbb; margin-top: 1rem; padding-top: 0.3rem; color: #555; font-size: 8.7pt; text-align: center; }}
  </style>
</head>
<body>
  <header>
    <h1>{html.escape(title)}</h1>
    <div class="byline"><strong>Dylan D. Mobley</strong><br>The Heart AI Foundation<br>ORCID: 0009-0002-3560-3955</div>
  </header>
  <main>
    {body}
  </main>
  <footer>Generated from LaTeX source for the MAP-States Governance Evidence package</footer>
</body>
</html>
"""


def main() -> None:
    title, blocks = parse_md(SOURCE_MD.read_text(encoding="utf-8"))
    tex = build_tex(title, blocks)
    ARTICLE_TEX.write_text(tex, encoding="utf-8")
    html_title, html_body = latex_to_html(tex)
    ARTICLE_HTML.write_text(build_html(html_title, html_body), encoding="utf-8")
    print(ARTICLE_TEX)
    print(ARTICLE_HTML)


if __name__ == "__main__":
    main()
