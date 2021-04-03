from tkinter import *
from PIL import ImageTk, Image


class CheckBox(Checkbutton):
    boxes = []

    def __init__(self, master=None, **options):
        Checkbutton.__init__(self, master, options)
        self.boxes.append(self)
        self.var = BooleanVar()
        self.text = self.cget('text')
        self.configure(variable=self.var)


ui_green = "#1ED760"
ui_black = "#191414"
ui_white = "#FFFFFF"


def return_value():
    return


def close_window(window):
    window.destroy()


def main_page():
    root = Tk()
    root.title('Spot-on-ify')
    root.configure(bg=ui_black)
    root.resizable(height=None, width=None)
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)

    # title and team name
    title = Label(root, text="Spot-on-ify", font=("MS Sans Serif", 30), fg=ui_green, bg=ui_black)
    line_break1 = Label(root, text=" ", bg=ui_black)

    my_img = ImageTk.PhotoImage(Image.open("Logo.png").resize((round(100), round(100))))
    image = Label(image=my_img, borderwidth=0, highlightthickness=0, pady=20)
    root.geometry('700x500')

    # button
    login = "Login with Spotify"
    button = Button(root, text=login, font=("MS Sans Serif", 10), command=lambda: close_window(root),
                    activebackground=ui_black, bg=ui_green, fg=ui_white)

    title.pack(pady=20)
    image.pack(side=TOP)
    line_break1.pack(pady=20)
    button.pack()
    root.mainloop()


def checked_boxes() -> list:
    selected = []
    for box in CheckBox.boxes:
        if box.var.get():
            selected.append(box.text)
    return selected


def show_checkboxes(track_dict):
    root = Tk()
    root.title("Spot-on-ify")
    root.resizable(height=None, width=None)
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)

    text = Label(root, text="These are the last few songs you played on Spotify.", font=("MS Sans Serif", 12))
    text1 = Label(root, text="Select upto 5 tracks that you would like to use as seeds.", font=("MS Sans Serif", 10))
    text.pack(pady=6)
    text1.pack(pady=20)

    for track in track_dict:
        box = CheckBox(text=track, command=track_dict[track])
        box.pack()

    button = Button(root, text="SELECT", command=lambda: close_window(root), width=10, fg=ui_green, bg=ui_black)
    button.pack(pady=50)
    root.mainloop()


def show_recommendations(recommendations_list):
    root = Tk()
    root.title('Spot-on-ify')
    icon = PhotoImage(file="icon.png")
    root.iconphoto(False, icon)

    root.resizable(height=None, width=None)

    text = Label(root, text="Here are the recommended tracks which will be included in your new playlist:",
                 font=("MS Sans Serif", 12), justify=CENTER)
    text.pack(pady=2, padx=5)
    text = Label(root, text="Check out your Spotify App to find your playlist!",
                 font=("MS Sans Serif", 9), height="2")
    text.pack(pady=5, padx=5)

    listbox = Listbox(root)
    listbox.pack(fill=BOTH)
    scrollbar = Scrollbar(root)
    scrollbar.pack(fill=BOTH)

    for track in recommendations_list:
        listbox.insert(END, track)

    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.xview)

    root.mainloop()
