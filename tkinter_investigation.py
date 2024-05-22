import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("800x600")

label = tk.Label(root, text="Hello World")
label.pack()

listbox = tk.Listbox(root)

team = ["Alice", "Bob", "Carol", "Dan", "Eve"]

for name in team:
    listbox.insert(tk.END, name)

listbox.place(x=10, y=10)

def list_box_select(event):
    print(event)
    selected_index = listbox.curselection()
    selected_name = listbox.get(selected_index)

    messagebox.showinfo("Select", f"you selected { selected_name }")

listbox.bind("<<ListboxSelect>>", list_box_select)

#listbox.pack()

def test_button_click():
    messagebox.showinfo("Click", "You clicked")


test_button = tk.Button(root, text="Press Me", command=test_button_click)
test_button.place(x=10, y=200)


file_listbox = tk.Listbox(root)


file_listbox.place(x = 10, y=300)

files = os.listdir()

for file in files:
    file_listbox.insert(tk.END, file)


def file_select(event):

    selected_index = file_listbox.curselection()
    if selected_index:
        selected_file = file_listbox.get(selected_index[0])

        with open(selected_file, "r") as fp:
            file_contents = fp.read()

        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, file_contents)


file_listbox.bind("<<ListboxSelect>>", file_select)

text_widget = tk.Text(root, wrap=tk.WORD)
text_widget.place(x=250, y=10, width=500, height=500)

root.mainloop()


