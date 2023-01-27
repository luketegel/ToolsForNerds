import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("printing for dummies")

        self.pack(fill=tk.BOTH, expand=1)

        quitButton = tk.Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=0, y=0)

        self.textbox = tk.Entry(self)
        self.textbox.place(x=0, y=20)

        self.button = tk.Button(self, text="Print", command=self.print_text)
        self.button.place(x=0, y=40)

    def client_exit(self):
        exit()

    def print_text(self):
        print(self.textbox.get())

root = tk.Tk()
root.geometry("400x300")
app = Window(root)


root.mainloop()
