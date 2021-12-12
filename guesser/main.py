# TODO: Refactor this shit

from tkinter import Button, Entry, StringVar, Tk, Menu, Toplevel, Label, Frame, Widget
from tkinter.messagebox import showinfo
import random

LABEL_COLOR = "#ffffff"
DARK = "#323232"
OFF_WHITE = "#3b3b3b"

SMALL_FONT_STYLE = ("Arial", 15)
HEADING_FONT_STYLE = ("Arial", 20, "bold")
LARGE_FONT_STYLE = ("Arial", 30, "bold", "underline")


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x600")
        self.window.resizable(0, 0)
        self.window["bg"] = DARK
        self.window.title("Zgadnij liczbę")
        menu = self.create_menu()
        self.window.config(menu=menu)

        self.number = StringVar(self.window, "")
        self.guess = StringVar(self.window, "")
        self.info = StringVar(self.window, "")
        self.left_bound = StringVar(self.window, 0)
        self.right_bound = StringVar(self.window, 99)
        self.generate_number()

        header_frame = self.create_header_frame()
        header_frame.grid(row=0, column=0, sticky="nsew")

        info_frame = self.create_info_frame()
        info_frame.grid(row=1, column=0, sticky="nsew")

        main_frame = self.create_main_frame()
        main_frame.grid(row=2, column=0)

        result_frame = self.create_result_frame()
        result_frame.grid(row=3, column=0, sticky="nsew")

        footer_frame = self.create_footer_frame()
        footer_frame.grid(row=4, column=0, sticky="w")


        self.window.columnconfigure(0, weight=1)
        for i in range(0, 4):
            self.window.rowconfigure(i, weight=1)

    def create_menu(self):
        menubar = Menu(self.window)
        program_menu = Menu(menubar, tearoff=0)
        program_menu.add_command(
            label="Zmień liczbę początku przedziału", command=self.update_left_bound)
        program_menu.add_command(
            label="Zmień liczbę końca przedziału", command=self.update_right_bound)
        program_menu.add_separator()
        program_menu.add_command(
            label="Exit", command=self.window.quit)
        menubar.add_cascade(label="Program", menu=program_menu)
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="O programie", command=self.about_program)
        help_menu.add_command(label="o Autorze", command=self.about_author)
        menubar.add_cascade(label="Pomoc", menu=help_menu)
        return menubar

    def create_header_frame(self):
        frame = Frame(self.window)
        label = Label(frame, text="ZGADNIJ LICZBĘ",
                             font=LARGE_FONT_STYLE, fg=LABEL_COLOR, bg=DARK)
        label.pack(expand=True,fill="both")
        return frame

    def create_info_frame(self):
        frame = Frame(self.window)
        label = Label(frame, text="Serdecznie witamy!",
                            bg=DARK, font=HEADING_FONT_STYLE, fg=LABEL_COLOR)
        label.pack(expand=True,fill="both")

        paragraph = Label(
            frame, wraplength=400, text="Aby rozpocząć grę,\n wpisz liczbę całkowitą z przedziału od 0 do 99, która Twoim zdaniem została wylosowana:", bg=DARK, font=SMALL_FONT_STYLE, fg=LABEL_COLOR)
        paragraph.pack(expand=True,fill="both")

        return frame


    def create_main_frame(self):
        frame = Frame(self.window, bg=DARK)
        entry = Entry(frame, textvariable=self.guess)
        entry.grid(row=0,column=0, sticky="nsew", padx=(0, 30))
        button = Button(frame, text="Podaj liczbę", command=self.check_input)
        button.grid(row=0,column=1, sticky="nsew")
        return frame

    def create_result_frame(self):
        frame = Frame(self.window)
        label = Label(frame, textvariable=self.info, bg=DARK, font=SMALL_FONT_STYLE, fg=LABEL_COLOR)
        label.pack(expand=True, fill="both")
        return frame

    def create_footer_frame(self):
        frame = Frame(self.window, bg=DARK)
        label = Label(frame, text="Naciśnij, aby opuścić program", font=HEADING_FONT_STYLE, fg=LABEL_COLOR, bg=DARK)
        label.grid(row=0, column=0, sticky="w")
        button  =Button(frame, text="Wyjście", command=self.window.quit)
        button.grid(row=0, column=1, sticky="w")
        return frame

    def update_left_bound(self):
        master = Toplevel(self.window)
        master.title("Podaj liczbę a")
        master.resizable(0, 0)
        label = Label(
            master, text="Podaj liczbę początku przedziału losowania")
        label.grid(row=0, column=0, sticky="nsew")
        entry = Entry(master)
        entry.grid(row=1, column=0)
        button = Button(master, text="OK",
                        command=lambda: [self.left_bound.set(entry.get()), master.destroy()])
        button.grid(row=1, column=1, sticky="nsew")
        self.generate_number()
        for i in range(0, 2):
            master.rowconfigure(i, weight=1)
            master.columnconfigure(i, weight=1)

    def update_right_bound(self):
        master = Toplevel(self.window)
        master.title("Podaj liczbę b")
        master.resizable(0, 0)
        label = Label(master, text="Podaj liczbę końca przedziału losowania")
        label.grid(row=0, column=0, sticky="nsew")
        entry = Entry(master)
        entry.grid(row=1, column=0)
        button = Button(master, text="OK",
                        command=lambda: [self.right_bound.set(entry.get()), master.destroy()])
        button.grid(row=1, column=1, sticky="nsew")
        self.generate_number()
        for i in range(0, 2):
            master.rowconfigure(i, weight=1)
            master.columnconfigure(i, weight=1)        

    def generate_number(self):
        self.number.set(random.randint(int(self.left_bound.get()), int(self.right_bound.get())))

    def check_input(self):
        if self.guess.get()==self.number.get():
            self.info.set("Brawo wygrałeś")
            self.generate_number()
        elif int(self.guess.get())>int(self.number.get()):
            self.info.set("Twoja liczba jest zbyt duża")
        else:
            self.info.set("Twoja liczba jest zbyt mała")
    
    def about_program(self):
        showinfo("O Programie", "Gra: Zgadnij Liczbę")

    def about_author(self):
        showinfo("O Autorze", "Autor: Marcin Brzozowski")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
