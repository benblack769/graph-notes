import os
from compile.utils import read_file,write_file
from compile.generate_folder_structure import generate_all_files
from generate_embed import generate_base



def generate_standalone(source_folder,dest_folder):
    base_text = generate_base(source_folder,dest_folder)
    standalone_template = read_file("templates/standalone.html")
    out_standalone = standalone_template.format(content=base_text)
    return out_standalone

if __name__ == "__main__":
    dest_folder = "test_out"
    source_folder = "examples/computer_science/"
    out_text = generate_standalone(source_folder,dest_folder)

    write_file(os.path.join(dest_folder,"index.html"),out_text)
