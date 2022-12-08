import flet
from flet import *
from appmenu import appmenu
from top import top
from middle import middle


def main(page: flet.Page):
    # ekran xususiyatlari
    page.scroll = "adaptive"
    page.bgcolor = "#1B1B38"
    page.window_width = 800
    page.window_hidden = True
    # main qism
    page.add(top)
    for i in middle:
        page.add(i)
    page.add(appmenu)
    page.update()


flet.app(target=main, assets_dir="assets")
