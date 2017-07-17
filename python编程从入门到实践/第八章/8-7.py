# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数，接受三个参数表示歌手名和专辑名和歌曲数，歌曲数为可选形参，返回字典
def make_album(singer, album, quantity=''):
    music_album = {'Singer': singer.title(), 'Album': album.title()}
    if quantity:
        music_album['Quantity'] = quantity
    return music_album
#调用函数三次，并指定一次歌曲数,打印返回值
print(make_album('han hong', 'tian liangle'))
print(make_album('zhou jielun', 'mo jiezuo'))
print(make_album('chen yixun', 'tao tai', 12))