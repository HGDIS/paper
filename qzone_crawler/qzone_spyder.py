# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 09:56:07 2017

@author: youth
"""
import requests
import json  
import math  

COOK={"Cookie": ""}

#构造请求图片列表的url
def get_photo_list(album_id,start):
    photos =[]
    url = 'https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo?g_tk=1770349299&callback=shine7_Callback&t=984959454&mode=0&idcNum=4&hostUin=xxx&topicId=' + album_id + '&noTopic=0&uin=xxx&pageStart=' + str(start) + '&pageNum=500&skipCmtCount=0&singleurl=1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset=utf-8'
    content = requests.get(url, cookies=COOK).content
    content = json.loads(content.split('(')[1].split(')')[0])
    result = content['data']['photoList']
    for photo in result:
        photo_url = photo['url']
        photos.append(photo_url)
    return photos
          
album_url='https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/fcg_list_album_v3?g_tk=1770349299&callback=shine0_Callback&t=836333356&hostUin=xxx&uin=xxx&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&format=jsonp&notice=0&filter=1&handset=4&pageNumModeSort=40&pageNumModeClass=15&needUserInfo=1&idcNum=4&callbackFun=shine0&_=1525439830577'
album_content=requests.get(album_url, cookies=COOK).content
album_content=album_content.split('(')[1].split(')')[0]
content=json.loads(album_content)

#相册信息
album_detail=content['data']['albumListModeSort']

#请求每一个相册的图片列表，返回json，每一次图片列表最多包含500个图片
#所有图片的url
photo_url = []
for album in album_detail:
    album_id = album['id']
    album_num = album['total']
    page_num = math.ceil(float(album_num)/500)
    photo_list = []
    for i in range(int(page_num)):
        photos = get_photo_list(album_id, i*500)
        photo_list.extend(photos)
    photo_url.append(photo_list)
    
for i in photo_url:
    print i[0]        
##for image in url:
# #   urllib.urlretrieve(image, 'D:\\images\\%s.jpg' %x)
# #   x=x+1
#    
