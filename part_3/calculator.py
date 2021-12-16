# TODO: Rafactor this shit

from tkinter import Tk, StringVar
from tkinter.ttk import Button, Frame, Label, Style
import math
import re

DIGITS = {
    "7": (2, 0), "8": (2, 1), "9": (2, 2),
    "4": (3, 0), "5": (3, 1), "6": (3, 2),
    "1": (4, 0), "2": (4, 1), "3": (4, 2),
    "0": (5, 1), ".": (5, 2)
}

OPERATORS = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

    
class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x600")
        self.window.minsize(300, 500)
        self.window.title("Kalkulator")

        self.total_exp = StringVar(self.window,  "")
        self.curr_exp = StringVar(self.window, "0")
        
        self.build()
        self.bind_keys()
        style = Style(self.window)
        style.configure("Digit.TButton", font=("Arial", 20, "bold"), foreground="#ffffff", background="#3b3b3b")
        style.configure("Operator.TButton", font=("Arial", 20), foreground="#ffffff", background="#323232")
        style.configure("Main.TLabel", foreground="#000000", font=("Arial", 40, "bold"))
        style.configure("Preview.TLabel", foreground="#4b4e52", font=("Arial", 16))

    def build(self):
        display_frame = Frame(self.window)
        display_frame.pack(side="top", expand=False, fill="both")
        
        total_label = Label(display_frame, textvariable=self.total_exp, anchor="e", style="Preview.TLabel")
        total_label.pack(expand=True, fill="both")

        current_label = Label(display_frame, textvariable=self.curr_exp, anchor="e", style="Main.TLabel")
        current_label.pack(expand=True, fill="both")
        
        buttons_frame = Frame(self.window)
        buttons_frame.pack(expand=True, fill="both")
        
        for digit, grid_value in DIGITS.items():
            button = Button(buttons_frame, text=str(digit), command=lambda x=digit: self.add_to_expression(x), style="Digit.TButton")
            button.grid(row=grid_value[0], column=grid_value[1], sticky="nsew")
            
        for i, (operator, symbol) in enumerate(OPERATORS.items()):
            button = Button(buttons_frame, text=symbol, command=lambda o=operator: self.append_operator(o), style="Operator.TButton")
            button.grid(row=i+1, column=3, sticky="nsew")
            
        sign_button = Button(buttons_frame, text="\u00B1", command=self.change_sign, style="Operator.TButton")
        sign_button.grid(row=5, column=0, sticky="nsew")
        
        abs_button = Button(buttons_frame, text="|x|", command=lambda: self.curr_exp.set(self.curr_exp.get().replace("-", "")),style="Operator.TButton")
        abs_button.grid(row=1, column=0, sticky="nsew")        

        sqrt_button = Button(buttons_frame, text="\u221A", command=lambda: self.curr_exp.set(round(math.sqrt(int(self.curr_exp.get())), 3)),style="Operator.TButton")
        sqrt_button.grid(row=1, column=1, sticky="nsew")

        mod_button = Button(buttons_frame, text="mod", command=lambda: self.append_operator(" %"),style="Operator.TButton")
        mod_button.grid(row=0, column=3, sticky="nsew")
        
        exp_button = Button(buttons_frame, text="x^y", command=lambda: self.append_operator("**"),style="Operator.TButton")
        exp_button.grid(row=1, column=2, sticky="nsew")

        equals_button = Button(buttons_frame, text="=", command=self.evaluate,style="Operator.TButton")
        equals_button.grid(row=5, column=3, sticky="nsew")

        clear_button = Button(buttons_frame, text="C", command=self.clear,style="Operator.TButton")
        clear_button.grid(row=0, column=0, columnspan=3, sticky="nsew")

        for x in range(0, 6):
            buttons_frame.rowconfigure(x, weight=1)
            
        for x in range(0, 4):
            buttons_frame.columnconfigure(x, weight=1)

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.delete())
        for key in DIGITS:
            self.window.bind(str(key), lambda event,
                             digit=key: self.add_to_expression(digit))

        for key in OPERATORS:
            self.window.bind(key, lambda event,
                             operator=key: self.append_operator(operator))

    def add_to_expression(self, value):
        exp = self.curr_exp.get()+value

        if len(exp) > 9:
            return
        if re.search("^(0[0-9])", exp):
            exp = exp[1:]
        if re.search("([0-9]\.\.)", exp):
            return
        if exp.count(".") > 1:
            return

        self.curr_exp.set(exp)

    def append_operator(self, operator):
        self.curr_exp.set(self.curr_exp.get()+operator)
        self.total_exp.set(self.total_exp.get()+self.curr_exp.get())
        self.curr_exp.set("")

    def delete(self):
        self.curr_exp.set(self.curr_exp.get()[:-1])

    def clear(self):
        self.total_exp.set("")
        self.curr_exp.set("0")

    def change_sign(self):
        if self.curr_exp.get().count("-") == 1:
            return
        self.curr_exp.set("-"+self.curr_exp.get())

    def evaluate(self):
        self.curr_exp.set(eval(self.total_exp.get()+self.curr_exp.get()))

        if re.search("(\.0)$", self.curr_exp.get()):
            self.delete()

        self.total_exp.set("")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
