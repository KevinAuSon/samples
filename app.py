import os
import vlc
import glob
import random

from flask import Flask, render_template, jsonify, request, send_from_directory

app = Flask(__name__, static_url_path='/static/')

@app.route("/")
def index():

  samples = glob.glob('static/audio/*.mp3')
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

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static/', path)

if __name__ == "__main__":
    app.run(debug=True)
