from pylatex import Document,TikZ,TikZNode,TikZOptions,Command
from pylatex.package import Package
from pylatex.utils import NoEscape
from pylatex.base_classes import Environment
import os
from IPython.display import Image
from IPython.core.display import HTML
import nltk
import re

# tkinter
import tkinter as tk



class nltk2tikz(Environment):
    """A class to NLTK draw trees in tikz"""
    _latex_name = 'tikzpicture'
    packages = [Package(NoEscape('tikz-qtree'))]
    escape = False
    content_separator = "\n"
    
    
    
def show_parse(tree,width=400):
    """
    use tikz to produce nltk.tree.Tree visualization
    """
    
    if not isinstance(tree,nltk.tree.Tree):
        try:
            raise ValueError('Object is not of nltk.tree.Tree type.')
        except:
            print('Object fails ...')
            return None
                    
    try:
        tree.draw()
    except tk.TclError:
        print('No X server, using TikZ engine ...')
    
    
    build_dir = 'img'
    if not os.path.exists(build_dir): os.mkdir(build_dir)
    #doc = Document(documentclass='standalone',document_options=NoEscape(r"convert={density=600,size=200,outext=.jpg}"))
    doc = Document(documentclass='standalone')
    output = re.sub(r'\s*,\s*',',',tree.pformat_latex_qtree()).replace('[]','')
    
    with doc.create(nltk2tikz()) as pic:        
        pic.append(output)
        
    # generate pdf and jpg
    doc.generate_pdf(filepath='{}/tikzdraw'.format(build_dir), clean_tex=True,compiler='pdflatex', compiler_args=['-output-directory {}'.format(build_dir)])
    os.system('convert -density 600 -quality 80 {0}/tikzdraw.pdf {0}/tikzdraw.jpg '.format(build_dir))
    img = Image('{}/tikzdraw.jpg'.format(build_dir),width=width,unconfined=True)
    os.system('rm -r {}'.format(build_dir))
    return img



    

if __name__ == '__main__':
    
    t = ['a',(1,2)]
    show_parse(t)

    t = nltk.Tree.fromstring('(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))')
    show_parse(t)
    
