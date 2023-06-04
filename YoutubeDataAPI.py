import requests
from datetime import datetime

class getYTLink:
    # 建構式
    def __init__(self, api_key):
        self.base_url = "https://youtube.googleapis.com/youtube/v3/"
        self.api_key = api_key  # API 金鑰
    
    def get_html_to_json(self, path):
        """組合 URL 後 GET 網頁並轉換成 JSON"""
        api_url = f"{self.base_url}{path}&key={self.api_key}"
        header = {'Accept':'application/json','Authorization':"Bearer "+str(self.api_key)}
        r = requests.get(api_url)
        if r.status_code == requests.codes.ok:
            data = r.json()
        else:
            data = None
        return data
    
    def get_channel_uploads_id(self, channel_id, part='contentDetails'):
        """取得頻道上傳影片清單的ID"""
        path = f'channels?part={part}&id={channel_id}'
        data = self.get_html_to_json(path)
        try:
            uploads_id = data['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        except KeyError:
            uploads_id = None
        return uploads_id

    def get_playlist(self, playlist_id, part='contentDetails', max_results=3):
        """取得影片清單ID中的影片"""
        path = f'playlistItems?part={part}&playlistId={playlist_id}&maxResults={max_results}'
        data = self.get_html_to_json(path)
        if not data:
            return []
        video_ids = []
        dt = datetime.now().strftime("%Y%m%d")
        for data_item in data['items']:
            publishDate = str(data_item['contentDetails']['videoPublishedAt'])[:10].replace("-", "")
            if  publishDate[:4] == dt[:4] and publishDate[4:6] == dt[4:6] and int(publishDate[6:]) <= int(dt[6:]) and int(publishDate[6:]) > int(dt[6:])-2:
                video_ids.append("https://www.youtube.com/watch?v="+data_item['contentDetails']['videoId'])
        return video_ids




