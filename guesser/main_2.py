from tkinter import StringVar, Tk,Menu,Toplevel
from tkinter.messagebox import showinfo
from tkinter.ttk import Button, Entry,  Label, Frame, Style
import random

DARK = "#323232"
LIGHT = "#ffffff"

class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("500x600")
        self.window.title("Zgadnij liczbę")
        self.window.configure(background="#323232")

        style = Style(self.window)
        style.configure("TFrame", background = DARK)
        style.configure("main_heading.TLabel", font=("Arial", 30, "bold", "underline"), foreground=LIGHT, background=DARK)
        style.configure("sub_heading.TLabel", font=("Arial", 20, "bold"), foreground=LIGHT, background=DARK)
        style.configure("normal.TLabel", font=("Arial", 15, "bold"), foreground=LIGHT, background=DARK)
        
        self.number = StringVar(self.window, "")
        self.guess = StringVar(self.window, "")
        self.info = StringVar(self.window, "")
        self.left_bound = StringVar(self.window, 0)
        self.right_bound = StringVar(self.window, 99)
        self.generate_number()
        
        self.build()


    def build(self):
        menu = self.create_menu()
        self.window.config(menu=menu)
        
        game_name = Label(self.window, text="ZGADNIJ LICZBĘ", style="main_heading.TLabel")
        game_name.pack(anchor="center", pady=(30,30))
                
        heading = Label(self.window, text="Serdecznie witamy!", style="sub_heading.TLabel")
        heading.pack()
        
        p_text = "Aby rozpocząć grę,\n wpisz liczbą całkowitą z przedziału od 0 do 99, która Twoim zdaniem została wylosowana: "
        paragraph = Label(self.window, text=p_text, wraplength=400, style="normal.TLabel", anchor="center")
        paragraph.pack(pady=(30, 20))
        
        box = Frame(self.window)
        box.pack()
        
        entry = Entry(box, textvariable=self.guess)
        entry.grid(row=0, column=0, padx=(0, 30))
        
        check_button = Button(box, text="Podaj liczbę", command=self.check_input)
        check_button.grid(row=0, column=1)
        
        game_info = Label(self.window, textvariable=self.info, style="normal.TLabel")
        game_info.pack(pady=(30,0))
        
        footer = Frame(self.window)
        footer.pack(side="bottom")
        
        quit_label = Label(footer, text="Naciśnij, aby opuścić program", style="sub_heading.TLabel")
        quit_label.grid(row=0, column=0, padx=(0, 30))

        quit_button = Button(footer, text="Wyjście", command=self.window.quit)
        quit_button.grid(row=0, column=1)
            

    def create_menu(self):
        menubar = Menu(self.window)
        
        program_menu = Menu(menubar)
        help_menu = Menu(menubar)
        
        program_menu.add_command(label="Zmień liczbę początku przedziału", command=self.update_left_bound)
        program_menu.add_command(label="Zmień liczbę końca przedziału", command=self.update_right_bound)
        program_menu.add_separator()
        program_menu.add_command(label="Exit", command=self.window.quit)
        
        help_menu.add_command(label="O programie", command=lambda: showinfo("O Programie", "Gra: Zgadnij Liczbę"))
        help_menu.add_command(label="o Autorze", command=lambda: showinfo("O Autorze", "Autor: Marcin Brzozowski"))
        
        menubar.add_cascade(label="Program", menu=program_menu)
        menubar.add_cascade(label="Pomoc", menu=help_menu)
        
        self.window.config(menu=menubar)

    def update_left_bound(self):
        master = Toplevel(self.window)
        master.title("Podaj liczbę a")
        
        label = Label(master, text="Podaj liczbę początku przedziału losowania")
        label.grid(row=0, column=0, sticky="nsew")
        
        entry = Entry(master)
        entry.grid(row=1, column=0)
        
        button = Button(master, text="OK", command=lambda: [self.left_bound.set(entry.get()), master.destroy()])
        button.grid(row=1, column=1, sticky="nsew")
        
        self.generate_number()
        
        for i in range(0, 2):
            master.rowconfigure(i, weight=1)
            master.columnconfigure(i, weight=1)

    def update_right_bound(self):
        master = Toplevel(self.window)
        master.title("Podaj liczbę b")

        label = Label(master, text="Podaj liczbę końca przedziału losowania")
        label.grid(row=0, column=0, sticky="nsew")

        entry = Entry(master)
        entry.grid(row=1, column=0)

        button = Button(master, text="OK", command=lambda: [self.right_bound.set(entry.get()), master.destroy()])
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


    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
