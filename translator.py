from cProfile import label
from cmath import e
from logging import root
from tkinter import *
import googletrans
from matplotlib.pyplot import pink
from regex import F, R
from sqlalchemy import null 
import textblob;
from tkinter import messagebox,ttk
from turtle import clear
from operator import ge
import cv2 
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from pytesseract import pytesseract
from sympy import im, re
from PIL import Image,ImageTk
root= Tk()
root.title("Translator")
root.geometry("1500x1500")
root.configure(background='pink')

def image_it():
    global img1
    f_types = [('Jpg Files', '*.jpg'),('PNG File','*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    # img1 = ImageTk.PhotoImage(file=filename)
    # img2= filename.str()
    try:
      def ocr_core(img):
          text= pytesseract.image_to_string(img)
          return text
     
      img = cv2.imread(filename)
  
  
      def get_grayscale_(image):
         return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


      def remove_noise(image):
        return cv2.medianBlur(image,5)
 

      def thresholding(image):
        return cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]


      img= get_grayscale_(img)
      img= remove_noise(img)
      img=thresholding(img)
      p=ocr_core(img)
      
        

      original_text.insert (1.0,p)

    except Exception as e:
        messagebox.showerror("Translator",e)

    return(ocr_core)


x= image_it()
def translate_it():
    x= null
    translated_text.delete(1.0,END)
    try:
        #get the languages from the dictionary 
        #get the from language key
        for key, value in languages.items():
            if (value == original_combo.get()):
                from_lang_key = key

        for key, value in languages.items():
            if (value == trans_combo.get()):
                to_lang_key = key
           
        if(x!=null):
            word = textblob.TextBlob(x)
        else:
            word = textblob.TextBlob(original_text.get(1.0,END))

        word = word.translate(from_lang= from_lang_key, to = to_lang_key)

        translated_text.insert (1.0,word)

    except Exception as e:
        messagebox.showerror("Translator",e)


def clear():
    original_text.delete(1.0,END)
    translated_text.delete(1.0,END)

languages=googletrans.LANGUAGES
language_list= list(languages.values())
# print(language_list)
label = Label(root, text="Translator", font=('Helvetica',44),background="pink")
label.grid(row=0, column=1,padx=50,pady=20)
original_text= Text(root,width=50,height=10)
original_text.grid(row=1,column=0,padx=100,pady=150)
trans_button = Button(root,text="Translate",font=('Helvetica',24),bg="pink",fg="white",command=translate_it)
trans_button.grid(row=1,column=1,padx=10)
translated_text=Text(root,width=50,height=10)
translated_text.grid(row=1,column=2,padx=140,pady=150)

original_combo = ttk.Combobox(root, width=20,value=language_list)
original_combo.current(21)
original_combo.grid(row=2,column=0,padx=10,pady=20)

trans_combo = ttk.Combobox(root, width=20,value=language_list)
trans_combo.current(25)
trans_combo.grid(row=2,column=2,padx=10,pady=20)

clear_button = Button(root,text="Clear",font=('Helvetica',24),command=clear)
clear_button.grid(row=3,column=1)

photo = PhotoImage(file = r"camera3.png")
camera_button = Button(root,text="Image", image = photo,font=('Helvetica'),command= image_it)
camera_button.grid(row=3,column=0,padx=10,pady=20)
# original_text.insert(1.0,x)
# root.resizable(True, True)
root.attributes('-fullscreen', True)
root.mainloop()