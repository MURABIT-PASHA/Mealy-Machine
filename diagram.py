from diagrams import Diagram, Edge, Node


def create_diagram(diagram, number):
    state_number = number
    with Diagram("Mealy Machine", show=True, direction="LR"):
        # Her bir state için Node oluşturacağız ve bunları state_node_list içine atacağız
        state_node_list = []
        for a in range(state_number):
            state_node_list.append(Node(label=f"q{a}", shape="circle", height=".25", ))
        # Şimdi bağlama işlemlerini yapmamız gerekiyor
        for b in range(state_number):
            for c in diagram:
                state_node_list[b].connect(state_node_list[int(diagram[c][f'q{b}']['new_state'].replace("q", ""))],
                                           edge=Edge(color="red", label=f"{c}/{diagram[c][f'q{b}']['output']}",
                                                     forward=True, fontsize="15"))


class DiagramImage:
    def __init__(self, diagram, number):
        self.diagram = diagram
        self.state_number = number
        create_diagram(diagram, number)
