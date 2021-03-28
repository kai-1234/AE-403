import tkinter as tk
window = tk.Tk()
window.title('Menu')
window.geometry('500x500')

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