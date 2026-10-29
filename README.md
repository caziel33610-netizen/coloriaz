# Coloriaz

Site de coloriage sur téléphone pour les petits : coloriaz.fr

## Contenu

- `index.html` : le site (accueil, coloriage au pot de peinture, motifs à coller)
- `themes.js` : la liste des thèmes et des dessins
- `img/` : les dessins à colorier (un fichier PNG par dessin)
- `covers/` : l'image coloriée de chaque thème sur l'accueil (`covers/<id du thème>.png`)
- `motifs/` : les motifs à coller

## Ajouter un dessin

1. Mettre l'image dans `img/` (dessin au trait noir sur fond blanc, carré, environ 720 × 720 px).
2. Dans `themes.js`, ajouter son nom dans la liste `items` du thème, et une ligne dans `IMAGES`.

## Ajouter un thème

1. Ajouter un bloc `{ id, label, icon, cover, items }` dans `THEMES` (fichier `themes.js`).
2. Ajouter l'image coloriée de l'accueil dans `covers/<id>.png`.

Le site n'a besoin d'aucun serveur : ce sont des fichiers statiques.
