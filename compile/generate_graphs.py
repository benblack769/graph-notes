from utils import read_csv,join,key_dictlist_by,linejoin,read_file,write_file
import subprocess
import os

def generate_graphviz_code(all_nodes,all_relations,show_nodes,node_types,rel_types):
    show_nodes = set(show_nodes)
    nodes = [n for n in all_nodes if n['node'] in show_nodes]
    relations = [rel for rel in all_relations
                if rel['source'] in show_nodes and rel['dest'] in show_nodes]

    node_graph = [f'{n["node"]} [label="{n["node"]}",color="{node_types[n["type"]]["color"]}",id={n["node"]}]' for n in nodes]
    rel_graph = [f'{rel["source"]} -> {rel["dest"]} [color="{rel_types[rel["type"]]["color"]}"]' for rel in relations]
    graph = f'''
        digraph search {{
        {linejoin(node_graph)}
        {linejoin(rel_graph)}
        }}
    '''
    return graph

def call_graphviz(graphviz_code):
    graphviz_args = "dot -Tsvg".split(' ')
    out = subprocess.run(graphviz_args,input=graphviz_code,stdout=subprocess.PIPE,encoding="utf-8").stdout
    #print("\n".join(out.split("\n")[:3]))
    #stripped = "\n".join(out.split("\n"))
    return out

def get_adj_list(nodes,relations):
    return {n['node']:[rel['dest'] for rel in relations if rel['source'] == n['node']] for n in nodes}

def score_nodes(root,adj_list):
    scores = dict()
    depth_nodes = [root]
    for x in range(10):
        new_depth_nodes = []
        for n in depth_nodes:
            if n not in scores:
                scores[n] = 8.**(-x) * (1+1e-5*len(adj_list[n]))
                for e in adj_list[n]:
                    new_depth_nodes.append(e)

        depth_nodes = new_depth_nodes

    sortables_scores = [(v,k) for k,v in scores.items()]
    sortables_scores.sort(reverse=True)
    return [n for v,n in sortables_scores]

def generate_all_graphs(dest_folder,nodes,relations,node_types,rel_types):
    adj_list = get_adj_list(nodes,relations)
    os.makedirs(dest_folder,exist_ok=True)
    for node in nodes:
        node_names = score_nodes(node['node'],adj_list)[:5]
        fname = node['node']+".svg"
        dest_path = os.path.join(dest_folder,fname)
        viz_code = generate_graphviz_code(nodes,relations,node_names,node_types,rel_types)
        svg_code = call_graphviz(viz_code)
        write_file(dest_path,svg_code)



if __name__ == "__main__":
    node_types = key_dictlist_by(read_csv("examples/computer_science/node-types.csv"),'type_id')
    rel_types = key_dictlist_by(read_csv("examples/computer_science/rel-types.csv"),'type_id')
    nodes = read_csv("examples/computer_science/nodes.csv")
    rels = read_csv("examples/computer_science/relationships.csv")
    show_nodes = [n['node'] for n in nodes]
    graph_code = (generate_graphviz_code(nodes,rels,show_nodes,node_types,rel_types))
    print(graph_code)
    svg_code = call_graphviz(graph_code)
    print(svg_code)
