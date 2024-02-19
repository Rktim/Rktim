#CLOCK


from tkinter import*
#from tkinter.ttk import*


from time import*

def updt():
    time_st=strftime("%I:%M:%S %p")
    time_l.config(text=time_st)
    
    date_st=strftime('%A')
    date_l.config(text=date_st)
    
    day_st=strftime("%B %d:%Y")
    day_l.config(text=day_st)
    window.after(1000,updt)
    
    
    
window=Tk()


time_l=Label(window, font=('Times',67),fg='yellow',bg='black')
time_l.pack()

date_l=Label(window, font=('Helvetica',60),fg='red',bg='black')
date_l.pack()

day_l=Label(window, font=('Arial',57),fg='#00FF00',bg='black')
day_l.pack()

updt()
window.mainloop()
