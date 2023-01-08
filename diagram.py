from diagrams import Diagram, Edge, Node
from tkinter import *
from tkinter import ttk
import PIL.Image, PIL.ImageTk
class DiagramImage:
    def __init__(self, diagram: dict, number:int, frame: Frame):
        self.diagram = diagram
        self.state_number = number
        self.frame = frame
        self.image = PhotoImage
        self.diagram_image = Image
        self._show_inside_the_frame()

    def _clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
    def _show_inside_the_frame(self):
        self._clear_frame()
        self.image = PIL.Image.open(self._create_diagram())
        golden_ratio = (1 + pow(5, 1 / 2)) / 2
        height = 400
        width = int(height * golden_ratio)
        self.diagram_image = self.image.resize((width, height))
        label = Label(master=self.frame, image=PIL.ImageTk.PhotoImage(self.diagram_image))
        label.grid(row=0, column=0)
        button = Button(master=self.frame, text="Test String")
        button.grid(padx=15, pady=15, row=1, column=0, sticky=E)

    def _create_diagram(self) -> str:
        state_number = self.state_number
        with Diagram("Mealy Machine", show=False, direction="LR", filename="mealy", outformat="jpg"):
            state_node_list = []
            for a in range(state_number):
                state_node_list.append(Node(label=f"q{a}", shape="circle", height=".25", ))
            for b in range(state_number):
                for c in self.diagram:
                    state_node_list[b].connect(state_node_list[int(self.diagram[c][f'q{b}']['new_state'].replace("q", ""))],
                                               edge=Edge(color="red", label=f"{c}/{self.diagram[c][f'q{b}']['output']}",
                                                         forward=True, fontsize="15"))
        return "mealy.jpg"

