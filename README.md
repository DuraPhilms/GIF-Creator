# GIF-Creator

An online/live implementation can be found at unknown6656.com/harrypotter/


Usage:

```bash
$ python gif-creator.py --help

usage: gif-creator.py [-h] [-p PART] -s START [-d DURATION] [-f FPS] [-r RESOLUTION] {hpues,hpudgpk,hpudpva,hpudpp,hpudodp} output

A GIF creator tool for the DURAPHILMS/COLDMIRROR parodies.

positional arguments:
  {hpues,hpudgpk,hpudpva,hpudpp,hpudodp}
                        The parody identifier.
  output                The output file path.

optional arguments:
  -h, --help            show this help message and exit
  -p PART, --part PART  The number of the part.
  -s START, --start START
                        The start time in seconds.
  -d DURATION, --duration DURATION
                        The duration in seconds.
  -f FPS, --fps FPS     The desired FPS rate.
  -r RESOLUTION, --resolution RESOLUTION
                        The output GIF's horizontal resolution (in pixels).
```



Example: 

```bash
$ python gif-creator.py -p 02 -s 555 -d 30 -f 15 -r 480 hpudodp test.gif
```

![](test.gif)
