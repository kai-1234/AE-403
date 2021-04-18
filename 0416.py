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
    

yt = YouTube('https://www.youtube.com/watch?v=xt_Ivk_NbRI',
             on_progress_callback=showProgress)
stream = yt.streams.filter(res='720p').first()
stream2 = yt.streams.filter(res='480p').first()
stream3 = yt.streams.filter(res='360p').first()
stream4 = yt.streams.filter(res='240p').first()
stream5 = yt.streams.filter(res='144p').first()
stream6 = yt.streams.filter(res='1080p').first()
stream6.download('youtube','1080p')
stream.download('youtube','720p')
stream2.download('youtube','480p')
stream3.download('youtube','360p')
stream4.download('youtube','240p')
stream5.download('youtube','144p')