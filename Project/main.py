from flet import * 
import flet
from login import Login

def main(page:Page):

    page.fonts = {
        "bahnschrift": "fonts/BAHNSCHRIFT.ttf"
    }
    page.theme_mode = 'dark'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.theme = Theme(color_scheme_seed=colors.PURPLE, font_family='bahnschrift')
    
    page.appbar = AppBar(
        title=Text("Billy"),
        leading= Icon(icons.PAYMENT_ROUNDED), 
        bgcolor= '#402F3F', 
        actions=[IconButton(icon=icons.MENU)])


    page.add(SafeArea(content= Login()))

flet.app(target=main,assets_dir='assets')
