from flask import Flask,render_template,request,send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/youmightlike',methods=['GET','POST'])
def reccomend():
    if request.method == 'POST':
            ytube = request.form.get("fname")
            yt = YouTube(str(ytube))
  
            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

            destination = r"songs"
            
            # download the file
            out_file = video.download(output_path=destination)
            
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            
            # result of success
            yes = yt.title
            path = "flask_try/first_app/songs/{}.mp3".format(yes)
            return send_file(path, as_attachment=True)
if __name__ == '__main__':
   app.run()