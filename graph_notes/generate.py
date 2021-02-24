import os
from .compile.utils import read_file,write_file
from .compile.generate_folder_structure import generate_all_files
import json
from pathlib import Path


def generate_base(source_folder,dest_folder):
    pjoin = os.path.join
    libdir = Path(__file__).parent
    generate_all_files(source_folder,dest_folder,libdir)

    base_template = read_file(libdir/"templates/base.html")
    out_base = base_template.format(
        base_style=read_file(libdir/"static/standalone.css"),
        markdown_alt=read_file(libdir/"static/markdown_alt.css"),
        pygments=read_file(libdir/"static/pygments.css"),
        base_script=read_file(libdir/"static/standalone.js"),
        svg_data_elements=read_file(pjoin(dest_folder,"graphs.html")),
        legend=read_file(pjoin(dest_folder,"legend.html")),
        js_node_info=read_file(pjoin(dest_folder,"node_js_info.json")),
    )
    return out_base


def generate_standalone(source_folder,dest_folder):
    libdir = Path(__file__).parent
    base_text = generate_base(source_folder,dest_folder)
    standalone_template = read_file(libdir/"templates/standalone.html")
    out_standalone = standalone_template.format(content=base_text)

    write_file(os.path.join(dest_folder,"index.html"),out_standalone)
