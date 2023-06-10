from pytube import YouTube
import os,datetime

def download_best_mp3(input_url):
    
    #下載mp4
    dest = ".\\download"
    if not os.path.exists(dest):
        os.mkdir(dest)
        os.mkdir(dest+"\\video")
    video = YouTube(input_url)
    if "(字幕版)" not in video.title and "short" not in video.title: # 只取直播檔案
        print("取得影片資源："+video.title)
        bestAbrVideo = video.streams.filter(only_audio=True).order_by("abr").desc().first()
        out_file = bestAbrVideo.download(output_path=dest+"\\video")
    
        #轉換 mp3
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
    else:
        return ""