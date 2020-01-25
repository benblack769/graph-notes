import markdown
import os
from compile.utils import read_file,write_file

def construct_html_docs(folder):
    for fname in os.listdir(folder):
        path = os.path.join(folder,fname)
