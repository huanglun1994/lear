# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
r = requests.get(url)
print('Status code: ', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print('Total repositories: ', response_dict['total_count'])
print('Total items: ', len(response_dict['items']))

# 研究有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {}
    plot_dict['value'] = repo_dict['stargazers_count']
    if repo_dict['description']:
        plot_dict['label'] = repo_dict['description']
    elif not repo_dict['description']:
        plot_dict['label'] = 'No description'
    plot_dict['xlink'] = repo_dict['html_url']
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 16
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Java Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('java_repos.svg')
