#!/usr/bin/env python3

import urllib.request
import subprocess
import argparse
import enum
import uuid
import sys
import os
import re
import pprint


class BaseID(enum.IntEnum):
    HPUES = 1
    HPUDGPK = 2
    HPUDPVA = 3
    HPUDPP = 4
    HPUDODP = 5

    def __str__(self):
        return self.name.lower()
    def __repr__(self):
        return str(self)

    @staticmethod
    def argparse(s):
        try:
            return BaseID[s.upper()]
        except KeyError:
            return s


parser = argparse.ArgumentParser(description = 'A GIF creator tool for the DURAPHILMS/COLDMIRROR parodies.')
parser.add_argument('baseid', type = BaseID.argparse, choices = list(BaseID), help = 'The parody identifier.')
parser.add_argument('-p', '--part', type = int, default = 1, help = 'The number of the part. The default is 1.')
parser.add_argument('-s', '--start', type = str, required = True, help = 'The start time in seconds.')
parser.add_argument('-d', '--duration', type = str, default = "3", help = 'The duration in seconds. The default is "3".')
parser.add_argument('-f', '--fps', type = int, default = 15, help = 'The desired FPS rate. The default is 15.')
parser.add_argument('-r', '--resolution', type = int, default = 480, help = "The output GIF's horizontal resolution (in pixels). The default is 480.")
# parser.add_argument('-s', '--subtitles', type = bool, default = False, help = '')
parser.add_argument('output', type = str, help = "The output file path.")

args = parser.parse_args()
pprint.pprint(args)


if (re.match(r'^hp\w+$', str(args.baseid)) is None or
    re.match(r'^\d+$', str(args.part)) is None or
    re.match(r'^(\d*:)*\d+(\.\d*)?$', str(args.start)) is None or
    re.match(r'^(\d*:)*\d+(\.\d*)?$', str(args.duration)) is None or
    re.match(r'^\d+$', str(args.fps)) is None or
    re.match(r'^\d+$', str(args.resolution)) is None):
    print("unable to parse arguments.")
else:
    video_uri = f"https://unknown6656.com/harrypotter/videos/{str(args.baseid).lower()}/{args.part:02}.mp4"
    subtitle_uri = f"https://unknown6656.com/harrypotter/subtitles/{str(args.baseid).lower()}/{args.part:02}.srt"
    random_id = '.' + str(uuid.uuid4())

    print(video_uri)
    print(subtitle_uri)
    print(random_id)

    try:
        with urllib.request.urlopen(subtitle_uri) as fs:
            with open(random_id + '.srt', 'wb') as file:
                bytes = fs.read()
                file.write(bytes)
    except:
        pass

    try:
        # f"ffmpeg -y -i {video_uri} -i {subtitle_uri} -ss {args.start} -t {args.duration} -pix_fmt rgb24 -r 10 -s 320x240 output-temp.gif"
        subtitlefile = random_id + '.srt'
        subtitlestr = f",subtitles={subtitlefile}:force_style='Fontsize=24'" if os.path.exists(subtitlefile) else ""
        command = f"ffmpeg -y -i {video_uri} -ss {args.start} -t {args.duration} -vf fps={args.fps},scale={args.resolution}:-1:flags=lanczos{subtitlestr} {random_id}.gif"

        print(command)

        if os.system(command) == 0:
            converted = False

            try:
                if os.system(f'optimize -layers Optimize {random_id}.gif "{args.output}"') == 0:
                    converted = True
            except:
                pass

            if not converted:
                os.rename(random_id + '.gif', args.output)
    except:
        pass

    for file in [random_id + '.srt', random_id + '.gif']:
        if os.path.exists(file):
            os.remove(file)
