import os
from compile.utils import read_file,write_file,read_csv,key_dictlist_by
#import markdown2
from distutils.dir_util import copy_tree
from compile.generate_graphs import generate_all_graphs,save_graphs_as_files,encode_graphs_as_html
from compile.generate_legend import generate_legend
import json
import subprocess
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
import yaml
import copy

def compile_kramdown(fname):
    kramdown_args = [
        "ruby",
        "compile/kram.rb",
        fname
    ]
    out = subprocess.run(kramdown_args,stdout=subprocess.PIPE,encoding="utf-8").stdout
    print(out)
    return out

def markdown_to_html(paths):
    source_path,dest_path = paths
    out_html = compile_kramdown(source_path)#, extras=["fenced-code-blocks","header-ids","markdown-in-html","tables","wiki-tables"])
    write_file(dest_path,out_html)


def parse_relation(relation):
    if "<-" in relation or "->" in relation:
        if "<-" in relation:
            main,dependent = [n.strip() for n in relation.split("<-")]
        else:
            dependent,main = [n.strip() for n in relation.split("->")]
        relations = [
            {
                "type": "dependent",
                "source": main,
                "dest": dependent,
            },
            {
                "type": "application",
                "source": dependent,
                "dest": main,
            }
        ]
    elif "-" in relation:
        n1,n2 = [n.strip() for n in relation.split("-")]
        relations = [
            {
                "type": "equal",
                "source": n1,
                "dest": n2,
            },
            {
                "type": "equal",
                "source": n2,
                "dest": n1,
            }
        ]
    return relations

def construct_html_from_markdown(source_folder,dest_folder):
    os.makedirs(dest_folder,exist_ok=True)
    filenames = [fname for fname in os.listdir(source_folder) if ".md" == fname[-3:]]
    changed_filenames = [fname for fname in os.listdir()]
    pool = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
    out_paths = []
    for fname in filenames:
        spath = os.path.join(source_folder,fname)
        dpath = os.path.join(dest_folder,fname)+".html"
        #cached generatioin
        if not os.path.exists(dpath) or os.path.getmtime(dpath) < os.path.getmtime(spath) + 10:
            out_paths.append((spath,dpath))
    pool.map(markdown_to_html,out_paths)

def copy_static(source_folder,dest_folder):
    copy_tree(source_folder,dest_folder)

def generate_all_files(source_folder,dest_folder):
    construct_html_from_markdown(os.path.join(source_folder,"long_descriptions"),os.path.join(dest_folder,"long_descriptions"))
    copy_static(os.path.join(source_folder,"linked_data"),os.path.join(dest_folder,"linked_data"))
    graph_path = os.path.join(dest_folder,"graphs")
    graph_data = yaml.safe_load(read_file(os.path.join(source_folder,"graphdef.yaml")))
    nodes = graph_data['nodes']
    node_types = graph_data['node_types']

    rels = sum([parse_relation(rel) for rel in graph_data['relations']],[])
    rel_types = {
        "dependent": {
            "name": "Dependent",
            "color": "green",
        },
        "equal": {
            "name": "Equal",
            "color": "black",
        },
        "application": {
            "name": "Application",
            "color": "red",
        }
    }
    #nodes = read_csv(os.path.join(source_folder,"nodes.csv"))
    #rels = read_csv(os.path.join(source_folder,"relationships.csv"))
    #node_type_list = read_csv(os.path.join(source_folder,"node-types.csv"))
    #rel_type_list = read_csv(os.path.join(source_folder,"rel-types.csv"))
    #node_types = key_dictlist_by(node_type_list,'type_id')
    #rel_types = key_dictlist_by(rel_type_list,'type_id')
    nodes_list = [{"node":k,**v} for k,v in nodes.items()]
    node_types_list = [{"type_id":k,**v} for k,v in node_types.items()]
    rel_types_list = [{"type_id":k,**v} for k,v in rel_types.items()]

    all_graphs = generate_all_graphs(nodes_list,rels,node_types,rel_types)
    save_graphs_as_files(graph_path,all_graphs)
    graph_html = encode_graphs_as_html(all_graphs)
    json_str = json.dumps(nodes_list)
    js_str = f"var node_js_info = {json_str}"
    write_file(os.path.join(dest_folder,"node_js_info.js"), js_str)
    write_file(os.path.join(dest_folder,"node_js_info.json"), json_str)

    legend_html = generate_legend(node_types_list,rel_types_list)
    write_file(os.path.join(dest_folder,"legend.html"), legend_html)

    write_file(os.path.join(dest_folder,"graphs.html"), graph_html)


if __name__ == "__main__":
    #construct_html_from_markdown("examples/computer_science/long_descriptions/","test_out/long_descriptions/")
    generate_all_files("examples/computer_science/","test_out/")
