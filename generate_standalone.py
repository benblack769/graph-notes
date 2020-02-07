import os
from compile.utils import read_file,write_file
from compile.generate_folder_structure import generate_all_files
from generate_embed import generate_base
import argparse


def generate_standalone(source_folder,dest_folder):
    base_text = generate_base(source_folder,dest_folder)
    standalone_template = read_file("templates/standalone.html")
    out_standalone = standalone_template.format(content=base_text)
    return out_standalone

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''
        Turn a notes folder with a graphdef and markdown description
         files and turn it into a browsable folder of html documents.

         Example:

         python generate_standalone.py examples/computer_science/ test_out/
    ''')
    parser.add_argument('source_folder', help='Path to folder full of graphdef and markdown description files.')
    parser.add_argument('dest_folder', help='Path to output folder where html files will be stored.')
    args = parser.parse_args()

    source_folder = args.source_folder
    dest_folder = args.dest_folder

    out_text = generate_standalone(source_folder,dest_folder)

    write_file(os.path.join(dest_folder,"index.html"),out_text)
