import YoutubeDataAPI
import YoutubeAudioDownload
import AudioSplit_Whisper

youtube_api_key = "" #請輸入 自己的API Key
channel_id = "" # 以 網頁檢視原始碼 勾選 Line Wrap 並搜尋 ?channel_id 就可以找到 channel_id
GPT_API_KEY = ""
getMyInfo = YoutubeDataAPI.getYTLink(youtube_api_key)
uploadId = getMyInfo.get_channel_uploads_id(channel_id)
video_all = getMyInfo.get_playlist(uploadId) # 取得今日影片


for today_video_index in range(len(video_all)):
    splitList = []
    KeyMessageList = ""
    video = YoutubeAudioDownload.download_best_mp3(video_all[today_video_index]) # 下載影片
    splitList = AudioSplit_Whisper.spiltAudio(video,today_video_index) # 分割片段
    
    for partAudio in splitList:
        partMessage = AudioSplit_Whisper.transcribeAudio(partAudio,GPT_API_KEY) # 語音轉文字
        print(partMessage)
        stockMessage = AudioSplit_Whisper.analysisText(partMessage,GPT_API_KEY) # 文字轉ChatGPT統計
        KeyMessageList+=stockMessage # 同一部影片會被加再一起
    with open(r".\排程\download\Output.text","a+") as file:
        file.write(KeyMessageList)
    
    


