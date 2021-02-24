from .utils import read_csv,join,linejoin


def generate_legend_part(types):
    header_names = ["Color","Name"]
    header_entries = [f"<th>{name}</th>" for name in header_names]
    header = f"<tr>{join(header_entries)}</tr>"
    body_rows = []
    for type in types:
        color = f'<td><span class="legend_box" style="background-color:{type["color"]}"></span></td>'
        name = f'<td>{type["name"]}</td>'
        row = f"<tr>{color}{name}</tr>"
        body_rows.append(row)
    table = f'<table>{header}{join(body_rows)}</table>'
    return table



def generate_legend(node_types,rel_types):
    node_part = generate_legend_part(node_types)
    rel_part = generate_legend_part(rel_types)
    return f'''
        <div class="legend_table">
            <h4>Node types</h4>
            {node_part}
        </div>
        <div class="legend_table">
            <h4>Relation types</h4>
            {rel_part}
        </div>
    '''


if __name__ == "__main__":
    node_types = read_csv("examples/computer_science/node-types.csv")
    rel_types = read_csv("examples/computer_science/rel-types.csv")
    print(generate_legend(node_types,rel_types))
