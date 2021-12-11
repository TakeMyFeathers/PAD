from tkinter import Tk, Button, CENTER

DEFAULT_FONT = ("Arial", 20, "bold")
DARK = "#323232"
WHITE = "#ffffff"
LIGHT_BLUE = "#4cc2ff"
HOVER_COLOR = "#bf2000"


class ButtonWithHover(Button):
    def __init__(self, hover_color=HOVER_COLOR, **kw):
        self.hover_color=hover_color
        super().__init__(**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.hover_on)
        self.bind("<Leave>", self.hover_out)

    def hover_on(self, e):
        self.config(activebackground=self.hover_color)

    def hover_out(self, e):
        self.config(activebackground=self.defaultBackground)


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x500")
        self.window.config(bg=DARK)
        self.window.resizable(0, 0)
        self.window.title("App")
        button = ButtonWithHover(master=self.window, text="Hover on me", bg=LIGHT_BLUE, fg=WHITE, font=DEFAULT_FONT)
        button.place(relx=.5, rely=.5, anchor=CENTER)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
