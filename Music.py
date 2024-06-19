import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pygame import mixer as mixer
import os
def update (ind):
    frame=frames[ind]
    ind+=1
    if ind==framecnt:
        ind=0
    label.configure(image=frame) 
    root.after(40,update,ind)

def  AddMusic():
    path=filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)

        for song in songs:
           if song.endswith(".mp3"):
               playlist.insert(END,song)
def playMusic():
    Music_Name = playlist.get(ACTIVE)
    print(Music_Name)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()             
              
def stopMusic():
    mixer.music.stop()

def pauseMusic():
    mixer.music.pause()

def play_next():
    global current_track, playlist_paths
    current_track = (current_track + 1) % len(playlist_paths)
    mixer.music.load(playlist_paths[current_track])
    mixer.music.play()

    


root= Tk()
root.title("Music") #title of tk.
root.geometry("485x700+290+10") #size of tk
root.configure(background="black")
root.resizable(False, False) #not resizable option.
mixer.init()


framecnt=30
frames=[PhotoImage(file="aa2.gif",height=500, width=500, format='gif -index %i'%(i)) for i in range(framecnt)]  

label=Label(root)  
label.place(x=0,y=0)  
root.after(0,update,0)
  

lower_frame= Frame(root,bg="white",width=485,height=180)
lower_frame.place(x=0,y=400)
image_icon = PhotoImage( file="kaveri.png")
root.iconphoto(False, image_icon)


Menu= PhotoImage(file="menu.png")
Label(root,image=Menu).place(x=0,y=580, width=485, height=100)
Frame_Music = Frame(root, bd=2, relief= RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

play_button = tk.Button(root, text="Play", bg="black", fg="white", bd=0, height=3, width=10, command=playMusic)

play_button.place(x=215, y=487)


Button_Stop= tk.Button(root, text="Stop", bg="black", fg="white", bd=0, height=3, width=10, command=mixer.music.stop )
Button_Stop.place(x=130,y=487)

Button_pause= tk.Button(root, text="Pause", bg="black", fg="white",bd=0, height=3, width=10, command=mixer.music.pause )
Button_pause.place(x=300,y=487)


Button_next=tk.Button(root,text="Next",bg="black", fg="white", bd=0, width=10,height=3, command= play_next)
Button_next.place(x=45, y=487)

Button(root, text="Browse Music", width=59, height=1, font=("Calibri", 12,"bold"),fg="Black", bg="white", command=AddMusic).place(x=0, y=550)
Scroll = Scrollbar(Frame_Music)
playlist=Listbox(Frame_Music, width=100, font=("Times New roman",10), bg="pink", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
playlist.pack(side=RIGHT,fill=BOTH)
Scroll.config(command=playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)

playlist_paths = []
current_track = 0

root.mainloop()
