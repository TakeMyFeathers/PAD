# TODO: Refactor this shit

from tkinter import Button, Label, StringVar, Tk, Frame


LABEL_COLOR = "#ffffff"
DARK = "#323232"
OFF_WHITE = "#3b3b3b"

DEFAULT_FONT_STYLE = ("Arial", 20)

CIRCLE = "\u20DD"
CROSS = "\u00D7"


class App:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x500")
        self.round = 0
        self.window.resizable(0, 0)
        self.window.title("TicTacToe")

        self.buttons_frame = self.create_buttons_frame()
        self.buttons = self.create_buttons()

        self.info_frame = self.create_info_frame()
        self.info = StringVar(self.info_frame, f"Teraz ruch ma {CIRCLE}")
        self.create_info_label()
        for i in range(0, 3):
            self.buttons_frame.rowconfigure(i, weight=1)
            self.buttons_frame.columnconfigure(i, weight=1)

    def create_buttons_frame(self):
        frame = Frame(self.window, bg=DARK)
        frame.pack(expand=True, fill="both")
        return frame

    def create_info_frame(self):
        frame = Frame(self.window, bg=DARK)
        frame.pack(fill="both")
        return frame

    def create_info_label(self):
        label = Label(self.info_frame, fg=LABEL_COLOR,
                      font=DEFAULT_FONT_STYLE, textvariable=self.info, bg=DARK)
        label.pack(expand=True, fill="both")

    def move(self, button):
        if self.round % 2 == 0:
            button["text"] = CIRCLE
            self.info.set(f"Teraz ruch ma {CROSS}")
        else:
            button["text"] = CROSS
            self.info.set(f"Teraz ruch ma {CIRCLE}")

        if self.check_if_won(CIRCLE):
            self.disable_all()
            self.info.set(f"Wygrał {CIRCLE}")
        if self.check_if_won(CROSS):
            self.disable_all()
            self.info.set(f"Wygrał {CROSS}")

        button["state"] = "disabled"
        self.round += 1

    def create_buttons(self):
        buttons = []
        for y in range(0, 3):
            for x in range(0, 3):
                button = Button(
                    self.buttons_frame, font=DEFAULT_FONT_STYLE, fg=LABEL_COLOR, bg=OFF_WHITE, disabledforeground=LABEL_COLOR)
                button["command"] = lambda button=button: self.move(button)
                buttons.append(button)
                button.grid(row=x, column=y, sticky="nsew")
        return buttons   

    def disable_all(self):
        for b in self.buttons:
            b["state"]="disabled"

    def check_if_won(self, symbol):
        counter = 0
        for i in range(0, 3):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;
        
        if counter==3:
            return True

        for i in range(3, 6):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;

        if counter==3:
            return True

        for i in range(6, 9):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;

        for i in range(0, 7, 3):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;            

        if counter==3:
            return True

        for i in range(1, 8, 3):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;     
        
        if counter==3:
            return True

        for i in range(2, 9, 3):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;            

        if counter==3:
            return True

        for i in range(0, 9, 4):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;            

        if counter==3:
            return True

        for i in range(2, 7, 2):
            if self.buttons[i]["text"]==symbol:
                counter+=1
            else:
                counter=0
                break;            

        if counter==3:
            return True

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
