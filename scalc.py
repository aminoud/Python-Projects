import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator by aminoud")

        # Create display widget
        self.display = tk.Entry(master, width=25, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)

        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)

        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)

        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("DELETE", 4, 2)
        self.create_button("+", 4, 3)

        self.create_button_equal("=", 5, 0, columnspan=4)

    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, height=2, width=5, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=2, pady=2)

    def create_button_equal(self, text, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, height=2, width=35, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=2, pady=2)

    def button_click(self, text):
        if text == "DELETE":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "ERROR")
        else:
            self.display.insert(tk.END, text)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
