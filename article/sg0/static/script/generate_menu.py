# python=3.10.6
# coding=utf-8
'''
@File   generate_menu.py
@Time   2023/09/28
@Author TaylorGy 
@Site   https://github.com/taylorgy
@Desc   Scan all files in the [doc] folder, 
        generete [menu.html] with the file path
        and the title in the first line of each file.
'''
import os

root = "../../doc/"
list_file = os.listdir(root)[1:]

with open("menu.html", 'w', encoding='utf8') as menu:
    menu.write("<li> <a href=\"./doc/0000\">序章</a> </li>\n")
    for file in list_file:
        with open(os.path.join(root, file), 'r', encoding='utf8') as f:
            title = f.readline()[2:-1]
            # <li> <a href="./doc/0000"> Prologue </a> </li>
            li = "<li> <a href=\"./doc/" + file.split('.')[0] + "\">" + title + "</a> </li>\n"
            menu.write(li)
