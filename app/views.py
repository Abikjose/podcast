import os
from flask import Flask, request, render_template
from app import app

music_dir = '/home/app/podcast/app/static/music'
video_dir = '/home/app/podcast/app/static/videos'
image_dir = '/home/app/podcast/app/static/images'

@app.route('/')
@app.route('/index')
def index():
    music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
    music_files_number = len(music_files)
    return render_template("index.html",
                        title = 'Home',
                        music_files_number = music_files_number,
                        music_files = music_files)

@app.route('/<filename>')
def song(filename):
    return render_template('play.html',
                        title = filename,
                        music_file = filename)
