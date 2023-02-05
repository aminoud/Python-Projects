import tkinter as tka
from tkinter import messagebox as messagebox
from tkinter import filedialog

root = tka.Tk()
root.title('Simple Text Editor')

# Create text area
text_area = tka.Text(root)
text_area.pack(side='left', fill='both', expand=True)

# create the scrollbar
scrollbar = tka.Scrollbar(root, orient='vertical', command=text_area.yview)
scrollbar.pack(side='right', fill='y')

# set the scrollbar to the text area
text_area.config(yscrollcommand=scrollbar.set)

# create the functions
def open_text():
    filename = filedialog.askopenfilename()
    global doc
    doc = str(filename)
    root.title(doc)
    if filename:
        with open(filename, 'r') as f:
            text_area.delete("1.0","end")
            text_area.insert('1.0', f.read())

def save_text():
    if doc != "":
        text_data = text_area.get("1.0", tka.END)
        with open(doc, "w") as f:
            f.write(text_data)
    else:
        print(doc)
        messagebox.showinfo(title="Error!", message="No file is open to save, please chose save_as to create a new text file.")

def save_text_as():
    filename = filedialog.asksaveasfilename()
    root.title(filename)
    if filename:
        text = text_area.get('1.0', 'end-1c')
        with open(filename, 'w') as f:
            f.write(text)

# define the function for the About menu
def show_about():
    messagebox.showinfo(title="About", message="Developped by aminoud V0.1")

# create the menu bar
menuBar = tka.Menu(root)

# create the File menu
fileMenu = tka.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open", command=open_text)
fileMenu.add_command(label="Save", command=save_text)
fileMenu.add_command(label="Save As", command=save_text_as)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)

# add the File menu to the menu bar
menuBar.add_cascade(label="File", menu=fileMenu)

# create the About menu
aboutMenu = tka.Menu(menuBar, tearoff=0)
aboutMenu.add_command(label="About", command=show_about)

# add the About menu to the menu bar
menuBar.add_cascade(label="Help", menu=aboutMenu)

# display the menu bar
root.config(menu=menuBar)

root.mainloop()
