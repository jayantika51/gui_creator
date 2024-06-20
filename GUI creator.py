from tkinter import*
from tkinter import ttk
from tkinter.messagebox import showinfo


elements = ["Label", "Button", "Dropdown"]


root = tk.Tk()
root.title("Create Elements")
root.geometry("400x300")


element_selector = ttk.Combobox(root, state="readonly", values=elements)
element_selector.pack(pady=10)


class CreateElements:
    def __init__(self):
        print("This is CreateElements class")

    def createLabel(self):
        label = tk.Label(root, text="A new label has been created using class", fg="blue")
        label.pack(pady=5)

    def createButton(self):
        button = tk.Button(root, text="Button", command=self.message)
        button.pack(padx=10, pady=10)

    def createDropdown(self):
        values = [1, 2, 3]
        dropdown = ttk.Combobox(root, state="readonly", values=values)
        dropdown.pack(pady=5)

    def choose(self):
        global element_selector
        element = element_selector.get()
        if element == "Label":
            self.createLabel()
        elif element == "Button":
            self.createButton()
        elif element == "Dropdown":
            self.createDropdown()

    def message(self):
        showinfo("Message", "You clicked the button created using class")


creator = CreateElements()


create_button = tk.Button(root, text="Create Element", command=creator.choose)
create_button.pack(padx=10, pady=20)


root.mainloop()
