from flask import Flask, render_template, request, send_file
import requests
import os
import zipfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_videos():
    urls = request.form['urls'].split('\n')  
    urls = [url.strip() for url in urls]  
    urls = list(filter(None, urls))  

    
    if len(urls) > 50:
        return "Error: Maximum of 50 URLs allowed."

    headers = {
        "X-RapidAPI-Key": "votre clé API",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    
    zipfilename = "tiktok_videos.zip"
    with zipfile.ZipFile(zipfilename, 'w') as zipf:
        for url in urls:
            querystring = {"url": url}
            response = requests.get("https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index", headers=headers, params=querystring)

            if response.status_code == 200:
                video_url = response.json()['video'][0]
                video_data = requests.get(video_url).content

                
                filename = secure_filename(url) + ".mp4"

                
                zipf.writestr(filename, video_data)

    
    return send_file(zipfilename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
