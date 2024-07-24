clientes = {}

def get_clientes(): return clientes

def set_clientes(clientes1):
    global clientes
    clientes = clientes1

def inserir_cliente(novo_cliente):
    cpf_cliente = novo_cliente.cpf
    if cpf_cliente not in clientes.keys():
        clientes[cpf_cliente] = novo_cliente
    else: print('Cliente já cadastrado')

class Cliente:

    def __init__(self, nome, rg, cpf, data_nascimento, sexo, endereço):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo if sexo in ('M', 'F') else 'indefinido'
        self.endereço = endereço

    def __str__(self):
        return self.nome + ' - RG:' + self.rg + ' - CPF:' + self.cpf + ' - nascimento:'\
        + str(self.data_nascimento) + ' - sexo:' + self.__to_str_sexo__()\
        + '    \n - residente em: ' + str(self.endereço)
    def __to_str_sexo__(self):
        if self.sexo == 'M': return 'masculino'
        elif self.sexo == 'F': return 'feminino'
        else: return 'indefinido'
