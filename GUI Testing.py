import tkinter as tk

def msg():
    get_name = name.get()
    if get_name == "areesha":
        print("Dfa ho")
    elif get_name == "shahzeb":
        print("You are genius!")

app = tk.Tk()
app.title("Tell Your Name")

app_frame = tk.Frame(app)
app_frame.pack()

title = tk.Label(app_frame, text="Enter Your Name")
title.configure(padx=30, pady=30)
title.grid()

name = tk.Entry(app_frame)
name.grid()
name.bind("<Enter>", msg())
btn = tk.Button(app_frame, text="Submit", command=msg)
btn.grid(sticky="news")





app.mainloop()