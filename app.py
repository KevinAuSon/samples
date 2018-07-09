import os
import vlc
import glob
import random

from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for
from werkzeug import secure_filename

app = Flask(__name__, static_url_path='/static/')

url_audio = 'static/audio'

@app.route("/")
def index():

  samples = glob.glob(os.path.join(url_audio, '*.mp3'))
  data = []
  for sample in samples:
    sample = os.path.splitext(os.path.basename(sample))[0]
    data.append((sample, sample.title()))

  return render_template("index.html", samples=data)


@app.route("/play/<sample>")
def play(sample):
  samples = glob.glob('static/audio/{}.mp3'.format(sample))
  sample = random.choice(samples)

  p = vlc.MediaPlayer(sample)
  p.audio_set_volume(100)
  p.play()

  return ('', 204)

@app.route('/upload', methods = ['POST'])
def upload_file():
    f = request.files['file']
    f_name = os.path.join(url_audio, secure_filename(f.filename))
    f.save(f_name)

    return redirect('/')

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static/', path)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
