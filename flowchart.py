
from graphviz import Digraph

def generate_flowchart(steps, output_path="flowchart"):
    dot = Digraph(format='png')
    for frm, to in steps:
        dot.edge(frm, to)
    dot.render(output_path, cleanup=True)
    return output_path + ".png"
