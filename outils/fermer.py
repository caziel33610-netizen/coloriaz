"""Referme les petites ouvertures d'un dessin (pare-chocs, bas de caisse…)
pour que la couleur ne s'échappe pas dans le fond.
On ajoute un petit pont d'encre seulement s'il isole une vraie zone du dessin."""
import sys
from PIL import Image
import numpy as np
from scipy import ndimage as nd
def disk(r):
    y,x=np.ogrid[-r:r+1,-r:r+1]; return x*x+y*y<=r*r
def bg(g):
    free=(255-g)<=140; L,_=nd.label(free); return L==L[0,0]
def fermer(src,dst):
    g=np.array(Image.open(src).convert('L')).astype(float)
    ink=g<128; b=bg(g); added=0
    for r in (4,7,10,14,20,26):
        cl=nd.binary_closing(np.pad(ink,40),structure=disk(r))[40:-40,40:-40]
        cand=cl&~ink&b
        L,n=nd.label(cand); sz=nd.sum(cand,L,range(1,n+1))
        for k in np.argsort(sz):
            if sz[k]>40*r: continue
            m=L==k+1
            if not (m&b).any(): continue
            g2=g.copy(); g2[m]=25; b2=bg(g2)
            sealed=b.sum()-b2.sum()-m.sum()
            if sealed>max(1500,4*m.sum()):
                g=g2; b=b2; ink=ink|m; added+=1
    Image.fromarray(g.astype(np.uint8)).save(dst,optimize=True)
    return added
if __name__=='__main__':
    for p in sys.argv[1:]: print(p, fermer(p,p))

def enveloppe(src,dst,r=22):
    """Dernier recours : trace le contour extérieur du dessin là où il est ouvert."""
    g=np.array(Image.open(src).convert('L')).astype(float)
    ink=g<128
    sil=nd.binary_fill_holes(nd.binary_closing(np.pad(ink,60),structure=disk(r))[60:-60,60:-60])
    edge=sil&~nd.binary_erosion(sil,iterations=4)
    b=bg(g); add=edge&b&~ink
    before=b.sum(); g2=g.copy(); g2[add]=25
    sealed=before-bg(g2).sum()-add.sum()
    if sealed>1500: Image.fromarray(g2.astype(np.uint8)).save(dst,optimize=True); return int(sealed)
    return 0
