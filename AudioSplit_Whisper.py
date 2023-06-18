import openai,os,datetime
# 使用pydub 下 ffmpeg 功能分割音訊
from pydub import AudioSegment
def transcribeAudio(audio,apiKey):
    # 讀取檔案，使用OpenAI 下的 Whisper 進行語音轉文字
    with open(audio,"rb") as audio_file:
        openai.api_key = apiKey
        model_id = "whisper-1"
        response = openai.Audio.transcribe(model_id, audio_file)
        
        return str(response['text'])
    

def spiltAudio(audioFile,today_video_index):
    AudioSegment.ffmpeg = r"D:\\MyFold\\Tools\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe"
    sound = AudioSegment.from_file(audioFile)
    
    dest = r".\\download\\"+str(datetime.datetime.now().strftime("%Y%m%d"))+"\\"
    if not os.path.exists(dest):
        os.mkdir(dest)

    #print(sound.duration_seconds) # 影片長度
    today = datetime.datetime.now().strftime("%Y%m%d")
    spiltAmt= int(sound.duration_seconds // 120) +1
    allSplitAudio = []
    for partIndex in range(spiltAmt):
        two_minute = 120 * 1000 # 以10分鐘分割 pydub does things in milliseconds
        # song clip of 10 seconds from starting
        eachPartAudio = sound[partIndex*two_minute:two_minute*(partIndex+1)] # 分割

        # save file
        eachPartAudio.export(dest+today+"index="+str(today_video_index)+"part="+str(partIndex)+".mp3",format="mp3") # 輸出片段
        allSplitAudio.append(dest+today+"index="+str(today_video_index)+"part="+str(partIndex)+".mp3")

    print("音訊分割完成！")
    return allSplitAudio


def analysisText(text,apiKey):
    openai.api_key = apiKey
    completion = openai.Completion.create(
        model="text-davinci-003",
        prompt="幫我整理統計以下文章中出現了哪些股票，並以逗號分隔:\n"+text,
        temperature=0.3,
        max_tokens=2500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
    # model 是使用的訓練模型
    # prompt 提問事項
    # max_tokens 回覆文具最多的Token數，不可超過4000個
    # temperature 0~1的冒險程度 0是最嚴苛
    # presence_penalty 鼓勵產生語句時使用新的token
    # frequency_penalty 值越大越會懲罰出現頻率高的Token，避免重複

    response = completion.choices[0].text
    return response