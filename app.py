from flask import Flask,render_template,request,send_file,send_from_directory
from pytube import YouTube
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'songs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/',methods=['GET','POST'])
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
            randnum = str(random.randint(0,696969))
            new_file = 'songs/' + randnum + '.mp3'
            os.rename(out_file, new_file)
            
            # result of success
            yes = yt.title
            path = "/{}.mp3".format(yes)
            #uploads = os.path.join(current_app.root_path, app.config['songs'])
            return render_template('output.html',filename = yes ,rnad = randnum )

@app.route('/downloads/<name>')
def download_file(name):
    return send_file("songs/{}.mp3".format(name),as_attachment=True)


if __name__ == '__main__':
   app.run()