import customtkinter
import tkinter as tk
import random 
from tkinter import filedialog

mode = "dark"

customtkinter.set_appearance_mode(mode)  # Modes: system (default), light, dark
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
    text_color='grey',
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

def openNewWindow():
     
    newWindow = customtkinter.CTkToplevel()
    newWindow.title("Random Generator")
    newWindow.geometry("400x400")
    newWindow._set_appearance_mode(mode)

def switch_event():
    if switch_var.get() == 'on':
        customtkinter.set_appearance_mode('dark') 
        mode = 'dark'
    if switch_var.get() == 'off':
        customtkinter.set_appearance_mode('light') 
        mode = 'light'
        
randombutton = customtkinter.CTkButton(
    master=app, 
    text='Random Generator', 
    command=openNewWindow,
    height=50,
    fg_color="#4a4949",
    corner_radius=17,
    font= ("",17))
randombutton.pack(fill='both')

switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(
    app,
    text="Dark mode",
    command=switch_event,
    variable=switch_var, 
    onvalue="on", 
    offvalue="off",
    fg_color="#4a4949",
    corner_radius=17,
    font= ("",17)
)
switch.pack(side='bottom')

buttonclose = customtkinter.CTkButton(
    master=app, 
    text='Beenden...', 
    command=stop,
    height=50,
    fg_color="#4a4949",
    corner_radius=17,
    font= ("",17)
    )
buttonclose.pack(fill='both', side='bottom')

app.mainloop()