# -*- coding: utf-8 -*-
current_users = ['admin', 'huanglun', 'wangdi', 'xiaoming', 'xiaohong']
new_users = ['Huanglun', 'Wangdi', 'ranming', 'yandong', 'maning']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry, you must choose another name again.')
    else:
        print("This name hasn't been used, you can make it.")