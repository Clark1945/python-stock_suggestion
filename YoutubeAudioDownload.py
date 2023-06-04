from pytube import YouTube
import os

def download_best_mp3(input_url):
    
    #下載mp4
    dest =f'./排程/download'
    video = YouTube(input_url)
    bestAbrVideo = video.streams.filter(only_audio=True).order_by("abr").desc().first()
    out_file = bestAbrVideo.download(output_path=dest)

    #mp4 換 mp3
    filename,ext = os.path.splitext(out_file)
    new_file = filename + '.mp3'
    try:
        os.rename(out_file,new_file)
    except:
        print("檔案已存在")
        return new_file
    #顯示完成Message
    print(new_file," 下載完成！")
    return new_file