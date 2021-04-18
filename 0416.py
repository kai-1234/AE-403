from pytube import YouTube
progress = 0
def showProgress(stream,chunk,bytes_remaining):
    size = stream.filesize
    global progress
    preprogress= progress
    currentprogress=(size-bytes_remaining)*100//size
    progress = currentprogress
    if progress == 100:
        print('下載完成！')
    elif preprogress != progress:
        print('下載進度:'+ str(progress)+'%')
    

yt = YouTube('https://www.youtube.com/watch?v=Yd9oluAZiTs',
             on_progress_callback=showProgress)
stream = yt.streams.filter(res='720p',only_video=False).first()
stream2 = yt.streams.filter(res='480p',only_video=False).first()
stream3 = yt.streams.filter(res='360p',only_video=False).first()
stream4 = yt.streams.filter(res='240p',only_video=False).first()
stream5 = yt.streams.filter(res='144p',only_video=False).first()
stream.download('youtube','720p')
stream2.download('youtube','480p')
stream3.download('youtube','360p')
stream4.download('youtube','240p')
stream5.download('youtube','144p')