import customtkinter
import tkinter as tk
import random 
from tkinter import filedialog

mode = "dark"

customtkinter.set_appearance_mode(mode)  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("700x400")
app.title('Calculator')

label =""
labelslider = ''

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
def getRandomZeichen(SWITCHPLUS, SWITCHMINUS, SWITCHGETEILT, SWITCHMAL):
    listezeichen = []

    if SWITCHPLUS == 'on':
        listezeichen.append('+')
    if SWITCHMINUS == 'on':
        listezeichen.append('-')
    if SWITCHGETEILT == 'on':
        listezeichen.append('/')
    if SWITCHMAL == 'on':
        listezeichen.append('*')
#    if listezeichen.count > 0:
    return random.choice(listezeichen)
#    else:
    print('Geht nicht......')
     

def berechnungrandom(entry1, entry2, scroolbar, SWITCHPLUS, SWITCHMINUS, SWITCHMAL, SWITCHGETEILT):
    Value1 = (int(entry1))
    Value2 = (int(entry2))
    SCROOLBAR = (int(scroolbar))
    
    print(SCROOLBAR)
    for i in range(1, SCROOLBAR):
        ZAHLEN = random.randint(Value1, Value2)
        Ergenis = ZAHLEN, getRandomZeichen(SWITCHPLUS,SWITCHMINUS,SWITCHGETEILT,SWITCHMAL)

def openNewWindow():
    global entry1
    global entry2
    newWindow = customtkinter.CTkToplevel()
    newWindow.title("Random Generator")
    newWindow.geometry("800x400")
    newWindow._set_appearance_mode(mode)

    def button_event():
        global entry1
        global entry2

        slidervalue = slider.get()
        switchplus = switch_var1.get()
        switchminus = switch_var2.get()
        switchmal = switch_var3.get()
        switchgeteilt = switch_var4.get()
        zahl1 = entry1.get()
        zahl2 = entry2.get()
        berechnungrandom(zahl1, zahl2, slidervalue, switchplus, switchminus, switchmal, switchgeteilt)
        newWindow.destroy()
    Prozeedbutton = customtkinter.CTkButton(
        newWindow, 
        text="Aufgabe Generieren!", 
        command=button_event,
        height=50,
        fg_color="#4a4949",
        corner_radius=17,
        font= ("",17)
    )
    
    Prozeedbutton.pack(fill='both',side='bottom')
    entry1= customtkinter.CTkEntry(
    newWindow, 
    placeholder_text="Start vom benutzten Zahlenraum",
    height=50,
    text_color='grey',
    placeholder_text_color='#b8b4b4',
    corner_radius=17,
    font= ("",17)
        )
    entry1.pack(fill='both')
    entry2= customtkinter.CTkEntry(
    newWindow,
    placeholder_text="Ende vom benutzten Zahlenraum",
    height=50,
    text_color='grey',
    placeholder_text_color='#b8b4b4',
    corner_radius=17,
    font= ("",17)
        )
    entry2.pack(fill='both')
    def slider_event(value):
        global labelslider
        try:
            labelslider.destroy()
        except:
            print('nichts zum löschen')
        labelslider = customtkinter.CTkLabel(
            newWindow, 
            text=f"Anzahl der Benutzen Zahlen: {(int(value))}",
            height=50,
            corner_radius=17,
            text_color='white',
            fg_color='#787575',
            font= ("",17)
        )
        labelslider.pack(fill='both')
        print(value)

    slider = customtkinter.CTkSlider(
        newWindow, 
        from_=1, 
        to=10, 
        command=slider_event,
        number_of_steps=9,
        height=20,
        fg_color="#4a4949"
    )
    slider.pack(fill='both')

    def switch_event():
        print("switch toggled, current value:", switch_var1.get())
        print(switch_var2.get())
        print(switch_var3.get())
        print(switch_var4.get())

    switch_var1 = customtkinter.StringVar(value="off")
    switch1 = customtkinter.CTkSwitch(
        newWindow, 
        text="+", 
        command=switch_event,
        variable=switch_var1, 
        onvalue="on", 
        offvalue="off",
        switch_height=30,
        switch_width=60,
        fg_color="#4a4949"
        )
    switch1.pack(side='right')
    switch_var2 = customtkinter.StringVar(value="off")
    switch2 = customtkinter.CTkSwitch(
        newWindow, 
        text="-", 
        command=switch_event,
        variable=switch_var2, 
        onvalue="on", 
        offvalue="off",
        switch_height=30,
        switch_width=60,
        fg_color="#4a4949"
        )
    switch2.pack(side='right')
    switch_var3 = customtkinter.StringVar(value="off")
    switch3 = customtkinter.CTkSwitch(
        newWindow, 
        text="*", 
        command=switch_event,
        variable=switch_var3, 
        onvalue="on", 
        offvalue="off",
        switch_height=30,
        switch_width=60,
        fg_color="#4a4949"
        )
    switch3.pack(side='right')
    switch_var4 = customtkinter.StringVar(value="off")
    switch4 = customtkinter.CTkSwitch(
        newWindow, 
        text=":", 
        command=switch_event,
        variable=switch_var4, 
        onvalue="on", 
        offvalue="off",
        switch_height=30,
        switch_width=60,
        fg_color="#4a4949"
        )
    switch4.pack(side='right')


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

def segmented_button_callback(value):
    print("segmented button clicked:", value)
app.mainloop()