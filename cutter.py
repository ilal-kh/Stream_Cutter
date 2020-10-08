import re
import os
import pandas as pd
import math
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from window import *


def text_to_time(text):
    text['i'] = text['n_t'].map(lambda x: str(re.match('\d', x)))
    text = text[text['i'] != 'None']
    text.pop('i')
    text[['start_time', 'text']] = text.n_t.str.split(' ', 1, expand=True)
    text.pop('n_t')
    text = text.reset_index()
    return text


def time_to_int(time, i):
    if len(time['start_time'][i]) <= 5:
        mm, ss = time['start_time'][i].split(':')
        t = int(ss) + 60 * int(mm)
    else:
        hh, mm, ss = time['start_time'][i].split(':')
        t = int(ss) + 60 * (int(mm) + 60 * int(hh))
    return t


def cut_video(video, time, path, i, n, root):
    i = int(i)
    progress_bar = create_progress_bar(root)
    while int(i) <= int(n)-1:
        s_t = time_to_int(time, i)
        if int(i) == int(n)-1:
            e_t = math.floor(VideoFileClip(video).duration)
        else:
            e_t = time_to_int(time, i+1)
        ffmpeg_extract_subclip(video, s_t, e_t,
                               targetname="{}\{} {}.mp4".format(path,
                                                                i+1,
                                                                time['text'][i].replace('?', '').replace('"', '')))
        progress_bar_move(progress_bar, n)
        root.update()
        print("_______________________________________________________________________________________________________")
        i += 1
    end_msg()

def clicked(text_1, text_2, text_3, window):
    video = text_1.get()
    text = pd.read_csv(text_2.get(),
                       sep="\n",
                       header=None,
                       names=['n_t'])
    text = text_to_time(text)
    path = text_3.get()
    n = len(text['text'])
    try:

        os.mkdir(path)
    except FileExistsError:
        'Уже есть папка'
    cut_video(video=video, time=text, path=path, i=0, n=n, root=window)



