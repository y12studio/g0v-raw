#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# modify from https://github.com/billy3321/ivod-download-client/blob/master/ivod_single_downloader.py
#
import os, urllib, urllib2, cookielib, sys, random, time, datetime, subprocess
from BeautifulSoup import BeautifulSoup, SoupStrainer
from optparse import OptionParser
from youtube_dl import YoutubeDL
from youtube_dl.downloader import get_suitable_downloader
from youtube_dl.downloader import F4mFD

reload(sys)
sys.setdefaultencoding('utf-8')
currect_time = 0

def init_cookie():
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    reset_cookie()

def reset_cookie():
    global currect_time
    #if time lagger then 15 min, will reset.
    if time.time() - currect_time > 900:
        http_header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 'Host': 'ivod.ly.gov.tw'}
        req = urllib2.Request('http://ivod.ly.gov.tw/', None, http_header)
        try:
            web = urllib2.urlopen(req)
            result = web.read()
            currect_time = time.time()
        except:
            sys.stderr.write('reset cookie error\n')
            return False
        #print result

"""
$ python util.py -u 'http://ivod.ly.gov.tw/Play/VOD/76394/300K'
http://h264media02.ly.gov.tw:1935/vod/_definst_/mp4:1MClips/05c94266e7aa0e4db3a5855ca79d0940b078379004037ca3ff7bf629664a15217a943fd3a9a74f9e.mp4/manifest.f4m
"""
def download_from_url(url):
    http_header = {'Referer': 'http://ivod.ly.gov.tw/Committee', 
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)', 
        'Host': 'ivod.ly.gov.tw',
        'Connection': 'keep-alive'}

    if 'http://ivod.ly.gov.tw/Play/' not in url:
        sys.stderr.write('URL error')
        sys.exit(1)

    url = url.replace('300K', '1M')
    req = urllib2.Request(url, None, http_header)
    try:
        web = urllib2.urlopen(req)
    except:
        sys.stderr.write('download_from_url web error')
        reset_cookie()
        return False
    #print web.getcode()
    if web.getcode() == 200:
        html_result = web.read()
        #print html_result
        xml = BeautifulSoup(html_result)
        text_block = xml.find('div', {'class': 'movie_box clearfix'}).find('div', {'class':'text'})
        if 'VOD' in url:
            meet = text_block.find('h4').text.replace(u'會議別 ：', u'').replace(u'委員會', u'')
            name = text_block.findAll('p')[1].text.replace(u'委  員  名  稱：', u'')
            date = text_block.findAll('p')[4].text.replace(u'會  議  時  間：', u'').split(' ')[0]
            filename = '%s %s %s' % (date, meet, name)
        elif 'FULL' in url:
            meet = text_block.find('h4').text.replace(u'會議別 ：', u'').replace(u'委員會', u'')
            date = text_block.findAll('p')[1].text.replace(u'會  議  時  間：', u'').split(' ')[0]
            filename = '%s %s' % (date, meet)
        div_movie = xml.find('div', {'class': 'movie'})
        if not div_movie:
            div_movie = xml.find('div', {'class': 'movie_large'})
        #print div_movie
        if div_movie:
            #print div_movie
            script_text = div_movie.find('script').text
            script_text = script_text.replace("readyPlayer('http://ivod.ly.gov.tw/public/scripts/','", '')
            script_text = script_text.replace("');", '')
            #print script_text
            return script_text
    else:
        sys.stderr.write('get_movie_url content error')
        return False

def download_video(url,filepath):
    ydl = YoutubeDL()
    info = {'url':url,'protocol':'http'}
    f4mFD = F4mFD(ydl,{})
    #dl = F4mFD()
    result = f4mFD.download(filepath, info)
    #return json.dumps(result)

def main_cli():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-u", "--url", dest="url",
                      help='IVOD Url')
    (options, args) = parser.parse_args()

    reset_cookie()
    if not options.url:
        print 'Please input url.'
        sys.exit(1)
    f4murl = download_from_url(options.url)
    print(f4murl)
    ydlinfo = download_video(f4murl,u'testdata/test.flv')
    print(ydlinfo)

if __name__ == '__main__':
    pass
