import os 
import time
import sys
import tkinter as tk
from googletrans import Translator
from tkinter import filedialog
from tkinter import messagebox

def splash_screen(seconds):
  print("\n")
  print(" ***********************")
  print(" *                     *")
  print(" *      CasRename      *")
  print(" *        v1.0         *")
  print(" *                     *")
  print(" ***********************")
  time.sleep(seconds)
 
#Main Program Starts Here....
splash_screen(3)    
root = tk.Tk()
root.withdraw()
d = filedialog.askdirectory(parent=root,
                                 initialdir=os.getcwd(),
                                 title="Please select a folder:") 
try:
    if d is None:
        sys.exit(0)
    else:
        translator = Translator()
        for path in os.listdir(d):
            full_path = os.path.join(d, path)
            if os.path.isfile(full_path):
                filename, file_extension = os.path.splitext(path)
                new_path = translator.translate(path, dest='en').text
                new_path = os.path.join(d, new_path + file_extension)
                os.rename(full_path, new_path)
    messagebox.showinfo("CasRename", "Renaming Success")
except FileNotFoundError:
    # add code on how you want the error handled
    messagebox.showinfo("CasRename","Folder not selected")