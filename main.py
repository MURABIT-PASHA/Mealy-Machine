from tkinter import *
from tkinter import ttk

from diagram import DiagramImage

window = Tk()
window.geometry("750x450")
window.config(padx=15, pady=15)
window.title("Mealy Machine")

frame1 = Frame(master=window, highlightthickness=2, highlightbackground="blue")
frame1.pack(anchor=NW)

alphabet_label = Label(master=frame1, text="Alfabe giriniz: ")
alphabet_label.grid(row=0, column=0, padx=15, pady=15, sticky=W)

alphabet_entry = Entry(master=frame1, highlightthickness=2, highlightbackground="blue")
alphabet_entry.grid(row=0, column=1, padx=15, pady=15)

state_label = Label(master=frame1, text="Durum sayısını giriniz: ")
state_label.grid(row=1, column=0, padx=15, pady=15, sticky=W)

state_entry = Entry(master=frame1, highlightthickness=2, highlightbackground="blue")
state_entry.grid(row=1, column=1)


def create_scheme(alphabet, state_number):
    alphabet = alphabet.replace(" ", "")
    alphabet_list = alphabet.split(",")
    alphabet_char = 0
    column_amount = len(alphabet_list) * 2 + 1
    row_amount = int(state_number) + 2
    state_list = []
    index = 0
    diagram = {}
    for _ in range(len(alphabet_list)):
        diagram[f"{alphabet_list[_]}"] = {}
        for y in range(int(state_number)):
            diagram[f"{alphabet_list[_]}"][f"q{y}"] = {}
    for _ in range(int(state_number)):
        state_list.append(f"q{_}")

    frame2 = Frame(master=window, highlightthickness=2, highlightbackground="blue")
    frame2.pack(anchor=NW)
    body_list = []
    for i in range(row_amount):
        for j in range(column_amount):
            if i == 0:
                if j % 2 == 0:
                    alphabet_char = alphabet_char + 1
                    continue
                else:
                    new_title = Label(master=frame2, text=f"After input {alphabet_list[j - alphabet_char]}")
                    new_title.grid(row=i, column=j, columnspan=2)
            elif i == 1:
                if j == 0:
                    new_title = Label(master=frame2, text="Old State")
                    new_title.grid(row=i, column=j)
                elif j % 2 == 0:
                    new_title = Label(master=frame2, text="Output")
                    new_title.grid(row=i, column=j)
                else:
                    new_title = Label(master=frame2, text="New State")
                    new_title.grid(row=i, column=j)
            else:
                if j == 0:
                    new_title = Label(master=frame2, text=f"q{i - 2}")
                    new_title.grid(row=i, column=j)
                elif j % 2 == 0:
                    new_value = Entry(master=frame2, highlightthickness=1)
                    new_value.grid(row=i, column=j)
                    body_list.append([new_value, index])
                    index = index + 1
                else:
                    state = ttk.Combobox(master=frame2, values=state_list)
                    state.grid(row=i, column=j)
                    body_list.append([state, index])
    values = set(map(lambda x: x[1], body_list))
    group_list = [[y[0] for y in body_list if y[1] == x] for x in values]
    print(group_list)

    def create_table():
        x = 0
        p = 0
        for w in diagram:
            for z in range(len(state_list)):
                diagram[w][f"q{z}"]["new_state"] = group_list[p + z + ((len(alphabet_list) - 1) * x)][0].get()
                diagram[w][f"q{z}"]["output"] = group_list[p + z + ((len(alphabet_list) - 1) * x)][1].get()
                x = x + 1
            p = p + 1
            x = 0
        print(diagram)

        def convert():
            string = input_string.get()
            old_state = "q0"
            states = []
            outputs = []
            for _ in string:
                new_state = diagram[_][old_state]["new_state"]
                output = diagram[_][old_state]["output"]
                outputs.append(output)
                states.append(new_state)
                new_state_label = Label(master=state_frame, text=f"Eski Durum: {old_state}, Yeni Durum: {new_state}, "
                                                                 f"Çıktı: {output}")
                new_state_label.pack()
                old_state = new_state
            output_label.config(text="".join(outputs))
            states_label.config(text="".join(states))
            diagram_image = DiagramImage(diagram, int(state_number))

        # Açılır pencere
        new_window = Toplevel(window)
        new_window.config(height=200, width=400)

        input_string = Entry(master=new_window)
        input_string.pack()

        convert_button = Button(master=new_window, text="Göster", command=convert)
        convert_button.pack()

        output_label = Label(master=new_window, text="")
        output_label.pack()

        states_label = Label(master=new_window, text="")
        states_label.pack()

        state_frame = Frame(master=new_window, highlightthickness=1, highlightbackground="blue", height=200,
                            width=400)
        state_frame.pack()

    table_button = Button(master=frame2, text="Tabloyu oluştur", command=create_table)
    table_button.grid(column=column_amount, row=row_amount)


scheme_button = Button(master=frame1, text="Şema oluştur",
                       command=lambda: create_scheme(alphabet_entry.get(), state_entry.get()))
scheme_button.grid(row=2, column=1, padx=15, pady=15, sticky=E)

window.mainloop()
