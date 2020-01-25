import os
from utils import read_file,write_file,read_csv,key_dictlist_by
import markdown2
from distutils.dir_util import copy_tree
from generate_graphs import generate_all_graphs
import json

def construct_html_from_markdown(source_folder,dest_folder):
    os.makedirs(dest_folder,exist_ok=True)
    for fname in os.listdir(source_folder):
        if ".md" == fname[-3:]:
            source_path = os.path.join(source_folder,fname)
            dest_path = os.path.join(dest_folder,fname)+".html"
            out_html = markdown2.markdown(read_file(source_path), extras=["fenced-code-blocks","header-ids","markdown-in-html","tables","wiki-tables"])
            write_file(dest_path,out_html)

def copy_static(source_folder,dest_folder):
    copy_tree(source_folder,dest_folder)

def generate_all_files(source_folder,dest_folder):
    construct_html_from_markdown(os.path.join(source_folder,"long_descriptions"),os.path.join(dest_folder,"long_descriptions"))
    copy_static(os.path.join(source_folder,"linked_data"),os.path.join(dest_folder,"linked_data"))
    graph_path = os.path.join(dest_folder,"graphs")
    nodes = read_csv(os.path.join(source_folder,"nodes.csv"))
    rels = read_csv(os.path.join(source_folder,"relationships.csv"))
    node_types = key_dictlist_by(read_csv(os.path.join(source_folder,"node-types.csv")),'type_id')
    rel_types = key_dictlist_by(read_csv(os.path.join(source_folder,"rel-types.csv")),'type_id')
    generate_all_graphs(graph_path,nodes,rels,node_types,rel_types)

    js_str = f"var node_js_info = {json.dumps(nodes)}"
    write_file(os.path.join(dest_folder,"node_js_info.js"), js_str)


if __name__ == "__main__":
    #construct_html_from_markdown("examples/computer_science/long_descriptions/","test_out/long_descriptions/")
    generate_all_files("examples/computer_science/","test_out/")
