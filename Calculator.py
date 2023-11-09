import customtkinter
import tkinter as tk
from tkinter import filedialog


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title('Calculator')

label =""

def stop():
    app.quit()

def button_function():
    global entry
    global label
    global loesung
    global entry1
    entry1 = entry.get()
    try:
        try:
            label.destroy()
        except:
            print('nichts zum löschen')
        loesung = eval(entry1)
        label = customtkinter.CTkLabel(
            app, 
            text=f"Lösung: {loesung}",
            height=50,
            corner_radius=17,
            text_color='white',
            fg_color='#787575',
            font= ("",17)
        )
        label.pack(fill='both')
        app.mainloop
    except:
        print('schiefgelaufen')

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Cakow\\PycharmProjects\\Main",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    rechnung = (str(entry1))
    loesung1 = (str(loesung))
    file.write(f'{entry1} = {loesung1}')
    file.close()



entry = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Rechnung eingeben:",
    height=50,
    text_color='white',
    placeholder_text_color='#b8b4b4',
    corner_radius=17,
    font= ("",17)
)
entry.pack(fill='both')

button = customtkinter.CTkButton(
    master=app, 
    text="Rechnung lösen", 
    command=button_function,
    height=50,
    fg_color="#4a4949",
    corner_radius=17,
    font= ("",17)
)
button.pack(fill='both')

button = customtkinter.CTkButton(
    app,
    text='Speichere deine Lösung',
    command=saveFile,
    height=50,
    fg_color="#4a4949",
    corner_radius=17,
    font= ("",17)
    )
button.pack(fill='both')

buttonclose = customtkinter.CTkButton(
    master=app, 
    text='Beenden...', 
    command=stop,
    height=50,
    fg_color="#4a4949",
    corner_radius=17,
    font= ("",17)
    )
buttonclose.pack(fill='both')

app.mainloop()
