# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.19.10",
# ]
# ///

from pathlib import Path

import marimo

__generated_with = "0.19.11"
app = marimo.App()

ROOT = Path(__file__).resolve().parent
INDEX_HTML = ROOT / "index.html"
OUTPUT_HTML = ROOT / "output.html"

PROFILE = {
    "name": "Salamat Dauletbay",
    "title": "Accounting & Finance Student",
    "summary": (
        "First-year Accounting and Finance student at City, University of "
        "London with a strong interest in financial analysis, business "
        "development, and data-driven decision making."
    ),
    "email": "salamat.dauletbay@bayes.city.ac.uk",
    "github": "https://github.com/boranbai007",
    "linkedin": (
        "https://www.linkedin.com/in/salamat-dauletbay"
        "?utm_source=share_via&utm_content=profile&utm_medium=member_ios"
    ),
    "telegram": "https://t.me/boranbai_babakhanovich",
    "hero_image": str(ROOT / "assets" / "human.png"),
}

EDUCATION = [
    {
        "name": "Mander Portman Woodward Limited",
        "period": "Sep 2023 - Jun 2025",
    },
    {
        "name": "City St George's, University of London",
        "degree": "Bachelor's Degree, Accounting and Finance",
        "period": "Sep 2023 - Jun 2025",
        "image": str(ROOT / "assets" / "university.png"),
    },
]

PROJECTS = [
    {
        "title": "sedmarket.kz",
        "type": "Marketplace",
        "image": str(ROOT / "assets" / "sed.png"),
        "description": (
            "A wholesale marketplace for suppliers and buyers, simplifying "
            "purchasing, sales, and the search for reliable business partners."
        ),
    },
    {
        "title": "goldmarket.kz",
        "type": "Marketplace",
        "image": str(ROOT / "assets" / "gold.png"),
        "description": (
            "A jewelry marketplace for buying and selling gold accessories, "
            "offering elegant collections, trusted sellers, and a convenient "
            "shopping experience for premium jewelry."
        ),
    },
    {
        "title": "Portfolio website",
        "type": "Landing",
        "image": str(ROOT / "assets" / "portfolio.png"),
        "description": (
            "A personal portfolio website showcasing my education, skills, "
            "projects, experience, and professional achievements in finance, "
            "business, and data analysis."
        ),
    },
]

SKILL_GROUPS = [
    {
        "title": "Technical Skills",
        "items": ["Python", "Marimo", "Github", "Data Visualization"],
    },
    {
        "title": "Business Skills",
        "items": [
            "Financial Analysis",
            "Problem Solving",
            "Communication",
            "Critical Thinking",
        ],
    },
]

CONTACT_TEXT = (
    "I am always open to new opportunities, networking, and professional "
    "collaboration in finance, business, and analytics."
)


def copy_index_to_output() -> Path:
    OUTPUT_HTML.write_bytes(INDEX_HTML.read_bytes())
    return OUTPUT_HTML

@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    output_path = copy_index_to_output()
    return (output_path,)


@app.cell
def _(mo, output_path):
    mo.callout(
        mo.md(
            f"`{output_path.name}` updated as an exact byte-for-byte copy of `index.html`."
        ),
        kind="success",
    )
    return


if __name__ == "__main__":
    out = copy_index_to_output()
    print(f"Written {out} from {INDEX_HTML.name}")
