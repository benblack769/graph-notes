import os
from compile.utils import read_file,write_file
from compile.generate_folder_structure import generate_all_files
import json


def generate_base(source_folder,dest_folder):
    pjoin = os.path.join
    generate_all_files(source_folder,dest_folder)

    base_template = read_file("templates/base.html")
    out_base = base_template.format(
        base_style=read_file("static/standalone.css"),
        base_script=read_file("static/standalone.js"),
        svg_data_elements=read_file(pjoin(dest_folder,"graphs.html")),
        legend=read_file(pjoin(dest_folder,"legend.html")),
        js_node_info=read_file(pjoin(dest_folder,"node_js_info.json")),
    )
    return out_base

if __name__ == "__main__":
    base_text = generate_base("examples/computer_science/")
    write_file("base.html",base_text)
