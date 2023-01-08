from tkinter import *
from tkinter import ttk
import PIL.Image, PIL.ImageTk
from diagram import DiagramImage
class Scheme:
    def __init__(self, alphabet:str, state_number:str, master: Tk, main_frame: Frame):
        self.alphabet = alphabet
        self.state_number = int(state_number)
        self.master = master
        self.main_frame = main_frame
        self.group_list = []
        self.state_list = []
        self.alphabet_list = self.alphabet.replace(" ", "").split(",")
        self.diagram = {}
        self._create_scheme()

    def _clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def _create_scheme(self):
        state_number = self.state_number
        frame = self.main_frame
        column_amount = len(self.alphabet_list) * 2 + 1
        row_amount = state_number + 2
        index = 0
        alphabet_char = 0
        for _ in range(len(self.alphabet_list)):
            self.diagram[f"{self.alphabet_list[_]}"] = {}
            for y in range(state_number):
                self.diagram[f"{self.alphabet_list[_]}"][f"q{y}"] = {}
        for _ in range(state_number):
            self.state_list.append(f"q{_}")
        body_list = []
        self._clear_frame()
        for i in range(row_amount):
            for j in range(column_amount):
                if i == 0:
                    if j % 2 == 0:
                        alphabet_char = alphabet_char + 1
                        continue
                    else:
                        new_title = Label(master=frame, text=f"After input {self.alphabet_list[j - alphabet_char]}")
                        new_title.grid(row=i, column=j, columnspan=2)
                elif i == 1:
                    if j == 0:
                        new_title = Label(master=frame, text="Old State")
                        new_title.grid(row=i, column=j)
                    elif j % 2 == 0:
                        new_title = Label(master=frame, text="Output")
                        new_title.grid(row=i, column=j)
                    else:
                        new_title = Label(master=frame, text="New State")
                        new_title.grid(row=i, column=j)
                else:
                    if j == 0:
                        new_title = Label(master=frame, text=f"q{i - 2}")
                        new_title.grid(row=i, column=j)
                    elif j % 2 == 0:
                        new_value = Entry(master=frame, highlightthickness=1)
                        new_value.grid(row=i, column=j)
                        body_list.append([new_value, index])
                        index = index + 1
                    else:
                        state = ttk.Combobox(master=frame, values=self.state_list)
                        state.grid(row=i, column=j)
                        body_list.append([state, index])
        values = set(map(lambda x: x[1], body_list))
        self.group_list = [[y[0] for y in body_list if y[1] == x] for x in values]
        table_button = Button(master=frame, text="Create Diagram", command=self._create_diagram)
        table_button.grid(column=column_amount, row=row_amount)

    def _create_diagram(self):
        DiagramImage(diagram=self._create_table(), number=self.state_number)
        self._clear_frame()
        image = PIL.Image.open("mealy.jpg")
        golden_ratio = (1 + pow(5, 1 / 2)) / 2
        height = 400
        width = int(height * golden_ratio)
        new_image = image.resize((width, height))
        self.diagram_image = PIL.ImageTk.PhotoImage(new_image)
        label = Label(master=self.main_frame, image=self.diagram_image)
        label.pack()
    def _create_table(self)->dict:
        x = 0
        p = 0
        for w in self.diagram:
            for z in range(len(self.state_list)):
                self.diagram[w][f"q{z}"]["new_state"] = self.group_list[p + z + ((len(
                    self.alphabet_list) - 1) * x)][0].get()
                self.diagram[w][f"q{z}"]["output"] = self.group_list[p + z + ((len(
                    self.alphabet_list) - 1) * x)][1].get()
                x = x + 1
            p = p + 1
            x = 0
        return self.diagram