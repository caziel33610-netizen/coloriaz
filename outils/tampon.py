"""Avant chaque mise en ligne : nouveau numéro de version.
Les téléphones voient alors qu'il y a du nouveau et rechargent dessins et images."""
import re, time
b = time.strftime('%Y%m%d%H%M%S')
p = 'index.html'; s = open(p, encoding='utf-8').read()
s = re.sub(r'<meta name="build" content="\d+">', f'<meta name="build" content="{b}">', s)
s = re.sub(r'<script src="themes\.js(\?v=\d+)?"></script>', f'<script src="themes.js?v={b}"></script>', s)
open(p, 'w', encoding='utf-8').write(s)
open('version.txt', 'w').write(b + '\n')
print(b)
