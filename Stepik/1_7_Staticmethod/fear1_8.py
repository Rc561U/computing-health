from string import ascii_lowercase, digits


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self,login,size=10):
        self.check_name(login)
        self.login = login
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.login}: <input type='text' size={self.size} />"


    @classmethod
    def check_name(cls, name):
        
        if not 3 <= len(name) <= 50:
            raise ValueError("некорректное поле name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")
         
class PasswordInput:    
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    def __init__(self,password,size=10):
        self.check_name(password)
        self.password = password
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.password}: <input type='text' size={self.size} />"

    @classmethod
    def check_name(cls, name):
        
        if not 3 <= len(name) <= 50:
            raise ValueError("некорректное поле name")
        if not set(name) < set(cls.CHARS_CORRECT):
            raise ValueError("некорректное поле name")

login = FormLogin(TextInput("Лоujhg"), PasswordInput("Пь"))
html = login.render_template()