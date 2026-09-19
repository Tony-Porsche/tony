# Site personnel — N'Goran Sylvain N'DRI

Site statique (HTML/CSS/JS pur, sans dépendance) — une page par section, en
français à la racine et en anglais dans `/en/`. Prêt à héberger tel quel sur
GitHub Pages.

## Structure

```
.
├── index.html            Accueil (FR)
├── a-propos.html         À propos
├── recherche.html        Recherche
├── projets.html          Projets
├── blog.html             Blog
├── cv.html               CV
├── contact.html          Contact
├── en/
│   ├── index.html        Home (EN)
│   ├── about.html
│   ├── research.html
│   ├── projects.html
│   ├── blog.html
│   ├── cv.html
│   └── contact.html
├── assets/
│   ├── css/style.css      design (couleurs, typographie, mise en page)
│   ├── js/script.js       menu mobile uniquement
│   ├── img/portrait.png   photo de profil
│   ├── img/logo.png       logo (affiché dans l'en-tête, sur les 12 pages)
│   ├── img/banners/       vos photos de bannière, une par section (voir ci-dessous)
│   └── cv/                déposez ici vos fichiers CV (voir ci-dessous)
├── build.py              script qui a généré les 14 pages (facultatif à garder)
└── README.md
```

Chaque page française porte un lien « EN » vers sa page anglaise équivalente,
et vice-versa — ce sont de simples liens `<a href>`, donc rien ne peut
« ne pas marcher » comme avec un bouton JavaScript.

## Ajouter vos photos de bannière

Chaque section a sa propre bannière (le bandeau sombre en haut de page, avec
le texte écrit par-dessus) et peut afficher une photo différente. Déposez vos
images dans `assets/img/banners/` sous ces noms exacts :

| Fichier attendu                   | Section                     |
|------------------------------------|------------------------------|
| `assets/img/banners/home.jpg`      | Accueil (grande bannière)   |
| `assets/img/banners/about.jpg`     | À propos                    |
| `assets/img/banners/research.jpg`  | Recherche                   |
| `assets/img/banners/projects.jpg`  | Projets                      |
| `assets/img/banners/blog.jpg`      | Blog                          |
| `assets/img/banners/cv.jpg`        | CV                            |
| `assets/img/banners/contact.jpg`   | Contact                       |

La même photo sert aux deux langues (FR et EN) d'une même section — inutile
d'en dupliquer une pour `/en/`. Tant qu'un fichier n'existe pas encore, la
bannière correspondante affiche simplement le fond vert sapin, sans rien
casser.

Conseils pratiques :
- Format paysage, au moins 1600px de large, en `.jpg` (remplacez l'extension
  dans `build.py`, dictionnaire `BANNER_IMAGES`, si vous préférez `.png` ou
  `.webp`).
- Le texte est toujours blanc et placé à gauche, sur un dégradé sombre qui
  s'assure qu'il reste lisible quelle que soit la photo — inutile d'assombrir
  vous-même vos photos avant de les déposer.
- Pour changer les noms de fichiers ou le dossier, modifiez le dictionnaire
  `BANNER_IMAGES` en haut de `build.py`, puis relancez `python3 build.py`.

## Modifier le contenu

Deux façons de faire, au choix :

- **À la main** : éditez directement le fichier `.html` de la page concernée.
  Toutes les pages partagent le même `assets/css/style.css`, donc un
  changement de couleur ou de police se fait à un seul endroit.
- **Via le générateur** : si vous préférez garder une seule source de texte,
  modifiez les textes dans `build.py` (dictionnaires `PAPERS`, `PROJECTS`,
  et les fonctions `*_body`), puis relancez :
  ```bash
  python3 build.py
  ```
  Cela régénère les 14 fichiers HTML à l'identique de la structure actuelle.
  Le script n'est utile qu'au moment où vous éditez le contenu — le site
  publié reste du HTML/CSS/JS statique, sans aucune dépendance à Python.

## Publier un article de blog

La page Blog est vide par défaut (elle affiche « Aucun article publié pour
l'instant »). Pour ajouter un article, ouvrez `build.py` et repérez la liste
`BLOG_POSTS` (juste avant `def blog_body`). Ajoutez-y un dict par article,
en français ET en anglais :

```python
BLOG_POSTS = [
    {"date": "2026-09-01",
     "title_fr": "Titre de l'article", "title_en": "Post title",
     "excerpt_fr": "Résumé en une phrase.", "excerpt_en": "One-sentence summary."},
]
```

Le plus récent en premier. Puis relancez `python3 build.py` — la page Blog
liste automatiquement chaque entrée, en FR sur `blog.html` et en EN sur
`en/blog.html`. Pour un article complet (pas seulement un résumé), il faudra
une page dédiée par article ; dites-le-moi et je mets ça en place.

## À compléter avant publication

Quatre choses ont été laissées en attente le temps que vous ayez les vraies
informations (cherchez `TODO` dans les fichiers, ou le texte « pas encore en
ligne » sur la page CV) :

1. **CV** — déposez vos PDF dans `assets/cv/` sous les noms `CV-NDRI-FR.pdf`
   et `CV-NDRI-EN.pdf` (mêmes fichiers utilisés par les pages FR et EN).
2. **Courriel** — remplacez `mailto:contact@sylvain-ndri.com` dans
   `contact.html` et `en/contact.html` par votre adresse réelle.
3. **Réseaux** — remplacez les `href="#"` de LinkedIn, ORCID et ResearchGate
   par vos liens réels, dans les deux pages contact.
4. **Photos de bannière** — déposez vos 7 photos dans `assets/img/banners/`
   (voir la section précédente pour les noms de fichiers attendus).

## Publier sur GitHub Pages

1. Créez un nouveau dépôt sur GitHub (public), par exemple
   `sylvain-ndri.github.io` ou un nom quelconque comme `site-perso`.
2. Poussez ce dossier tel quel à la racine du dépôt :
   ```bash
   git init
   git add .
   git commit -m "Site personnel"
   git branch -M main
   git remote add origin https://github.com/<votre-utilisateur>/<votre-depot>.git
   git push -u origin main
   ```
3. Dans le dépôt GitHub : **Settings → Pages → Build and deployment**,
   choisissez **Deploy from a branch**, branche `main`, dossier `/ (root)`.
4. Après une ou deux minutes, le site est en ligne à :
   - `https://<votre-utilisateur>.github.io/<votre-depot>/`
   - ou directement `https://<votre-utilisateur>.github.io/` si le dépôt
     s'appelle `<votre-utilisateur>.github.io`.

## Utiliser votre domaine personnalisé (sylvain-ndri.com)

1. Créez un fichier `CNAME` à la racine du dépôt contenant seulement :
   ```
   www.sylvain-ndri.com
   ```
2. Chez votre fournisseur de domaine, ajoutez un enregistrement CNAME
   pointant `www` vers `<votre-utilisateur>.github.io`.
3. Dans **Settings → Pages**, indiquez le même domaine personnalisé et
   activez « Enforce HTTPS » une fois le certificat généré.
