## Project Info
 
[電腦端立院IVOD下載器 hackpad](https://g0v.hackpad.com/IVOD-KdTs5gZb3yw)

[billy3321/ivod-download-client](https://github.com/billy3321/ivod-download-client)

python tool

* [rg3/youtube-dl](https://github.com/rg3/youtube-dl)
* [youtube-dl: Download Page](http://rg3.github.io/youtube-dl/download.html)
* [vid2a.com/scrape.py at master · bobpoekert/vid2a.com](https://github.com/bobpoekert/vid2a.com/blob/master/scrape.py)
* [crtaci/player.py at master · gen2brain/crtaci](https://github.com/gen2brain/crtaci/blob/master/frontend/python/crtaci/player.py)
* [kuyan/yaas](https://github.com/kuyan/yaas)

php tool

* [電腦端立院IVOD下載器(win protable) | 巴克里](http://jangmt.com/?p=108)

## Test Log

Test 2014/09/27

```
$ cd ivod-gui/static
$ bower init
$ bower install --save Polymer/polymer
$ bower install --save Polymer/core-elements
$ bower install --save Polymer/paper-elements

~/git/g0v-raw/ivod-gui$ sudo docker build -t test .
~/git/g0v-raw/ivod-gui$ sudo docker run -p 8080:8080 test
 * Running on http://0.0.0.0:8080/
```

Test 2014/09/26

```
$ uname -a
Linux ubuntu73 3.13.0-24-generic #47-Ubuntu SMP Fri May 2 23:30:00 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux

$ date
Fri Sep 26 17:43:19 CST 2014

$ pip install -r requirements.txt

$ python util.py -u 'http://ivod.ly.gov.tw/Play/VOD/76394/300K'
http://h264media02.ly.gov.tw:1935/vod/_definst_/mp4:1MClips/05c94266e7aa0e4db3a5855ca79d0940b078379004037ca3ff7bf629664a15217a943fd3a9a74f9e.mp4/manifest.f4m
[download] Downloading f4m manifest
[download] Destination: test.flv
[download] 100% of 89.82MiB in 01:49
None

$ ffmpeg -i test.flv
ffmpeg version 2.4.1-   http://johnvansickle.com/ffmpeg/    Copyright (c) 2000-2014 the FFmpeg developers
  built on Sep 24 2014 18:52:48 with gcc 4.8 (Debian 4.8.3-11)
  configuration: --enable-gpl --enable-version3 --disable-shared --disable-debug --enable-runtime-cpudetect --enable-libmp3lame --enable-libx264 --enable-libx265 --enable-libwebp --enable-libspeex --enable-libvorbis --enable-libvpx --enable-libfreetype --enable-fontconfig --enable-libxvid --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libtheora --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-gray --enable-libopenjpeg --enable-libopus --disable-ffserver --enable-libass --enable-gnutls --cc=gcc-4.8
  libavutil      54.  7.100 / 54.  7.100
  libavcodec     56.  1.100 / 56.  1.100
  libavformat    56.  4.101 / 56.  4.101
  libavdevice    56.  0.100 / 56.  0.100
  libavfilter     5.  1.100 /  5.  1.100
  libswscale      3.  0.100 /  3.  0.100
  libswresample   1.  1.100 /  1.  1.100
  libpostproc    53.  0.100 / 53.  0.100
  
[NULL @ 0x304e0c0] missing picture in access unit with size 33503
[h264 @ 0x304e0c0] missing picture in access unit with size 730
[h264 @ 0x304e0c0] missing picture in access unit with size 1385
....
[h264 @ 0x304e0c0] missing picture in access unit with size 1390
[h264 @ 0x304e0c0] missing picture in access unit with size 1470

Input #0, flv, from 'test.flv':
  Metadata:
    length          : 67365000
    timescale       : 90000
    sampletype      : mp4a
    audiochannels   : 2
    videoframerate  : 30
    aacaot          : 2
    avclevel        : 30
    avcprofile      : 66
    frameWidth      : 720
    frameHeight     : 480
    displayWidth    : 640
    displayHeight   : 480
    moovposition    : 93432751
  Duration: 00:12:28.52, start: 0.000000, bitrate: 1006 kb/s
    Stream #0:0: Video: h264 (Constrained Baseline), yuv420p(tv), 720x480 [SAR 8:9 DAR 4:3], 31.25 fps, 29.97 tbr, 1k tbn, 59.94 tbc
    Stream #0:1: Audio: aac, 48000 Hz, stereo, fltp
At least one output file must be specified
```