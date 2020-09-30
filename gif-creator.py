import argparse
import enum
import sys
import os


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
            return SomeEnum[s.upper()]
        except KeyError:
            return s

        
# 
# gif-creator.py <base-id> [part-number] <start time> <duration> <size>
#
#

parser = argparse.ArgumentParser(description = 'A GIF creator tool for the DURAPHILMS/COLDMIRROR parodies.')
parser.add_argument('baseid', type = BaseID.argparse, choices = list(BaseID))
parser.


#
# TODO : fetch video -> cache ?
# TODO : fetch vtt / srt
# TODO : convert frames -> temporary dir
# TODO : merge into GIF
# TODO : delete temporary frames
#
