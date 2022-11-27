class LoginModel(object):
    # def __init__(self):
    #     self.usuario = "alejandro.gonzalez"
    #     self.password = "hola1234"

    @classmethod
    def revisarCredenciales(cls, usr: str, pswd: str):
        if usr == "alejandro.gonzalez":
            if pswd == "hola1234":
                return True

        return False
