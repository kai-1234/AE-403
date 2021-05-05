from pytube import YouTube  #匯入模組
import tkinter as tk
import threading
progress = 0    
def showProgress(stream,chunk,bytes_remaining): #建立showProgress函式
    size = stream.filesize #取得影片大小
    global progress
    preprogress= progress
    currentprogress=(size-bytes_remaining)*100//size
    progress = currentprogress
    if progress == 100:  #判斷如果進度是100，便會print下載完成
        print('下載完成！')
        button.config(state=tk.NORMAL,text = '下載')
        return
    elif preprogress != progress: #如果進度還沒到100，會寫下載進度
        scale.set(progress) #把進度條變長
        window.update()#把視窗更新
        print('下載進度:'+ str(progress)+'%')
def thread():
    threading.Thread(target=onClick).start()
#
def onClick(): #建立onClick函式
    
    global var
    var.set(entry.get()) #把var設成entry輸入的網址
    button.config(state=tk.DISABLED,text = '正在下載中...')
    try:
        yt = YouTube(var.get(),on_progress_callback=showProgress) #建立yt變數
        if var3.get() and var2.get():
            stream = yt.streams.filter(res="1080p",only_audio=False,only_video=False).first()#調yt的設定，存在stream裡
        elif var3.get():
            stream = yt.streams.filter(res="1080p",only_audio=True).first()
        elif var2.get():
            stream = yt.streams.filter(res="1080p",only_video=True).first()
        else:
            stream = yt.streams.filter(res="1080p").first()
        stream.download('youtube','downloader') #下載影片
    except: #失敗的話會print'FAIL'
        print("FAIL")
        button.config(state=tk.NORMAL,text = '下載')


window = tk.Tk() #設定視窗
window.geometry('500x200') #設定視窗大小 
window.resizable(False,False) #讓視窗無法調整大小
label = tk.Label(window,text="輸入要下載的影片的網址") #建立label元件
label.pack() #打包label
var = tk.StringVar() #建立var變數
entry = tk.Entry(window,width=50)#建立entry元件
entry.pack() #打包window
var3 = tk.BooleanVar()
var2 = tk.BooleanVar()

check = tk.Checkbutton(window,text='有音樂',variable=var3,onvalue=True,offvalue=False)
check2 = tk.Checkbutton(window,text='有影片',variable=var2,onvalue=True,offvalue=False)
check.pack()
check2.pack()
button = tk.Button(window,text="下載",command=thread)#建立button元件，按下去可以下載影片
button.pack()#打包button
scale = tk.Scale(window,label="Scale",from_=0,to=100,orient = tk.HORIZONTAL,
                 length=200,showvalue = False,tickinterval=0) #建立scale元件(進度條)
scale.pack()#打包scale


window.mainloop() 
