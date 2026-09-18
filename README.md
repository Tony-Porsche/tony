# Site personnel — N'Goran Sylvain N'DRI

Site statique (HTML/CSS/JS pur, sans dépendances) avec bascule Français/Anglais,
prêt à héberger sur GitHub Pages.

## Structure

```
.
├── index.html              page unique (Accueil, À propos, Recherche, Projets, CV, Contact)
├── assets/
│   ├── css/style.css        design (couleurs, typographie, mise en page)
│   ├── js/script.js         bascule de langue FR/EN + menu mobile
│   ├── img/portrait.png     photo de profil
│   └── cv/                  déposez ici vos fichiers CV (voir ci-dessous)
└── README.md
```

## À compléter avant publication

Trois choses ont été laissées en attente le temps que vous ayez les vraies informations
(cherchez `TODO` dans `index.html`) :

1. **CV** — déposez vos PDF dans `assets/cv/` sous les noms `CV-NDRI-FR.pdf` et
   `CV-NDRI-EN.pdf` (ou modifiez les chemins dans la section `#cv` de `index.html`).
2. **Courriel** — remplacez `mailto:contact@sylvain-ndri.com` par votre adresse réelle.
3. **Réseaux** — remplacez les `href="#"` de LinkedIn, ORCID et ResearchGate par vos
   liens réels, dans la section `#contact`.

Vous pouvez aussi ajuster les intitulés et ajouter des articles de blog plus tard
(la section n'existe pas encore, elle peut être ajoutée facilement).

## Publier sur GitHub Pages

1. Créez un nouveau dépôt sur GitHub (public), par exemple `sylvain-ndri.github.io`
   ou un nom quelconque comme `site-perso`.
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
   - ou directement `https://<votre-utilisateur>.github.io/` si le dépôt s'appelle
     `<votre-utilisateur>.github.io`.

## Utiliser votre domaine personnalisé (sylvain-ndri.com)

1. Créez un fichier `CNAME` à la racine du dépôt contenant seulement :
   ```
   www.sylvain-ndri.com
   ```
2. Chez votre fournisseur de domaine, ajoutez un enregistrement CNAME pointant
   `www` vers `<votre-utilisateur>.github.io`.
3. Dans **Settings → Pages**, indiquez le même domaine personnalisé et activez
   « Enforce HTTPS » une fois le certificat généré.

## Modifier le contenu

- **Textes** : tout le texte visible passe par `assets/js/script.js` (objet
  `translations`), pour que la bascule FR/EN reste synchronisée. Modifiez les
  deux langues en parallèle.
- **Couleurs / typographie** : variables au tout début de `assets/css/style.css`
  (`:root { ... }`).
- **Projets / publications** : blocs `.project-card` et `.paper-item` dans
  `index.html` — dupliquez un bloc existant pour en ajouter un nouveau.
