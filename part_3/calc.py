from tkinter import Button, Frame, Tk, Label, StringVar
import re

WHITE = "#ffffff"
LIGHT_GRAY = "#4b4e52"
LABEL_COLOR = "#000000"
DARK = "#323232"
OFF_WHITE = "#3b3b3b"
LIGHT_BLUE = "#4cc2ff"

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

DIGITS = {
    "7": (1, 1), "8": (1, 2), "9": (1, 3),
    "4": (2, 1), "5": (2, 2), "6": (2, 3),
    "1": (3, 1), "2": (3, 2), "3": (3, 3),
    "0": (4, 2), ".": (4, 1)
}

OPERATORS = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}


class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x600")
        self.window.resizable(0, 0)
        self.window.title("Kalkulator")

        self.total_exp = StringVar(self.window,  "")
        self.curr_exp = StringVar(self.window, "0")

        self.display_frame = self.create_display_frame()

        self.total_label, self.current_label = self.create_display_labels()


        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def create_buttons_frame(self):
        frame = Frame(self.window)
        frame.pack(side="bottom", expand=True, fill="both")
        return frame

    def create_digit_buttons(self):
        for digit, grid_value in DIGITS.items():
            button = Button(self.buttons_frame, text=str(digit), command=lambda x=digit: self.add_to_expression(
                x), bg=OFF_WHITE, fg=WHITE, font=DIGITS_FONT_STYLE)
            button.grid(row=grid_value[0], column=grid_value[1], sticky="nsew")

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in OPERATORS.items():
            button = Button(self.buttons_frame, text=symbol, command=lambda o=operator: self.append_operator(
                o), bg=DARK, fg=WHITE, font=DEFAULT_FONT_STYLE)
            button.grid(row=i, column=4, sticky="nsew")
            i += 1

    def create_equals_button(self):
        button = Button(self.buttons_frame, text="=", bg=LIGHT_BLUE,
                        fg="#000000", font=DEFAULT_FONT_STYLE, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky="nsew")

    def create_clear_button(self):
        button = Button(self.buttons_frame, text="C", bg=LIGHT_BLUE,
                        fg=WHITE, font=DEFAULT_FONT_STYLE, command=self.clear)
        button.grid(row=0, column=1, columnspan=3, sticky="nsew")

    def create_special_buttons(self):
        self.create_equals_button()
        self.create_clear_button()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        self.window.bind("<BackSpace>", lambda event: self.delete())
        for key in DIGITS:
            self.window.bind(str(key), lambda event,
                             digit=key: self.add_to_expression(digit))

        for key in OPERATORS:
            self.window.bind(key, lambda event,
                             operator=key: self.append_operator(operator))

    def create_display_frame(self):
        frame = Frame(self.window)
        frame.pack(side="top", expand=False, fill="both")
        return frame

    def create_display_labels(self):
        total_label = Label(self.window, textvariable=self.total_exp,
                            anchor="e", fg=LIGHT_GRAY, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        current_label = Label(self.window, textvariable=self.curr_exp,
                              anchor="e", fg=LABEL_COLOR, font=LARGE_FONT_STYLE)
        current_label.pack(expand=True, fill="both")

        return total_label, current_label

    def add_to_expression(self, value):

        if len(self.curr_exp.get()+value) > 9:
            return

        self.curr_exp.set(self.curr_exp.get()+value)
        if re.search("^(0[0-9])", self.curr_exp.get()):
            self.curr_exp.set(self.curr_exp.get()[1:])
        if re.search("([0-9]\.\.)", self.curr_exp.get()):
            self.delete()
        if self.curr_exp.get().count(".") > 1:
            self.delete()

    def append_operator(self, operator):
        self.curr_exp.set(self.curr_exp.get()+operator)
        self.total_exp.set(self.total_exp.get()+self.curr_exp.get())
        self.curr_exp.set("")

    def delete(self):
        self.curr_exp.set(self.curr_exp.get()[:-1])

    def clear(self):
        self.total_exp.set("")
        self.curr_exp.set("")

    def evaluate(self):
        self.curr_exp.set(eval(self.total_exp.get()+self.curr_exp.get()))

        if re.search("(\.0)$", self.curr_exp.get()):
            self.delete()

        self.total_exp.set("")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = Calculator()
    app.run()
