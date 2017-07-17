# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数，接受三个参数表示歌手名和专辑名和歌曲数，歌曲数为可选形参，返回字典
def make_album(singer, album, quantity=''):
    music_album = {'Singer': singer.title(), 'Album': album.title()}
    if quantity:
        music_album['Quantity'] = quantity
    return music_album
#利用循环提示用户输入信息,并提示退出条件
while True:
    print('\nPlease tell me your favorite singer and album:')
    print("(enter 'q' at any time to quit)")
    singer = input('Singer: ')
    if singer == 'q':
        break
    album = input('Album: ')
    if album == 'q':
        break
    #调用函数并打印返回的字典
	album_dict = make_album(singer, album)
    print(album_dict)
