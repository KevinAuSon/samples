import os
import vlc
import glob
import random
import subprocess
from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, url_for
from werkzeug import secure_filename

app = Flask(__name__, static_url_path='/static/')

url_audio = 'static/audio'
vlc_sample = None
volume_sample = 100

@app.route("/")
def index():
  samples = glob.iglob(os.path.join(url_audio, '**', '*.mp3'), recursive=True)
  data = {}
  for sample in samples:
    path = sample.split('/')[2:]
    url = os.path.join(*path)[:-4]
    sample = os.path.splitext(os.path.basename(sample))[0]
    value = (url, sample)
    key = len(path) == 2 and path[0] or 'Others'

    values = data.get(key, [])
    values.append(value)
    data[key] = values

  return render_template("index.html", samples=data)


@app.route("/play")
def play():
  sample = request.args.get('sample', '')
  samples = glob.glob('static/audio/{}.mp3'.format(sample))
  
  # If it was a directory (random)
  if not samples:
    if sample == 'Others':
      samples = glob.glob('static/audio/*.mp3')
    else:
      samples = glob.iglob(os.path.join(url_audio, sample, '**', '*.mp3'), recursive=True)
      samples = list(samples)

  sample = random.choice(samples)

  global vlc_sample

  if vlc_sample:
    vlc_sample.stop()

  vlc_sample = vlc.MediaPlayer(sample)
  vlc_sample.audio_set_volume(volume_sample)
  vlc_sample.play()

  return ('', 204)


@app.route("/stop")
def stop():
  global vlc_sample

  if vlc_sample:
    vlc_sample.stop()
    vlc_sample = None
    
  return ('', 204)

@app.route("/volume")
def volume():
  global volume_sample
  action = request.args.get('action', '')
  
  if action == 'up':
    volume_sample = min(100, volume_sample + 20)
  elif action == 'down':
    volume_sample = max(0,   volume_sample - 20)
  elif action == 'mute':
    volume_sample = 0

  if vlc_sample:
    vlc_sample.audio_set_volume(volume_sample)

  return ('', 204)

@app.route("/reboot")
def reboot():
  os.system('sudo reboot')


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
    app.run(debug=True, host='0.0.0.0')
