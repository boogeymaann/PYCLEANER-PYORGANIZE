#------------------------------------------------------------------------------------------------------------
#welcome to boogeyman auto cleaner 
#this was done in like 30 minutes,super simple, i didn't test it too much , i just know that it works
#if there is any error at some point i am sorry / let me know 
#thank you
#i am not sure if anyone will ever see use this but ,if you do let me know :) 
#---------------------------------------------------------------------------------------------------------

from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import os
import tempfile
import shutil

#this is a dictionary with keys and list pairs of certain genres and the popular extensions
#i got the inspiration from IDM when you download some files and it is automatically sorted

common_extensions = {
    'zip': ['.zip', '.tar', '.tar.gz', '.tar.bz2', '.tar.xz', '.gz', '.bz2', '.7z','.rar'],
    'video': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg', '.m4v'],
    'programming': [
        '.c', '.cpp', '.h', '.hpp', '.java', '.py', '.js', '.html', '.css', '.php', '.swift',
        '.ruby', '.go', '.ts', '.json', '.xml', '.sh', '.yml', '.ini', '.cfg'
    ],
    'setups and executables': ['.exe', '.msi', '.dmg', '.deb', '.rpm', '.sh', '.bat', '.command', '.pkg', '.appimage',
        '.yml', '.ini', '.cfg','.com', '.cmd', '.ps1', '.jar'],
    'music': ['.mp3', '.wav', '.flac', '.m4a', '.ogg', '.wma', '.aac', '.ac3', '.mid', '.midi'],
    'document': ['.doc','.ods', '.docx','.bpz', '.pdf', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.csv', '.ppt', '.pptx', '.html'],
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico'],
    'dll': ['.dll', '.ocx', '.drv', '.sys', '.cpl', '.acm', '.ax', '.scr']
}
#i googled this method , i did not about the shutil rmtree function 
#but the message box was my idea :D
def tempclean():
    temp = tempfile.gettempdir()
    shutil.rmtree(temp, ignore_errors=True)
    messagebox.showinfo(title="Success", message="Deleted successfully")

#chatgpt wrote most of this code :( , i could not figure the sortfolder() method
#after like 2 hours of trying and regretting learning programing and 2 cups of coffe later,
# i surrenderd , and went to chatgpt and told him to write me the dictionary above and this sortfolder() method
#everyhing else was my doing so , it's a small win i guess ?
#i am sorry , i talk too much , i have no programming freinds :(

def sortfolder():
    folderpath = filedialog.askdirectory(initialdir="c:\\program files\\", title="Choose a folder to organize")
    files = os.listdir(folderpath)

    for file in files:
        if os.path.isfile(os.path.join(folderpath, file)):
            _, extension = os.path.splitext(file)
            extension = extension.lower()

            # Check which genre the extension belongs to
            for genre, ext_list in common_extensions.items():
                if extension in ext_list:
                    category_folder = os.path.join(folderpath, genre)
                    if not os.path.exists(category_folder):
                        os.mkdir(category_folder)

                    # Move the file to the corresponding folder
                    source_path = os.path.join(folderpath, file)
                    destination_path = os.path.join(category_folder, file)
                    shutil.move(source_path, destination_path)

                    break  # Break the loop once the file is moved

    messagebox.showinfo(title="Success !!!!!!", message="Files sorted successfully")

#and this is just some basic Tkinter , if you don't know what any of this means ,
#go watch bro code TKINTER tutorial and also johan godinho Tkinter tutorial, i recommend them for beginners(y)
window = Tk()
window.title("DA BOOGEY CLEANER")
window.resizable(False,False)
window.geometry("450x450")

sortbutton = Button(text="PICK A FILE TO ORGANIZE", font=("comicsans", 18, "bold"), bg="#ff0006",
                    fg="#6e0002", activebackground="#ff0006", activeforeground="#6e0002",
                    relief="ridge", command=sortfolder)
sortbutton.pack(anchor=S, side="bottom", padx=20, pady=30)

cleanbutton = Button(text="CLEAN TEMP FILES", font=("comicsans", 18, "bold"), bg="#ff0006",
                     fg="#6e0002", activebackground="#ff0006", activeforeground="#6e0002",
                     relief="ridge", command=tempclean)
cleanbutton.pack(anchor=S, side="bottom", padx=20, pady=30)

window.mainloop()
