# python-stock_suggestion
讓CHATGPT幫你分析投顧分析師天天說了什麼。
-------------------------------------------------------------
簡介：
這是一個透過ChatGPT服務讓你方便追蹤投顧分析師天天的節目，並將他們整理成簡短的文字敘述，後續想改成排程執行也相當方便。
使用到的工具如下：

●  Youtube Data API 用來擷取投顧分析師每日最新的影片
●  pytube套件 用來將擷取的URL下載到本地端
●  ffmpeg套件 用來分割音訊，因為Whisper API 一次能產生的文字量有限，所以需要分批處理，現在專案用10分鐘為計算標準。
●  Openai套件 當中包含ChatGPT以及Whisper，Whisper用來將音訊檔轉換成文字稿，ChatGPT用來將大量文字統整輸出。



使用方法：
1. 申請ChatGPT API金鑰 (https://platform.openai.com/account/api-keys) 
※ 需要先擁有帳號
2. 申請Youtube API金鑰 (https://console.cloud.google.com/apis/credentials?hl=zh-tw&project=myfirstproject-371113)
※ 需要先擁有帳號
3. 取得想要抓取Youtube頻道的channel_id 
(目前 Youtube 已經沒有公開顯示頻道ID，需要另外透過方法取得，詳見此影片：https://www.youtube.com/watch?v=0oDy2sWPF38&list=LL&index=5&t=1s&ab_channel=GaugingGadgets)
