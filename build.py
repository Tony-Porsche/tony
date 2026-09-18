#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages statiques du site (une page HTML par section, en FR et EN).
Ce script est un outil de fabrication — le livrable est le HTML qu'il produit,
qui n'a besoin d'aucun serveur ni build à l'exécution."""

import os

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = ["home", "about", "research", "projects", "cv", "contact"]

FR_FILES = {
    "home": "index.html",
    "about": "a-propos.html",
    "research": "recherche.html",
    "projects": "projets.html",
    "cv": "cv.html",
    "contact": "contact.html",
}
EN_FILES = {
    "home": "index.html",
    "about": "about.html",
    "research": "research.html",
    "projects": "projects.html",
    "cv": "cv.html",
    "contact": "contact.html",
}

NAV_LABELS = {
    "fr": {"home": "Accueil", "about": "À propos", "research": "Recherche",
           "projects": "Projets", "cv": "CV", "contact": "Contact"},
    "en": {"home": "Home", "about": "About", "research": "Research",
           "projects": "Projects", "cv": "CV", "contact": "Contact"},
}

TITLES = {
    "fr": {
        "home": "N'Goran Sylvain N'DRI — Économiste de l'énergie",
        "about": "À propos — N'Goran Sylvain N'DRI",
        "research": "Recherche — N'Goran Sylvain N'DRI",
        "projects": "Projets — N'Goran Sylvain N'DRI",
        "cv": "CV — N'Goran Sylvain N'DRI",
        "contact": "Contact — N'Goran Sylvain N'DRI",
    },
    "en": {
        "home": "N'Goran Sylvain N'DRI — Energy Economist",
        "about": "About — N'Goran Sylvain N'DRI",
        "research": "Research — N'Goran Sylvain N'DRI",
        "projects": "Projects — N'Goran Sylvain N'DRI",
        "cv": "CV — N'Goran Sylvain N'DRI",
        "contact": "Contact — N'Goran Sylvain N'DRI",
    },
}

FONT_LINK = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;'
             '0,9..144,600;1,9..144,500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500'
             '&display=swap" rel="stylesheet">')


def asset(lang, path):
    prefix = "../" if lang == "en" else ""
    return prefix + "assets/" + path


def page_href(lang, page):
    files = FR_FILES if lang == "fr" else EN_FILES
    return files[page]


def other_lang_href(lang, page):
    """Lien vers l'équivalent de la page courante dans l'autre langue."""
    if lang == "fr":
        return "en/" + EN_FILES[page]
    return "../" + FR_FILES[page]


def build_nav(lang, current):
    items = []
    for p in PAGES:
        label = NAV_LABELS[lang][p]
        href = page_href(lang, p)
        current_attr = ' aria-current="page"' if p == current else ""
        items.append(f'<li><a href="{href}"{current_attr}>{label}</a></li>')
    other = "EN" if lang == "fr" else "FR"
    items.append(f'<li><a class="lang-link" href="{other_lang_href(lang, current)}">{other}</a></li>')
    return "\n      ".join(items)


def base_page(lang, current, body_html, extra_head=""):
    home_href = page_href(lang, "home")
    role_word = "Économiste de l'énergie" if lang == "fr" else "Energy Economist"
    skip_label = "Aller au contenu" if lang == "fr" else "Skip to content"
    menu_label = "Ouvrir le menu" if lang == "fr" else "Open menu"
    rights = "Tous droits réservés." if lang == "fr" else "All rights reserved."
    built = "Site conçu pour GitHub Pages" if lang == "fr" else "Site built for GitHub Pages"

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{TITLES[lang][current]}</title>
{extra_head}
{FONT_LINK}
<link rel="stylesheet" href="{asset(lang, 'css/style.css')}">
<link rel="icon" href="data:,">
</head>
<body>

<a class="skip-link" href="#main">{skip_label}</a>

<header class="site-header">
  <nav class="nav">
    <a class="wordmark" href="{home_href}">N'Goran Sylvain N'DRI<small>{role_word}</small></a>
    <button class="nav-toggle" aria-expanded="false" aria-label="{menu_label}">☰</button>
    <ul class="nav-links">
      {build_nav(lang, current)}
    </ul>
  </nav>
</header>

<main id="main">
{body_html}
</main>

<footer class="site-footer">
  <div class="container">
    <span>© 2026 N'Goran Sylvain N'DRI — {rights}</span>
    <span>{built}</span>
  </div>
</footer>

<script src="{asset(lang, 'js/script.js')}"></script>
</body>
</html>
"""


HERO_SVG = """
      <div class="hero-chart" aria-hidden="true">
        <svg viewBox="0 0 460 300" xmlns="http://www.w3.org/2000/svg">
          <line x1="0" y1="255" x2="460" y2="255" stroke="rgba(255,255,255,0.18)" stroke-width="1"/>
          <g stroke="rgba(255,255,255,0.18)" stroke-width="1">
            <line x1="0" y1="255" x2="0" y2="262"/>
            <line x1="76" y1="255" x2="76" y2="262"/>
            <line x1="152" y1="255" x2="152" y2="262"/>
            <line x1="228" y1="255" x2="228" y2="262"/>
            <line x1="304" y1="255" x2="304" y2="262"/>
            <line x1="380" y1="255" x2="380" y2="262"/>
            <line x1="456" y1="255" x2="456" y2="262"/>
          </g>
          <path d="M0,60 C 90,75 150,120 220,165 C 300,205 360,235 460,248"
                fill="none" stroke="var(--fossil)" stroke-width="2.5" stroke-linecap="round"/>
          <path d="M0,240 C 90,225 150,190 220,150 C 300,100 360,60 460,35"
                fill="none" stroke="var(--renew)" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="222" cy="158" r="4.5" fill="var(--amber)"/>
          <line x1="222" y1="158" x2="222" y2="255" stroke="var(--amber)" stroke-width="1" stroke-dasharray="3 4"/>
          <text x="228" y="272" fill="var(--amber)" font-family="IBM Plex Mono, monospace" font-size="11">{tipping}</text>
          <circle cx="460" cy="248" r="3.5" fill="var(--fossil)"/>
          <circle cx="460" cy="35" r="3.5" fill="var(--renew)"/>
        </svg>
        <div class="chart-caption">
          <span><i class="dot" style="background:var(--fossil)"></i><span>{fossil}</span></span>
          <span><i class="dot" style="background:var(--renew)"></i><span>{renew}</span></span>
        </div>
      </div>
"""


def home_body(lang):
    fr = lang == "fr"
    eyebrow = "Économiste de l'énergie · Doctorant, Université de Sherbrooke" if fr else \
        "Energy Economist · PhD Candidate, Université de Sherbrooke"
    h1 = ('Faire compter l\u2019économie dans la <em>transition énergétique</em>' if fr else
          'Making economics count in the <em>energy transition</em>')
    lede = ("J'étudie les incitations financières, les minéraux critiques et les marchés électriques "
            "qui déterminent la vitesse à laquelle le monde délaisse les énergies fossiles." if fr else
            "I study the financial incentives, critical minerals, and electricity markets that determine "
            "how fast the world moves away from fossil fuels.")
    cta1_label = "Voir mes recherches" if fr else "See my research"
    cta2_label = "En savoir plus sur moi" if fr else "More about me"
    cta1_href = page_href(lang, "research")
    cta2_href = page_href(lang, "about")

    chart = HERO_SVG.format(
        tipping="point de bascule" if fr else "tipping point",
        fossil="part fossile" if fr else "fossil share",
        renew="part renouvelable" if fr else "renewable share",
    )

    intro_label = "Doctorant en économie à l'Université de Sherbrooke, au Québec (Canada)" if fr else \
        "PhD candidate in Economics at Université de Sherbrooke, Québec (Canada)"
    intro_p = ("Je suis économiste spécialisé dans la transition énergétique et l'adoption des technologies "
               "bas carbone — incitations financières, minéraux critiques, intégration des énergies "
               "intermittentes et fonctionnement des marchés électriques." if fr else
               "I am an economist specializing in the energy transition and the adoption of low-carbon "
               "technologies — financial incentives, critical minerals, intermittent renewable "
               "integration, and how electricity markets function.")
    more_label = "Lire mon parcours complet" if fr else "Read my full background"
    more_href = page_href(lang, "about")

    return f"""
  <section class="hero">
    <div class="container">
      <div class="hero-text">
        <span class="hero-eyebrow">{eyebrow}</span>
        <h1>{h1}</h1>
        <p class="hero-lede">{lede}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{cta1_href}">{cta1_label}</a>
          <a class="btn btn-ghost" href="{cta2_href}">{cta2_label}</a>
        </div>
      </div>
      {chart}
    </div>
  </section>

  <section class="home-intro">
    <div class="container">
      <div>
        <p style="font-weight:600;color:var(--teal);margin-bottom:10px;">{intro_label}</p>
        <p>{intro_p}</p>
      </div>
      <a class="btn btn-outline" href="{more_href}">{more_label}</a>
    </div>
  </section>
"""


def about_body(lang):
    fr = lang == "fr"
    eyebrow = "Profil" if fr else "Profile"
    title = "À propos" if fr else "About"
    role = ("Doctorant en économie à l'Université de Sherbrooke, au Québec (Canada)" if fr else
            "PhD candidate in Economics at Université de Sherbrooke, Québec (Canada)")
    p1 = ("Je suis économiste spécialisé dans la <strong>transition énergétique</strong> et l'adoption des "
          "technologies bas carbone. Mes recherches portent sur les incitations financières qui encouragent "
          "leur déploiement, la gestion des minéraux critiques, l'intégration des énergies intermittentes et "
          "le fonctionnement des marchés électriques." if fr else
          "I am an economist specializing in the <strong>energy transition</strong> and the adoption of "
          "low-carbon technologies. My research focuses on the financial incentives that drive their "
          "deployment, the management of critical minerals, the integration of intermittent renewable "
          "energy, and the functioning of electricity markets.")
    p2 = ("Formé en Côte d'Ivoire et en France, avec un <strong>Master en Politique Économique et "
          "Modélisation</strong> (2021) et un <strong>Master en Économie de l'Énergie et Développement "
          "Durable</strong> (2025), j'ai développé une expertise solide en analyse économique appliquée aux "
          "enjeux climatiques." if fr else
          "Trained in Côte d'Ivoire and France, with a <strong>Master's in Economic Policy and "
          "Modelling</strong> (2021) and a <strong>Master's in Energy Economics and Sustainable "
          "Development</strong> (2025), I have built solid expertise in economic analysis applied to "
          "climate issues.")
    goal = ("Mon objectif&nbsp;: contribuer à des solutions concrètes et innovantes pour accélérer la "
            "transition vers une économie bas carbone et répondre aux défis énergétiques mondiaux." if fr else
            "My goal: to contribute concrete, innovative solutions that accelerate the transition to a "
            "low-carbon economy and help meet the world's energy challenges.")
    loc_label = "Localisation" if fr else "Location"
    loc_val = "Sherbrooke, Québec, Canada"
    field_label = "Domaine" if fr else "Field"
    field_val = "Économie de l'énergie et de l'environnement" if fr else "Energy and environmental economics"
    alt = "Portrait de N'Goran Sylvain N'DRI" if fr else "Portrait of N'Goran Sylvain N'DRI"

    return f"""
  <section class="page-banner">
    <div class="container">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
    </div>
  </section>

  <section>
    <div class="container about-grid">
      <div class="about-side">
        <div class="about-portrait">
          <img src="{asset(lang, 'img/portrait.png')}" alt="{alt}" width="260" height="298">
        </div>
        <dl class="about-credentials">
          <dt>{loc_label}</dt>
          <dd>{loc_val}</dd>
          <dt>{field_label}</dt>
          <dd>{field_val}</dd>
        </dl>
      </div>
      <div class="about-body">
        <p style="font-weight:600;color:var(--teal);">{role}</p>
        <p>{p1}</p>
        <p>{p2}</p>
        <p class="pull-goal">{goal}</p>
      </div>
    </div>
  </section>
"""


# Comme pour PROJECTS : "year" est volontairement partagé (une date ne se
# traduit pas). "title_fr"/"title_en" et "co_fr"/"co_en" sont indépendants —
# modifier l'un ne change jamais l'autre, même quand leur contenu se
# ressemble (ex. un titre de papier resté en français des deux côtés).
PAPERS = [
    {"year": "2024", "title_fr": "Bioenergy and Land Use", "title_en": "Bioenergy and Land Use", "co_fr": "", "co_en": ""},
    {"year": "2024", "title_fr": "Dualité dans les industries de réseau",
     "title_en": "Dualité dans les industries de réseau", "co_fr": "", "co_en": ""},
    {"year": "2021", "title_fr": "Crédits en souffrance et performance bancaire&nbsp;: cas de l'UEMOA",
     "title_en": "Crédits en souffrance et performance bancaire: the case of UEMOA", "co_fr": "", "co_en": ""},
    {"year": "2020",
     "title_fr": "Institutions, gouvernance et développement économique&nbsp;: problèmes, réformes et "
                 "orientation de l'économie ivoirienne",
     "title_en": "Institutions, governance and economic development: challenges, reforms and direction "
                 "of the Ivorian economy",
     "co_fr": "avec Aka, Assié, Kouadio et Kouassi", "co_en": "with Aka, Assié, Kouadio and Kouassi"},
    {"year": "2020", "title_fr": "Estimation de la fonction de consommation des ménages ivoiriens",
     "title_en": "Estimating the consumption function of Ivorian households",
     "co_fr": "avec Kouamé", "co_en": "with Kouamé"},
]


def research_body(lang):
    fr = lang == "fr"
    eyebrow = "Publications" if fr else "Publications"
    title = "Recherche" if fr else "Research"
    lede = "Documents de travail et principaux intérêts académiques." if fr else \
        "Working papers and main academic interests."

    items = []
    for p in PAPERS:
        title_txt = p["title_fr"] if fr else p["title_en"]
        co_txt = p["co_fr"] if fr else p["co_en"]
        co_html = f'<p class="paper-coauthors">{co_txt}</p>' if co_txt else ""
        items.append(f"""        <li class="paper-item">
          <span class="paper-year">{p['year']}</span>
          <div>
            <p class="paper-title">{title_txt}</p>
            {co_html}
          </div>
        </li>""")
    items_html = "\n".join(items)

    return f"""
  <section class="page-banner">
    <div class="container">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      <p>{lede}</p>
    </div>
  </section>

  <section>
    <div class="container">
      <ul class="paper-list">
{items_html}
      </ul>
    </div>
  </section>
"""


# Chaque projet porte SES DEUX langues explicitement (suffixe _fr / _en) :
# modifier l'une ne touche jamais l'autre. Seul "url" (le lien externe) est
# volontairement partagé, car un lien Streamlit/Tableau/Power BI ne se traduit
# pas — c'est la même adresse quelle que soit la langue de la page.
PROJECTS = [
    {"tag_fr": "Streamlit", "tag_en": "Streamlit",
     "title_fr": "Index des projets", "title_en": "Project index",
     "desc_fr": "Portail regroupant l'ensemble des projets ci-dessous, déployé avec Streamlit.",
     "desc_en": "A portal gathering every project below, deployed with Streamlit.",
     "url": "https://sylvainndri-ndri-index-3czarp.streamlit.app/",
     "link_fr": "Ouvrir le portail", "link_en": "Open the portal"},
    {"tag_fr": "Risque de crédit", "tag_en": "Credit risk",
     "title_fr": "IFRS 9 & Stress Test", "title_en": "IFRS 9 & Stress Test",
     "desc_fr": "Modélisation du provisionnement des pertes de crédit attendues et scénarios de stress "
                "test bancaire.",
     "desc_en": "Expected credit loss provisioning model and bank stress-test scenarios.",
     "url": None},
    {"tag_fr": "Machine learning", "tag_en": "Machine learning",
     "title_fr": "Classification multiclasse", "title_en": "Multiclass classification",
     "desc_fr": "Modèle de classification multiclasse appliqué à des données réelles.",
     "desc_en": "A multiclass classification model applied to real-world data.",
     "url": None},
    {"tag_fr": "Machine learning", "tag_en": "Machine learning",
     "title_fr": "Prédiction du prix des maisons", "title_en": "House price prediction",
     "desc_fr": "Modèle de prédiction du prix des maisons à partir de caractéristiques structurelles et "
                "de localisation.",
     "desc_en": "A house-price prediction model based on structural and location features.",
     "url": None},
    {"tag_fr": "Tableau Public", "tag_en": "Tableau Public",
     "title_fr": "Tableau de bord", "title_en": "Dashboard",
     "desc_fr": "Tableau de bord interactif publié sur Tableau Public.",
     "desc_en": "Interactive dashboard published on Tableau Public.",
     "url": "https://public.tableau.com/app/profile/tony5276/viz/Tableaudebord_16713179649930/Tableaudebord",
     "link_fr": "Voir sur Tableau Public", "link_en": "View on Tableau Public"},
    {"tag_fr": "Tableau Public", "tag_en": "Tableau Public",
     "title_fr": "Tableau de bord 1 — marchés", "title_en": "Dashboard 1 — markets",
     "desc_fr": "Suivi de données boursières, tableau de bord n°1 sur Tableau Public.",
     "desc_en": "Stock market data tracking, dashboard #1 on Tableau Public.",
     "url": "https://public.tableau.com/app/profile/tony5276/viz/Stock_16720822769790/Tableaudebord1",
     "link_fr": "Voir sur Tableau Public", "link_en": "View on Tableau Public"},
    {"tag_fr": "Tableau Public", "tag_en": "Tableau Public",
     "title_fr": "Tableau de bord 2", "title_en": "Dashboard 2",
     "desc_fr": "Tableau de bord n°2, complément d'analyse sur Tableau Public.",
     "desc_en": "Dashboard #2, a follow-up analysis on Tableau Public.",
     "url": None},
    {"tag_fr": "Power BI", "tag_en": "Power BI",
     "title_fr": "Tableau de bord Power BI", "title_en": "Power BI dashboard",
     "desc_fr": "Tableau de bord construit avec Power BI.",
     "desc_en": "Dashboard built with Power BI.",
     "url": None},
]


def projects_body(lang):
    fr = lang == "fr"
    eyebrow = "Applications &amp; tableaux de bord" if fr else "Apps &amp; dashboards"
    title = "Projets" if fr else "Projects"
    lede = "Modélisation, visualisation de données et outils interactifs." if fr else \
        "Modelling, data visualization, and interactive tools."

    cards = []
    for p in PROJECTS:
        tag = p["tag_fr"] if fr else p["tag_en"]
        title_txt = p["title_fr"] if fr else p["title_en"]
        desc = p["desc_fr"] if fr else p["desc_en"]
        link_html = ""
        if p["url"]:
            link_label = p["link_fr"] if fr else p["link_en"]
            link_html = f'\n          <a href="{p["url"]}" target="_blank" rel="noopener">{link_label}</a>'
        cards.append(f"""        <div class="project-card">
          <span class="project-tag">{tag}</span>
          <h3>{title_txt}</h3>
          <p>{desc}</p>{link_html}
        </div>""")
    cards_html = "\n".join(cards)

    return f"""
  <section class="page-banner">
    <div class="container">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      <p>{lede}</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="project-grid">
{cards_html}
      </div>
    </div>
  </section>
"""


def cv_body(lang):
    fr = lang == "fr"
    eyebrow = "Parcours" if fr else "Background"
    title = "Curriculum vitae" if fr else "Curriculum vitae"
    lede = "Formation, expérience et compétences en détail." if fr else \
        "Education, experience, and skills in detail."
    label = "N'Goran Sylvain N'DRI — Économiste de l'énergie" if fr else \
        "N'Goran Sylvain N'DRI — Energy Economist"
    dl_fr = "Télécharger le CV (FR)" if fr else "Download CV (FR)"
    dl_en = "Télécharger le CV (EN)" if fr else "Download CV (EN)"
    notice = ("Les fichiers PDF ne sont pas encore en ligne&nbsp;: déposez-les dans "
              "<code>assets/cv/</code> sous les noms indiqués ci-dessus pour activer ces boutons." if fr else
              "The PDF files are not uploaded yet: add them to <code>assets/cv/</code> under the file "
              "names above to activate these buttons.")

    return f"""
  <section class="page-banner">
    <div class="container">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{title}</h1>
      <p>{lede}</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="cv-box">
        <p>{label}</p>
        <div class="cv-actions">
          <a class="btn btn-outline" href="{asset(lang, 'cv/CV-NDRI-FR.pdf')}">{dl_fr}</a>
          <a class="btn btn-outline" href="{asset(lang, 'cv/CV-NDRI-EN.pdf')}">{dl_en}</a>
        </div>
      </div>
      <p class="cv-notice">{notice}</p>
    </div>
  </section>
"""


def contact_body(lang):
    fr = lang == "fr"
    eyebrow = "Collaboration"
    title = "Prêt à façonner l'avenir par la recherche&nbsp;?" if fr else \
        "Ready to shape the future through research?"
    lede = ("Remplissez le formulaire en quelques clics pour que nous co-construisions une solution durable "
            "pour la nouvelle génération." if fr else
            "Fill out the form in a few clicks so we can co-build a sustainable solution for the next "
            "generation.")
    email_label = "Écrire un courriel" if fr else "Send an email"
    li_hint = "profil professionnel" if fr else "professional profile"
    orcid_hint = "identifiant chercheur" if fr else "researcher ID"
    rg_hint = "publications" if fr else "publications"

    return f"""
  <section class="contact-section">
    <div class="container contact-grid">
      <div>
        <span class="eyebrow">{eyebrow}</span>
        <h1>{title}</h1>
        <p class="contact-lede">{lede}</p>
        <!-- TODO : remplacez par votre adresse courriel réelle -->
        <a class="btn btn-primary" href="mailto:contact@sylvain-ndri.com">{email_label}</a>
      </div>
      <ul class="social-list">
        <!-- TODO : remplacez les liens # par vos profils réels -->
        <li><a href="#" target="_blank" rel="noopener">LinkedIn <span class="hint">{li_hint}</span></a></li>
        <li><a href="#" target="_blank" rel="noopener">ORCID <span class="hint">{orcid_hint}</span></a></li>
        <li><a href="#" target="_blank" rel="noopener">ResearchGate <span class="hint">{rg_hint}</span></a></li>
      </ul>
    </div>
  </section>
"""


BODY_BUILDERS = {
    "home": home_body,
    "about": about_body,
    "research": research_body,
    "projects": projects_body,
    "cv": cv_body,
    "contact": contact_body,
}


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


for lang, files in (("fr", FR_FILES), ("en", EN_FILES)):
    for page in PAGES:
        body = BODY_BUILDERS[page](lang)
        html = base_page(lang, page, body)
        rel_path = files[page] if lang == "fr" else f"en/{files[page]}"
        write(rel_path, html)

print("Terminé.")
