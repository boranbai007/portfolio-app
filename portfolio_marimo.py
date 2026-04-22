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
def _(mo):
    mo.md("# Salamat Dauletbay Portfolio").style(
        {
            "font-size": "40px",
            "font-weight": "700",
            "margin-bottom": "12px",
        }
    )
    return


@app.cell
def _(mo):
    badge = mo.md(PROFILE["title"]).style(
        {
            "display": "inline-block",
            "padding": "6px 20px",
            "border-radius": "9999px",
            "background-color": "#242424",
            "color": "white",
            "font-weight": "600",
            "font-size": "14px",
        }
    )

    name = mo.md(PROFILE["name"]).style(
        {
            "font-size": "56px",
            "font-weight": "700",
            "line-height": "1.05",
            "margin-top": "14px",
        }
    )

    summary = mo.md(PROFILE["summary"]).style(
        {
            "max-width": "740px",
            "font-size": "15px",
            "font-weight": "500",
            "color": "#4F4D44",
            "margin-top": "18px",
        }
    )

    mo.vstack([badge, name, summary], gap=0).style({"margin-bottom": "28px"})
    return


@app.cell
def _(mo):
    contact = mo.md(f"[Contact Me](mailto:{PROFILE['email']})").style(
        {
            "display": "inline-block",
            "padding": "10px 24px",
            "border-radius": "16px",
            "background-color": "#242424",
            "color": "white",
            "font-weight": "600",
            "text-decoration": "none",
            "margin-right": "12px",
        }
    )

    linkedin = mo.md(f"[LinkedIn]({PROFILE['linkedin']})").style(
        {
            "display": "inline-block",
            "padding": "10px 24px",
            "border-radius": "16px",
            "background-color": "white",
            "color": "#242424",
            "font-weight": "600",
            "text-decoration": "none",
        }
    )

    mo.hstack([contact, linkedin], gap=8).style({"margin-bottom": "24px"})
    return


@app.cell
def _(mo):
    mo.image(PROFILE["hero_image"]).style(
        {
            "max-width": "360px",
            "width": "100%",
            "border-radius": "16px",
            "background": "white",
            "padding": "10px",
            "margin-bottom": "28px",
        }
    )
    return

@app.cell
def _(mo):
    mo.md("## Education").style({"font-size": "34px", "font-weight": "700"})

    left = mo.vstack(
        [
            mo.md(EDUCATION[0]["name"]).style({"font-size": "24px", "font-weight": "700"}),
            mo.md(EDUCATION[0]["period"]).style({"color": "#4F4D44", "font-weight": "600"}),
        ],
        justify="space-between",
    ).style(
        {
            "background": "white",
            "border-radius": "16px",
            "padding": "24px",
            "min-height": "160px",
            "flex": "1",
        }
    )

    right = mo.vstack(
        [
            mo.md(EDUCATION[1]["name"]).style({"font-size": "24px", "font-weight": "700"}),
            mo.md(EDUCATION[1]["degree"]).style({"color": "#4F4D44", "font-weight": "600"}),
            mo.md(EDUCATION[1]["period"]).style({"color": "#4F4D44", "font-weight": "600"}),
        ],
        gap=8,
    ).style(
        {
            "background": "white",
            "border-radius": "16px",
            "padding": "24px",
            "flex": "1.5",
        }
    )

    mo.hstack([left, right], widths=[0.4, 0.6], gap=12).style({"margin-top": "10px"})
    return


@app.cell
def _(mo):
    mo.md("## Projects").style({"font-size": "34px", "font-weight": "700"})

    project_cards = []
    for project in PROJECTS:
        img = mo.image(project["image"]).style(
            {
                "width": "100%",
                "aspect-ratio": "16 / 9",
                "object-fit": "cover",
                "border-radius": "16px",
                "background": "white",
            }
        )

        text = mo.vstack(
            [
                mo.md(project["title"]).style({"font-size": "26px", "font-weight": "700"}),
                mo.md(project["type"]).style({"color": "#4F4D44", "font-weight": "600"}),
                mo.md(project["description"]).style({"color": "#4F4D44", "font-weight": "500"}),
            ],
            gap=6,
        ).style(
            {
                "background": "white",
                "border-radius": "16px",
                "padding": "24px",
                "height": "100%",
            }
        )

        project_cards.append(mo.hstack([img, text], widths=[0.38, 0.62], gap=12))

    mo.vstack(project_cards, gap=14).style({"margin-top": "10px"})
    return

@app.cell
def _(mo):
    mo.md("## Skills & Tools").style({"font-size": "34px", "font-weight": "700"})

    blocks = []
    for group in SKILL_GROUPS:
        pills = [
            mo.md(item).style(
                {
                    "display": "inline-block",
                    "background": "#242424",
                    "color": "white",
                    "padding": "8px 18px",
                    "border-radius": "9999px",
                    "font-size": "13px",
                    "font-weight": "600",
                    "margin-right": "8px",
                    "margin-bottom": "8px",
                }
            )
            for item in group["items"]
        ]

        block = mo.vstack(
            [
                mo.md(group["title"]).style({"font-size": "26px", "font-weight": "700"}),
                mo.hstack(pills, wrap=True, gap=4),
            ],
            gap=8,
        ).style(
            {
                "background": "white",
                "border-radius": "16px",
                "padding": "24px",
                "flex": "1",
            }
        )
        blocks.append(block)

    mo.hstack(blocks, gap=12).style({"margin-top": "10px"})
    return

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
