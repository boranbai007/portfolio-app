# Salamat Dauletbay Portfolio

This project is a personal portfolio webpage for Salamat Dauletbay. The page
includes a hero section, education, projects, skills, contact links, and a
floating navigation header that appears while scrolling.

The final webpage is generated from the Marimo/Python file:

```text
portfolio_marimo.py
```

The Python file stores the portfolio data in variables such as `PROFILE`,
`EDUCATION`, `PROJECTS`, and `SKILL_GROUPS`. HTML sections are created with
render functions like `render_hero()`, `render_projects()`, `render_skills()`,
and `render_contact()`.

## Compile to HTML

Run this command from the project folder:

```bash
python portfolio_marimo.py
```

This generates:

```text
output.html
```

Open `output.html` in a browser to view the compiled portfolio page.

## Optional Marimo Editor

If Marimo is installed, you can open the file in the notebook editor with:

```bash
marimo edit portfolio_marimo.py
```

Use the Python compile command above when you want to regenerate `output.html`.

## Editing Content

To update the website content, edit the data variables in the Python file:

- `PROFILE` for name, summary, email, GitHub, LinkedIn, Telegram, and hero image
- `EDUCATION` for education cards
- `PROJECTS` for project cards
- `SKILL_GROUPS` for technical and business skills

After editing, run the compile command again to regenerate `output.html`.
