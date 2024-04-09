bens = {}

def get_bens():   return bens

def set_bens(bens1):
    global bens
    bens = bens1

def inserir_bem(bem):
    codigo_bem = bem.codigo
    if codigo_bem not in bens.keys():
        bens[codigo_bem] = bem
    else:
        print('Bem já cadastrado')

class Bem:
    def __init__(self, tempo_de_segurado, codigo):
        self.tempo_de_segurado = tempo_de_segurado
        self.codigo = codigo

    def __str__(self):
        return 'Código: ' + str(self.codigo) + ' -- Tempo de segurado do bem: ' + str(self.tempo_de_segurado) + ' ANOS '

class Veículo(Bem):
    def __init__(self, codigo,tempo_de_segurado, nome, marca_veículo, modelo, carro0):
        super().__init__(tempo_de_segurado, codigo)
        self.nome = nome
        self.marca_veículo = marca_veículo
        self.modelo = modelo if modelo in ('suv', 'sedan', 'hatch', 'picape', 'off-road') else 'indefinido'
        self.carro0 = carro0


    def __str__(self):
        return 'VEÍCULO -- '+super().__str__() +'-- Nome do carro: ' + self.nome + ' -- marca do carro: ' + self.marca_veículo + ' -- modelo do carro: ' + self.modelo + self.__to_str_carro0__()

    def __to_str_carro0__(self):
        return ' --NOVO' if self.carro0 else ''

class Imóvel(Bem):
    def __init__(self, codigo,tempo_de_segurado, tipo, num_comodos, imovel0):
        super().__init__(tempo_de_segurado, codigo)
        self.tipo = tipo if tipo in ('casa', 'apartamento', 'terreno', 'comercial') else 'indefinido'
        self.num_comodos = num_comodos
        self.imovel0 = imovel0

    def __str__(self):
        return 'IMÓVEL -- '+super().__str__() + '-- Tipo do imóvel: ' + self.tipo + ' -- Número de Cômodos: ' + str(
            self.num_comodos) + self.__to_str_imovel0__()

    def __to_str_imovel0__(self):
        return ' --NOVO' if self.imovel0 else ''

class Vida(Bem):
    def __init__(self, codigo, tempo_de_segurado, idade, estado_civil, fumante_vida):
        super().__init__(tempo_de_segurado, codigo)
        self.idade = idade
        self.estado_civil = estado_civil
        self.fumante_vida = fumante_vida

    def __str__(self):
        return 'VIDA -- '+super().__str__() + '-- Idade: ' + str(self.idade) + ' anos' + ' -- Estado civil: ' + self.estado_civil + self.__to_str_fumante__()

    def __to_str_fumante__(self):
        return ' -- Fumante' if self.fumante_vida else ''