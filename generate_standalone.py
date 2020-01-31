import os
from compile.utils import read_file,write_file
from compile.generate_folder_structure import generate_all_files
from generate_embed import generate_base



def generate_standalone(source_folder):
    temp_folder = "test_out"
    base_text = generate_base(source_folder)
    standalone_template = read_file("templates/standalone.html")
    out_standalone = standalone_template.format(content=base_text)
    return out_standalone

if __name__ == "__main__":
    out_text = generate_standalone("examples/computer_science/")

    write_file("standalone.html",out_text)
