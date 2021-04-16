import tkinter as tk
window = tk.Tk()
window.title('Radiobutton')
window.geometry('500x500')

string = tk.StringVar()
string2=tk.StringVar()
string3=tk.StringVar()
def selection():
    label.config(text ='我是'+ string2.get()+',我喜歡'+ string.get()+',我讀'+string3.get())
    
    
label=tk.Label(window,text='尚未選擇',bg='#00f',fg='#ff0')
label.pack()

radio1=tk.Radiobutton(window,text="Minecraft Python",
                      variable=string,value='Python'
                      ,command = selection)
radio2=tk.Radiobutton(window,text="Minecraft",
                      variable=string,value='Minecraft'
                      ,command = selection)
radio3=tk.Radiobutton(window,text="Pygame",
                      variable=string,value='Pygame'
                      ,command = selection)
radio4=tk.Radiobutton(window,text="女性",
                      variable=string2,value='女性'
                      ,command = selection)
radio5=tk.Radiobutton(window,text="男性",
                      variable=string2,value='男性'
                      ,command = selection)
radio6=tk.Radiobutton(window,text="國小",
                      variable=string3,value='國小'
                      ,command = selection)
radio7=tk.Radiobutton(window,text="國中",
                      variable=string3,value='國中'
                      ,command = selection)
radio8=tk.Radiobutton(window,text="高中",
                      variable=string3,value='高中'
                      ,command = selection)
radio9=tk.Radiobutton(window,text="大學",
                      variable=string3,value='大學'
                      ,command = selection)


string.set('Minecraft Python')
string2.set('Minecraft Python')
string3.set('Minecraft Python')
radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()
radio5.pack()
radio6.pack()
radio7.pack()
radio8.pack()
radio9.pack()
menuBar = tk.Menu(window)

singleMenu = tk.Menu(menuBar,tearoff=False)
singleMenu.add_command(label='New world')
singleMenu.add_command(label='Old world')

multiMenu = tk.Menu(menuBar,tearoff=False)
multiMenu.add_command(label='Best server')
multiMenu.add_command(label='LAN world')
multiMenu.add_separator()

settingsMenu = tk.Menu(menuBar,tearoff=False)
settingsMenu.add_command(label='Add server')
settingsMenu.add_command(label='Edit')
multiMenu.add_cascade(label='Settings',menu = settingsMenu)

optionsMenu = tk.Menu(menuBar,tearoff=False)
optionsMenu.add_command(label='遊戲設定')
optionsMenu.add_command(label='畫面設定')
optionsMenu.add_separator()
optionsMenu.add_command(label='返回')

fileMenu = tk.Menu(menuBar,tearoff=False)
fileMenu.add_command(label='開新遊戲')
fileMenu.add_command(label='作弊指令')
fileMenu.add_separator()
fileMenu.add_command(label='Quit Game')

subMenu=tk.Menu(menuBar,tearoff=False)
subMenu.add_command(label='遊戲優化')
subMenu.add_command(label='攻擊敵人')
optionsMenu.add_cascade(label='Game',menu = subMenu)

menuBar.add_cascade(label='File',menu = fileMenu)
menuBar.add_cascade(label='Option',menu = optionsMenu)
menuBar.add_cascade(label='Single Player',menu = singleMenu)
menuBar.add_cascade(label='Multi Player',menu = multiMenu)

window.config(menu=menuBar)
window.mainloop()