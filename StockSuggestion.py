import YoutubeDataAPI
import YoutubeAudioDownload
import AudioSplit_Whisper
import time,logging,datetime

youtube_api_key = "" #請輸入 自己的API Key
GPT_API_KEY = ""

#以 網頁檢視原始碼 勾選 Line Wrap 並搜尋 ?channel_id 就可以找到 channel_id
channel_list = []
channel_list.append("UChfl3auNxAxOR3wy8a8ysQQ") #{郭哲榮}
channel_list.append("UC9Pd7LN9potuHVafJCLX7Pw") #{林鈺凱}

ref_name = {0:"郭哲榮",1:"林鈺凱"}

logging.basicConfig(filename="stockSuggestion.log",format='%(asctime)s %(message)s',encoding="utf-8",level=logging.INFO)
# 取得Youtube物件後，利用頻道ID取得頻道上傳ID，再根據時間取得今日影片
YT_Object = YoutubeDataAPI.YoutubeObject(youtube_api_key)
for channel_id in range(len(channel_list)):
    uploadId = YT_Object.get_channel_uploads_id(channel_list[channel_id]) 
    video_all = YT_Object.get_playlist(uploadId) # 取得今日影片

    logging.info("第"+str(channel_id+1)+"位分析師的影片共有%d部"%(len(video_all)))
    idx = 0

    for today_video_index in range(len(video_all)):
        splitList = []
        KeyMessageList = ""
        video = YoutubeAudioDownload.download_best_mp3(video_all[today_video_index]) # 下載影片
        
        if(""==video):
            continue
        splitList = AudioSplit_Whisper.spiltAudio(video,idx) # 分割片段
        
        for partAudio in range(len(splitList)):
            logging.info("開始擷取")
            try:
                partMessage = AudioSplit_Whisper.transcribeAudio(splitList[partAudio],GPT_API_KEY) # 語音轉文字
                partMessage=partMessage.replace("\n", "").replace("\r", "")
                logging.info("第"+str(partAudio)+"部分完成~")
                stockMessage = AudioSplit_Whisper.analysisText(partMessage,GPT_API_KEY) # 文字轉ChatGPT統計
                KeyMessageList=stockMessage # 同一部影片會被加再一起
            except:
                logging.error("第"+str(partAudio)+"部份發生錯誤")
                continue
            with open(f'.\download\Result-{ref_name[channel_id]+" in "+ str(datetime.datetime.now().strftime("%Y%m%d"))}.txt',"a+",encoding="utf-8") as file:
                file.write(KeyMessageList)
            logging.info("擷取完成～ＣＤ中")
            time.sleep(25)
        idx+=1

print("完成啦，準備寄送郵件...")
    
    


