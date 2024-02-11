from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.clearcolor = (100/255, 0, 1, 1)
Window.size = (400, 630)

class MainWindow(Screen):
    pass
    
class SecondWindow(Screen):
    pass
    
class ErrorWindow(Screen):
    pass

class PythonWindow(Screen):
    pass
    
class PhpWindow(Screen):
    pass
    
class SqlWindow(Screen):
    pass
    
class PerlWindow(Screen):
    pass
    
class HtmlWindow(Screen):
    pass
    
class CssWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_string('''
WindowManager:
    MainWindow:
    SecondWindow:
    ErrorWindow:
    PythonWindow:
    PhpWindow:
    SqlWindow:
    PerlWindow:
    HtmlWindow:
    CssWindow:

<MainWindow>:
    name: "main"
    GridLayout:
        cols:1
        GridLayout:
            rows:4
            Image:
                source:'images/codingIcon.png'
            Label:
                text:'Learn Coding'
                font_size:30
            Label:
                text: 'Please Enter Password'
                size_hint: .1, .3
            TextInput:
                id: password
                multiline:False
                size_hint: .1, .3
                password:True
        Button:
            text:'Login'
            size_hint: .1, .1
            on_release:
                app.root.current = 'second' if password.text == "BabaIsCool" else 'error'
                root.manager.transition.direction = "up"

<SecondWindow>:
    name: 'second'
    GridLayout:
        cols:1
        GridLayout:
            rows:2
            Image:
                source:'images/codingIcon2.png'
            Label:
                text:'Welcome Programmer'
        GridLayout:
            cols:2
            rows:3
            Button:
                text:'python'
                size_hint: .1, .1
                on_release:
                    app.root.current = 'py'
                    root.manager.transition.direction = 'right'
            Button:
                text:'perl'
                size_hint: .1, .1
                on_release:
                    app.root.current = 'perl'
                    root.manager.transition.direction = 'left'
            Button:
                text:'php'
                size_hint: .1, .1
                on_release:
                    app.root.current = 'php'
                    root.manager.transition.direction = 'right'
            Button:
                text:'sql'
                size_hint: .1, .1
                on_release:
                    app.root.current = 'sql'
                    root.manager.transition.direction = 'left'
            Button:
                text:'html5'
                size_hint: .1, .1
                on_release:
                    app.root.current = 'html'
                    root.manager.transition.direction = 'right'
            Button:
                text:'css3'
                size_hint: .1, .1
                on_release:
                    app.root.current = 'css'
                    root.manager.transition.direction = 'left'
        Button:
            text:'Back'
            size_hint: .1, .3
            on_release:
                app.root.current = 'main'
                root.manager.transition.direction = "down"

<ErrorWindow>:
    name: 'error'
    GridLayout:
        cols: 1
        rows: 3
        Image:
            source:"images/errorIcon.png"
        Label:
            text:'Password Incorrect'
            font_size: 30
        Button:
            text:'Try Again'
            size_hint: .1, .3
            on_release:
                app.root.current = 'main'

<PythonWindow>:
    name: 'py'
    GridLayout:
        cols: 1
        rows: 3
        Image:
            source:"images/pythonIcon.png"
        Label:
            text:'Learn Python'
            font_size: 30
        Button:
            text:'Back'
            size_hint: .1, .3
            on_release:
                app.root.current = 'second'

<PerlWindow>:
    name: 'perl'
    GridLayout:
        cols: 1
        rows: 3
        Image:
            source:"images/perlIcon.png"
        Label:
            text:'Learn Perl'
            font_size: 30
        Button:
            text:'Back'
            size_hint: .1, .3
            on_release:
                app.root.current = 'second'

<PhpWindow>:
    name: 'php'
    GridLayout:
        cols: 1
        rows: 3
        Image:
            source:"images/phpIcon.png"
        Label:
            text:'Learn PHP'
            font_size: 30
        Button:
            text:'Back'
            size_hint: .1, .3
            on_release:
                app.root.current = 'second'

<SqlWindow>:
    name: 'sql'
    GridLayout:
        cols: 1
        rows: 3
        Image:
            source:"images/sqlIcon.png"
        Label:
            text:'Learn SQL'
            font_size: 30
        Button:
            text:'Back'
            size_hint: .1, .3
            on_release:
                app.root.current = 'second'

<HtmlWindow>:
    name: 'html'
    GridLayout:
        cols: 1
        rows: 3
        Image:
            source:"images/htmlIcon.png"
        Label:
            text:'Learn HTML5'
            font_size: 30
        Button:
            text:'Back'
            size_hint: .1, .3
            on_release:
                app.root.current = 'second'

<CssWindow>:
    name: 'css'
    GridLayout:
        cols: 1
        rows: 3
        Image:
            source:"images/cssIcon.png"
        Label:
            text:'Learn CSS'
            font_size: 30
        Button:
            text:'Back'
            size_hint: .1, .3
            on_release:
                app.root.current = 'second'
''')

class KivyProject(App):
    def build(self):
        self.title = "Abed's Apps"
        return kv

if __name__ == '__main__':
    KivyProject().run()