from diagrams import Diagram, Edge, Node

class DiagramImage:
    def __init__(self, diagram: dict, number:int):
        self.diagram = diagram
        self.state_number = number
        self._create_diagram()
    def _create_diagram(self):
        state_number = self.state_number
        with Diagram("Mealy Machine", show=True, direction="LR", filename="mealy", outformat="jpg"):
            state_node_list = []
            for a in range(state_number):
                state_node_list.append(Node(label=f"q{a}", shape="circle", height=".25", ))
            for b in range(state_number):
                for c in self.diagram:
                    state_node_list[b].connect(state_node_list[int(self.diagram[c][f'q{b}']['new_state'].replace("q", ""))],
                                               edge=Edge(color="red", label=f"{c}/{self.diagram[c][f'q{b}']['output']}",
                                                         forward=True, fontsize="15"))



