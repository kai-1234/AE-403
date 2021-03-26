import tkinter as tk
import tkinter.messagebox
def clickMe():
    tkinter.messagebox.showinfo(title='OUCH',message='OUCH! OOF it hurts!')
window = tk.Tk()
window.title('晞愷的第一個GUI程式')
window.geometry('300x300')
label=tk.Label(window,text ='晞愷',bg="#123",fg="#A43")
label.pack()
entry=tk.Entry(window,width = 20)
entry.pack()
button=tk.Button(window,text = "按我",command=clickMe)
button.pack()
    
window.mainloop()
