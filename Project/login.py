import flet
from flet import *

class InputField(TextField):
    
    def __init__(self, hint_text, label , border_color):
        super().__init__()
        
        self.hint_text = hint_text
        self.label = label
        self.border_color = border_color

    def build (self):
        return TextField(
            hint_text= self.hint_text,
            border_color = self.border_color,
            label = self.label,

        )

class InputButton(FilledButton):

    def __init__(self, text, icon):
        super().__init__()
        self.text = text
    
    def build(self):


        return FilledButton(
            text= self.text,
            icon= self.icon,
        )


class Login(UserControl):
    
    def __init__(self):
        super().__init__()
    

    def build(self):

        self.username =  InputField('USERNAME','USERNAME', colors.PURPLE_100)
        self.key = InputField('PASSWORD','PASSWORD', colors.PURPLE_100)


        self.buttons = Container(content=Row(controls=[
            InputButton('LOGIN',icons.ARROW_FORWARD_IOS_ROUNDED),
            InputButton('SIGN UP', icons.PERSON_ADD_ALT_ROUNDED)
            ],
            alignment=MainAxisAlignment.CENTER, 
            vertical_alignment=CrossAxisAlignment.CENTER),
            margin=20
            )
        

        self.column = Column(controls=[
            Icon(icons.ACCOUNT_CIRCLE_ROUNDED, size = 60),
            Text('LOGIN', size=30, color=colors.PURPLE_100),
            self.username,
            self.key,
            self.buttons

        ],alignment=MainAxisAlignment.CENTER,
        horizontal_alignment= CrossAxisAlignment.CENTER,
        spacing=20)

        return Column(controls=[Card(
            content=Container(
                content=self.column,
                margin= margin.symmetric(20,20),
                ),
            ),],
            alignment= MainAxisAlignment.CENTER,
            horizontal_alignment= CrossAxisAlignment.CENTER,
            spacing= 30)