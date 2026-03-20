#!/usr/bin/env python3
"""Build HTML documentation from Markdown source files for the Structural Necessity framework."""

import markdown
import re
import os

# Document metadata: (filename_base, title, subtitle, level_label, color)
DOCUMENTS = [
    ("T0_SUBSTRATE", "Paper 0: The Phase-Neutral Substrate", "From Co-Primitives to Engines, Potentials, and Phase-Dist", "Level 0-1", "#2d5016"),
    ("T1_DIST", "Paper 1: The Kernel Theorem", "Morphism Forcing and Quotient Idempotence", "Level 2", "#2d5016"),
    ("T2_BRIDGE", "Paper 2: The Bridge Chain", "Zero-Branching from {0,1} to M₂(ℝ)", "Level 3", "#1a4d1a"),
    ("T3_P1_PRODUCTION", "Paper 3-P1: Production", "Fibonacci, Möbius RG, and Baryon Physics", "Level 4 · P1", "#8b4513"),
    ("T3_P2_MEDIATION", "Paper 3-P2: Mediation", "Exponential Flow, Tower Saturation, Thermodynamics", "Level 4 · P2", "#8b4513"),
    ("T3_P3_OBSERVATION", "Paper 3-P3: Observation", "Rotation Closure, Spin-½, Holomorphic Properties", "Level 4 · P3", "#8b4513"),
    ("T3_META", "Paper 3-META: Cross-Projection Theorems", "Independence, Completeness, Folding, Central Collapse", "Level 4 · Cross", "#8b4513"),
    ("T4_LATTICE", "Paper 4: The Lattice", "Λ′ ≅ ℤ⁵, 27 Relations, Two-World Separation", "Level 4", "#4a3728"),
    ("T5_OBSERVER", "Paper 5: The Observer", "Dist→Hilb Functor, Bekenstein, Consciousness Hierarchy", "Level 5", "#2c3e6b"),
    ("T6A_SPACETIME", "Paper 6A: Spacetime Kinematics", "Minkowski, Lorentz, Spin-½, Poincaré, Born Rule", "Level 6 · P3", "#6b2c4e"),
    ("T6B_FORCES", "Paper 6B: Forces and Dynamics", "Standard Model Gauge Group, Gravity, Koide, Predictions", "Level 6 · P1+Cross", "#6b2c4e"),
    ("T_COMP", "Computational Theory", "Type I/II/III Hardness, OWF, Cost-Landauer-Bekenstein", "Cross-Cutting", "#555555"),
    ("T_SIL", "Self-Interpretation Layer", "FORCED/ENCODED/RESONANT/MYTHIC Status Grammar", "Cross-Cutting", "#555555"),
    ("T_SEM", "Semantic Layer", "Contranyms, Verb Algebra, Semantic Tower", "Cross-Cutting", "#555555"),
    ("T_BLUEPRINT", "Architectural Blueprint", "9×3 Grid B(n,p), Role Grammar, R(R)=R Tower", "Architecture", "#3a3a6b"),
    ("T_GOV", "Governance Calculus", "Generation Taxonomy, Ontological Standing, Transport", "Governance", "#3a3a6b"),
    ("T_ASI", "Architecture Specification v2", "Cognitive Invariant Ledger, 9-Layer Stack, ρ-Regulation", "Closure", "#6b3a3a"),
    ("T_TOE", "Closure Certificate", "Primitive Charter, Six Master Theorems, Open Problems", "Closure", "#6b3a3a"),
    ("DICTIONARY", "Canonical Dictionary", "30 Structurally-Loaded Terms with Projection and SIL Status", "Reference", "#6b3a3a"),
    ("T_INDEX", "Series Navigation Index", "Dependency Graph, Reading Orders, Problem Registry", "Navigation", "#333333"),
    ("CLAIM_CENSUS", "Claim Census", "Framework Rebuild Execution Protocol — ~122 Claims Registry", "Registry", "#333333"),
]

# Navigation groups for sidebar
NAV_GROUPS = [
    ("Foundation (0-2)", ["T0_SUBSTRATE", "T1_DIST", "T2_BRIDGE"]),
    ("Projections (3-4)", ["T3_P1_PRODUCTION", "T3_P2_MEDIATION", "T3_P3_OBSERVATION", "T3_META", "T4_LATTICE"]),
    ("Observer &amp; Physics (5-6)", ["T5_OBSERVER", "T6A_SPACETIME", "T6B_FORCES"]),
    ("Cross-Cutting", ["T_COMP", "T_SIL", "T_SEM"]),
    ("Architecture", ["T_BLUEPRINT", "T_GOV"]),
    ("Closure &amp; Reference", ["T_ASI", "T_TOE", "DICTIONARY"]),
    ("Navigation", ["T_INDEX", "CLAIM_CENSUS"]),
]

DOC_MAP = {d[0]: d for d in DOCUMENTS}

CSS = r"""
:root {
    --bg: #fafaf8;
    --fg: #1a1a1a;
    --accent: #2d5016;
    --border: #d4d0c8;
    --sidebar-bg: #f0ede6;
    --sidebar-width: 280px;
    --header-height: 56px;
    --code-bg: #f5f2eb;
    --table-stripe: #f8f6f0;
    --link: #2d5016;
    --link-hover: #4a7a28;
    --bold-accent: #1a3a0a;
}

@media (prefers-color-scheme: dark) {
    :root {
        --bg: #1a1a1e;
        --fg: #e0ddd6;
        --accent: #7ab648;
        --border: #3a3a3e;
        --sidebar-bg: #222226;
        --code-bg: #25252a;
        --table-stripe: #222226;
        --link: #7ab648;
        --link-hover: #9cd06a;
        --bold-accent: #a0d870;
    }
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
    font-family: 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif;
    background: var(--bg);
    color: var(--fg);
    line-height: 1.7;
    font-size: 17px;
}

/* Header */
.site-header {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: var(--header-height);
    background: #1a1a1a;
    color: #e0ddd6;
    display: flex;
    align-items: center;
    padding: 0 24px;
    z-index: 100;
    border-bottom: 2px solid var(--accent);
}
.site-header h1 {
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 0.5px;
}
.site-header h1 a {
    color: #e0ddd6;
    text-decoration: none;
}
.site-header h1 a:hover { color: var(--accent); }
.site-header .subtitle {
    font-size: 13px;
    color: #888;
    margin-left: 16px;
    font-style: italic;
}
.hamburger {
    display: none;
    background: none;
    border: none;
    color: #e0ddd6;
    font-size: 24px;
    cursor: pointer;
    margin-right: 16px;
    padding: 4px 8px;
}

/* Sidebar */
.sidebar {
    position: fixed;
    top: var(--header-height);
    left: 0;
    bottom: 0;
    width: var(--sidebar-width);
    background: var(--sidebar-bg);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    padding: 16px 0;
    z-index: 90;
    transition: transform 0.3s ease;
}
.sidebar .nav-group { margin-bottom: 12px; }
.sidebar .nav-group-title {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #888;
    padding: 8px 20px 4px;
}
.sidebar a {
    display: block;
    padding: 4px 20px 4px 28px;
    font-size: 13.5px;
    color: var(--fg);
    text-decoration: none;
    line-height: 1.5;
    border-left: 3px solid transparent;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
.sidebar a:hover {
    background: rgba(0,0,0,0.05);
    border-left-color: var(--accent);
}
.sidebar a.active {
    background: rgba(45,80,22,0.1);
    border-left-color: var(--accent);
    font-weight: 600;
    color: var(--accent);
}

/* Main content */
.main {
    margin-left: var(--sidebar-width);
    margin-top: var(--header-height);
    max-width: 900px;
    padding: 40px 48px 80px;
}

/* Document header banner */
.doc-header {
    margin-bottom: 40px;
    padding-bottom: 24px;
    border-bottom: 2px solid var(--border);
}
.doc-header .level-badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 3px 10px;
    border-radius: 3px;
    margin-bottom: 12px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
.doc-header h1 {
    font-size: 32px;
    line-height: 1.2;
    margin-bottom: 8px;
    color: var(--fg);
}
.doc-header .doc-subtitle {
    font-size: 18px;
    color: #666;
    font-style: italic;
}

/* TOC */
.toc {
    background: var(--sidebar-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 16px 24px;
    margin-bottom: 32px;
}
.toc summary {
    font-weight: 700;
    font-size: 14px;
    cursor: pointer;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: #666;
}
.toc ul { list-style: none; margin: 12px 0 0 0; }
.toc li { padding: 2px 0; }
.toc a {
    color: var(--link);
    text-decoration: none;
    font-size: 14px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
.toc a:hover { text-decoration: underline; }
.toc .toc-h2 { padding-left: 0; }
.toc .toc-h3 { padding-left: 20px; font-size: 13px; }

/* Typography */
.content h1 {
    font-size: 28px;
    margin: 48px 0 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
    color: var(--fg);
}
.content h1:first-child { margin-top: 0; }
.content h2 {
    font-size: 22px;
    margin: 36px 0 12px;
    color: var(--fg);
}
.content h3 {
    font-size: 18px;
    margin: 28px 0 10px;
    color: var(--fg);
}
.content h4 {
    font-size: 16px;
    margin: 24px 0 8px;
    color: #444;
}
.content p { margin: 0 0 16px; }
.content strong { color: var(--bold-accent); }
.content a { color: var(--link); }
.content a:hover { color: var(--link-hover); }

.content ul, .content ol {
    margin: 0 0 16px 24px;
}
.content li { margin-bottom: 4px; }

.content hr {
    border: none;
    border-top: 1px solid var(--border);
    margin: 32px 0;
}

/* Tables */
.content table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0 24px;
    font-size: 15px;
}
.content th {
    background: var(--sidebar-bg);
    font-weight: 700;
    text-align: left;
    padding: 10px 12px;
    border: 1px solid var(--border);
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
.content td {
    padding: 8px 12px;
    border: 1px solid var(--border);
    vertical-align: top;
}
.content tr:nth-child(even) { background: var(--table-stripe); }

/* Code */
.content code {
    font-family: 'SF Mono', 'Fira Code', 'Consolas', monospace;
    font-size: 14px;
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 3px;
    border: 1px solid var(--border);
}
.content pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 4px;
    padding: 16px 20px;
    overflow-x: auto;
    margin: 16px 0 24px;
    line-height: 1.5;
}
.content pre code {
    background: none;
    border: none;
    padding: 0;
    font-size: 13.5px;
}

/* Blockquote */
.content blockquote {
    border-left: 4px solid var(--accent);
    padding: 12px 20px;
    margin: 16px 0 24px;
    background: var(--sidebar-bg);
    border-radius: 0 4px 4px 0;
}
.content blockquote p { margin-bottom: 8px; }
.content blockquote p:last-child { margin-bottom: 0; }

/* Footer nav */
.page-nav {
    display: flex;
    justify-content: space-between;
    margin-top: 48px;
    padding-top: 24px;
    border-top: 1px solid var(--border);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
.page-nav a {
    color: var(--link);
    text-decoration: none;
    font-size: 14px;
    padding: 8px 16px;
    border: 1px solid var(--border);
    border-radius: 4px;
    transition: all 0.2s;
}
.page-nav a:hover {
    background: var(--sidebar-bg);
    border-color: var(--accent);
}
.page-nav .prev::before { content: '← '; }
.page-nav .next::after { content: ' →'; }

/* Responsive */
@media (max-width: 900px) {
    .sidebar { transform: translateX(-100%); }
    .sidebar.open { transform: translateX(0); }
    .main { margin-left: 0; padding: 24px 20px 60px; }
    .hamburger { display: block; }
    .doc-header h1 { font-size: 24px; }
}

/* Print */
@media print {
    .sidebar, .site-header, .hamburger, .page-nav { display: none; }
    .main { margin: 0; max-width: 100%; padding: 20px; }
    body { font-size: 12pt; }
}
"""


def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text.lower())
    return re.sub(r'[\s]+', '-', text).strip('-')


def extract_toc(html_content):
    """Extract headings from HTML to build a TOC."""
    toc_items = []
    pattern = re.compile(r'<(h[23])\s+id="([^"]+)"[^>]*>(.*?)</\1>', re.DOTALL)
    for match in pattern.finditer(html_content):
        level = match.group(1)
        id_attr = match.group(2)
        text = re.sub(r'<[^>]+>', '', match.group(3)).strip()
        toc_items.append((level, id_attr, text))
    return toc_items


def add_heading_ids(html_content):
    """Add id attributes to h1-h4 tags for anchor linking."""
    seen = {}
    def replacer(match):
        tag = match.group(1)
        attrs = match.group(2) or ''
        text = match.group(3)
        plain = re.sub(r'<[^>]+>', '', text).strip()
        slug = slugify(plain)
        if not slug:
            slug = 'section'
        if slug in seen:
            seen[slug] += 1
            slug = f"{slug}-{seen[slug]}"
        else:
            seen[slug] = 0
        return f'<{tag} id="{slug}"{attrs}>{text}</{tag}>'
    return re.compile(r'<(h[1234])(\s[^>]*)?>(.+?)</\1>', re.DOTALL).sub(replacer, html_content)


def build_sidebar_html(current_file):
    """Generate sidebar navigation HTML."""
    parts = []
    for group_name, files in NAV_GROUPS:
        parts.append(f'<div class="nav-group">')
        parts.append(f'<div class="nav-group-title">{group_name}</div>')
        for fname in files:
            doc = DOC_MAP[fname]
            active = ' class="active"' if fname == current_file else ''
            short_title = doc[1]
            # Shorten for sidebar
            short_title = short_title.replace("Paper 0: The Phase-Neutral Substrate", "0 — Substrate")
            short_title = short_title.replace("Paper 1: The Kernel Theorem", "1 — Kernel Theorem")
            short_title = short_title.replace("Paper 2: The Bridge Chain", "2 — Bridge Chain")
            short_title = short_title.replace("Paper 3-P1: Production", "3-P1 — Production")
            short_title = short_title.replace("Paper 3-P2: Mediation", "3-P2 — Mediation")
            short_title = short_title.replace("Paper 3-P3: Observation", "3-P3 — Observation")
            short_title = short_title.replace("Paper 3-META: Cross-Projection Theorems", "3-META — Cross-Projection")
            short_title = short_title.replace("Paper 4: The Lattice", "4 — Lattice")
            short_title = short_title.replace("Paper 5: The Observer", "5 — Observer")
            short_title = short_title.replace("Paper 6A: Spacetime Kinematics", "6A — Spacetime")
            short_title = short_title.replace("Paper 6B: Forces and Dynamics", "6B — Forces")
            short_title = short_title.replace("Computational Theory", "Comp — Computation")
            short_title = short_title.replace("Self-Interpretation Layer", "SIL — Self-Interpretation")
            short_title = short_title.replace("Semantic Layer", "SEM — Semantics")
            short_title = short_title.replace("Architectural Blueprint", "Blueprint")
            short_title = short_title.replace("Governance Calculus", "Governance")
            short_title = short_title.replace("Architecture Specification v2", "ASI — Architecture Spec")
            short_title = short_title.replace("Closure Certificate", "TOE — Closure")
            short_title = short_title.replace("Canonical Dictionary", "Dictionary")
            short_title = short_title.replace("Series Navigation Index", "Index — Navigation")
            short_title = short_title.replace("Claim Census", "Claim Census")
            parts.append(f'<a href="{fname}.html"{active}>{short_title}</a>')
        parts.append('</div>')
    return '\n'.join(parts)


def build_page_nav(current_file):
    """Build prev/next navigation."""
    all_files = [d[0] for d in DOCUMENTS]
    idx = all_files.index(current_file)
    parts = ['<div class="page-nav">']
    if idx > 0:
        prev_doc = DOC_MAP[all_files[idx - 1]]
        parts.append(f'<a class="prev" href="{all_files[idx-1]}.html">{prev_doc[1]}</a>')
    else:
        parts.append('<span></span>')
    if idx < len(all_files) - 1:
        next_doc = DOC_MAP[all_files[idx + 1]]
        parts.append(f'<a class="next" href="{all_files[idx+1]}.html">{next_doc[1]}</a>')
    else:
        parts.append('<span></span>')
    parts.append('</div>')
    return '\n'.join(parts)


def build_toc_html(toc_items):
    """Build table of contents HTML."""
    if not toc_items:
        return ''
    parts = ['<details class="toc" open>', '<summary>Table of Contents</summary>', '<ul>']
    for level, id_attr, text in toc_items:
        css_class = f'toc-{level}'
        parts.append(f'<li class="{css_class}"><a href="#{id_attr}">{text}</a></li>')
    parts.append('</ul></details>')
    return '\n'.join(parts)


def convert_md_to_html(md_path, filename_base):
    """Convert a single markdown file to styled HTML."""
    doc = DOC_MAP[filename_base]
    title, subtitle, level_label, color = doc[1], doc[2], doc[3], doc[4]

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert markdown to HTML
    extensions = ['tables', 'fenced_code', 'codehilite', 'toc', 'smarty', 'sane_lists']
    md = markdown.Markdown(extensions=extensions, extension_configs={
        'codehilite': {'guess_lang': False, 'css_class': 'highlight'},
    })
    body_html = md.convert(md_text)

    # Add heading IDs
    body_html = add_heading_ids(body_html)

    # Extract TOC
    toc_items = extract_toc(body_html)
    toc_html = build_toc_html(toc_items)

    # Build navigation
    sidebar_html = build_sidebar_html(filename_base)
    page_nav_html = build_page_nav(filename_base)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Structural Necessity</title>
<style>
{CSS}
</style>
</head>
<body>

<header class="site-header">
    <button class="hamburger" onclick="document.querySelector('.sidebar').classList.toggle('open')" aria-label="Toggle navigation">&#9776;</button>
    <h1><a href="T_INDEX.html">Structural Necessity</a></h1>
    <span class="subtitle">Canonical Paper Series — March 2026</span>
</header>

<nav class="sidebar">
{sidebar_html}
</nav>

<main class="main">
    <div class="doc-header">
        <span class="level-badge" style="background:{color}; color:#fff;">{level_label}</span>
        <h1>{title}</h1>
        <div class="doc-subtitle">{subtitle}</div>
    </div>

    {toc_html}

    <div class="content">
{body_html}
    </div>

    {page_nav_html}
</main>

<script>
// Close sidebar on mobile when clicking a link
document.querySelectorAll('.sidebar a').forEach(a => {{
    a.addEventListener('click', () => {{
        if (window.innerWidth <= 900) {{
            document.querySelector('.sidebar').classList.remove('open');
        }}
    }});
}});
</script>
</body>
</html>"""
    return html


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(base_dir, 'docs')
    os.makedirs(docs_dir, exist_ok=True)

    for filename_base, title, *_ in DOCUMENTS:
        md_path = os.path.join(base_dir, f'{filename_base}.md')
        if not os.path.exists(md_path):
            print(f"  SKIP {filename_base}.md (not found)")
            continue

        html = convert_md_to_html(md_path, filename_base)
        out_path = os.path.join(docs_dir, f'{filename_base}.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"  OK   {filename_base}.html")

    # Generate index.html redirect
    index_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="0; url=T_INDEX.html">
<title>Structural Necessity — Redirecting</title>
</head>
<body>
<p>Redirecting to <a href="T_INDEX.html">Index</a>...</p>
</body>
</html>"""
    with open(os.path.join(docs_dir, 'index.html'), 'w') as f:
        f.write(index_html)
    print("  OK   index.html (redirect)")

    print(f"\nDone. {len(DOCUMENTS)} documents generated in docs/")


if __name__ == '__main__':
    main()
