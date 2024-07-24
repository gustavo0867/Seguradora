from datetime import date


def str_to_data(data_str):
    dia, mês, ano = data_str.split('/')
    return Data(int(dia), int(mês), int(ano))

class Data:


    def __init__(self, dia, mês, ano):
        self.dia = dia
        self.mês = mês
        self.ano = ano

    def __str__(self):
        if self.dia < 10:
            data_str = '0' + str(self.dia)
        else:
            data_str = str(self.dia)
        if self.mês < 10:
            data_str += "/0" + str(self.mês) + "/"
        else:
            data_str += "/" + str(self.mês) + "/"
        data_str += str(self.ano)
        return data_str

    def __eq__(self, data):
        if str(self) == str(data): return True
        return False

    def __ne__(self, data):
        return not self == data

    def __gt__(self, data):
        if self.ano > data.ano:
            return True
        elif self.ano < data.ano:
            return False
        if self.mês > data.mês:
            return True
        elif self.mês < data.mês:
            return False
        if self.dia > data.dia:
            return True
        elif self.dia < data.dia:
            return False
        return False

    def __lt__(self, data):
        if self.ano < data.ano:
            return True
        elif self.ano > data.ano:
            return False
        if self.mês < data.mês:
            return True
        elif self.mês > data.mês:
            return False
        if self.dia < data.dia:
            return True
        elif self.dia > data.dia:
            return False
        return False

    def __ge__(self, data):
        if self < data:
            return False
        else:
            return True

    def __le__(self, data):
        if self > data:
            return False
        else:
            return True

    def calcular_idade(self):
        dia_atual_str, mês_atual_str, ano_atual_str = date.today().strftime("%d/%m/%Y").split('/')
        dia_atual, mês_atual, ano_atual = int(dia_atual_str), int(mês_atual_str), int(ano_atual_str)
        idade = ano_atual - self.ano
        if mês_atual < self.mês or (mês_atual == self.mês and dia_atual < self.dia): idade -= 1
        return idade
