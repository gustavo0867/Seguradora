from entidades.bem import inserir_bem, get_bens, Vida,Imóvel,Veículo
from entidades.seguro import Seguro, inserir_seguro, filtrar_seguros, get_seguros
from entidades.cliente import inserir_cliente, Cliente, get_clientes
from util.data import str_to_data
from entidades.endereço import Endereço


def imprimir_objetos(cabeçalho, objetos, filtros=None):
    if filtros == None:
        print('\n' + cabeçalho)
    else:
        print('\n' + cabeçalho + filtros)
    for índice, objeto in enumerate(objetos): print(str(índice + 1) + ' - ' + str(objeto))

def loop_opções_execução():
    print('Opções da Seguradora')
    sair_loop = False
    while not sair_loop:
        operação = ler_str\
        ('operação [C: Cadastrar / I: Imprimir / S: Selecionar / T: imprimir Todos / <ENTER>: Parar]',
        retornar=True)
        if operação == None: break
        elif operação in ('C', 'I'):
            opção_conteúdo = ler_str('[C: Clientes / B: Bens / S: Seguros / <ENTER>: retornar]',
            retornar=True)
            if opção_conteúdo == None: pass
            elif opção_conteúdo in 'C':
                if operação == 'C': loop_leitura_clientes()
                imprimir_objetos('Clientes cadastrados', get_clientes().values())
            elif opção_conteúdo == 'B':
                if operação == 'C': loop_leitura_bens()
                imprimir_objetos('Bens cadastrados', get_bens().values())
            elif opção_conteúdo == 'S':
                if operação == 'C': loop_leitura_seguros()
                imprimir_objetos('Seguros cadastrados', get_seguros())
        elif operação == 'S': loop_seleção_seguros()
        elif operação == 'T':
            imprimir_objetos('Bens cadastradas', get_bens().values())
            imprimir_objetos('Clientes cadastrados', get_clientes().values())
            imprimir_objetos('Seguros cadastrados', get_seguros())

def loop_leitura_clientes():
    sair_loop = False
    print('--- Leitura de Dados dos Clientes ---')
    while not sair_loop:
        cliente = ler_cliente()
        if cliente != None: inserir_cliente(cliente)
        else: print(' - ERRO : na leitura do cliente')
        sair_loop = ler_sair_loop('cadastro de clientes')

def loop_leitura_bens():
    sair_loop = False
    print('--- Leitura de Dados dos Bens ---')
    while not sair_loop:
        bem = ler_bem()
        if bem != None: inserir_bem(bem)
        else: print(' - ERRO : na leitura do bem')
        sair_loop = ler_sair_loop('cadastro de bem')

def loop_leitura_seguros():
    sair_loop = False
    print('--- Leitura de Dados dos Seguros ---')
    while not sair_loop:
        seguro = ler_seguro()
        if seguro != None:
            inserir_seguro(seguro)
        else: print(' - ERRO : na leitura do seguro')
        sair_loop = ler_sair_loop('cadastro de seguros')

def loop_seleção_seguros():
    sair_loop = False
    print('--- Seleção de Seguros Cadastrados ---')
    while not sair_loop:
        filtros, seguros_selecionados = selecionar_seguros(get_seguros())
        if filtros != None:
            imprimir_objetos('Seguros selecionados com ', seguros_selecionados, filtros)
        sair_loop = ler_sair_loop('seleção de seguros')

def ler_sair_loop(loop):
    try:
        sair = input('-- sair do loop de ' + loop + ' [S]: ')
        if sair == 'S': return True
    except IOError: pass
    return False




def ler_cliente():
    nome = ler_str('nome do cliente')
    if nome is None:
        return None
    rg = ler_str('RG do cliente')
    if rg is None:
        return None
    cpf = ler_str('CPF do cliente')
    if cpf is None:
        return None
    data_nascimento = ler_data('data de nascimento do cliente')
    if data_nascimento is None:
        return None
    sexo = ler_sexo()
    if sexo is None:
        return None
    endereco = ler_endereco()
    if endereco is None:
        return None
    return Cliente(nome, rg, cpf, data_nascimento, sexo, endereco)

def ler_bem():
    tempo_de_segurado = ler_int_positivo('tempo de segurado do bem (em anos)')
    if tempo_de_segurado is None:
        return None
    codigo = ler_str('código do bem')
    if codigo is None:
        return None
    tipo_bem = ler_tipo_bem()
    if tipo_bem is None:
        return None
    if tipo_bem == 'Veículo':
        nome = ler_str('nome do veículo')
        if nome is None:
            return None
        marca_veículo = ler_str('marca do veículo')
        if marca_veículo is None:
            return None
        modelo = ler_modelo()
        if modelo is None:
            return None
        carro0 = ler_bool('veículo novo (True/False)')
        if carro0 is None:
            return None
        return Veículo(codigo, tempo_de_segurado, nome, marca_veículo, modelo, carro0)
    elif tipo_bem == 'Imóvel':
        tipo = ler_str('tipo do imóvel')
        if tipo is None:
            return None
        num_comodos = ler_int_positivo('número de cômodos do imóvel')
        if num_comodos is None:
            return None
        imovel0 = ler_bool('imóvel novo (True/False)')
        if imovel0 is None:
            return None
        return Imóvel(codigo, tempo_de_segurado, tipo, num_comodos, imovel0)
    elif tipo_bem == 'Vida':
        idade = ler_int_positivo('idade do segurado')
        if idade is None:
            return None
        estado_civil = ler_str('estado civil do segurado')
        if estado_civil is None:
            return None
        fumante_vida = ler_bool('segurado é fumante (True/False)')
        if fumante_vida is None:
            return None
        return Vida(codigo, tempo_de_segurado, idade, estado_civil, fumante_vida)
    else:
        return None



def ler_seguro():
    cpf_cliente = ler_str('CPF do cliente')
    if cpf_cliente is None:
        return None
    try:
        cliente = get_clientes()[cpf_cliente]
    except KeyError:
        print("Cliente não cadastrado")
        return None
    inadimplencia = ler_bool('Cliente possui inadimplência')
    codigo_bem = ler_str('Código do bem (Veículo/Imóvel/Vida)')
    if codigo_bem is None:
        return None
    bem = get_bens().get(codigo_bem)
    if bem is None:
        print('Bem não cadastrado')
        return None
    data_inicio = ler_data('Data de início do seguro')
    if data_inicio is None:
        return None
    return Seguro(cliente, inadimplencia, bem, data_inicio)








def ler_tipo_bem():
    while True:
        entrada = input('Tipo do bem (Veículo/Imóvel/Vida): ').strip().capitalize()
        if entrada in ('Veículo', 'Imóvel', 'Vida'):
            return entrada
        print('Por favor, insira um tipo válido (Veículo, Imóvel ou Vida).')

def ler_modelo():
    while True:
        entrada = input('Modelo do veículo (SUV/Sedan/Hatch/Picape/Off-road): ').strip().lower()
        if entrada in ('suv', 'sedan', 'hatch', 'picape', 'off-road'):
            return entrada
        print('Por favor, insira um modelo válido.')

def ler_sexo():
    while True:
        entrada = input('Sexo (M/F): ').strip().upper()
        if entrada in ('M', 'F'):
            return entrada
        print('Por favor, insira M para masculino ou F para feminino.')

def ler_str(dado, filtro=False, retornar=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and (filtro or retornar): return None
        if len(string) > 0: return string
    except IOError: pass
    print('Erro na leitura do dado: ' + dado)
    return None

def ler_endereco():
    endereco = {}
    endereco['rua'] = ler_str('Rua')
    endereco['numero'] = ler_str('Número')
    endereco['bairro'] = ler_str('Bairro')
    endereco['cidade'] = ler_str('Cidade')
    endereco['estado'] = ler_str('Estado')
    endereco['cep'] = ler_str('CEP')
    return endereco

def ler_data(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [dd/mm/aaaa]: ')
        if len(string) == 0 and filtro: return None
        data = str_to_data(string)
        if data is not None: return data
    except IOError:
        pass
    print('Erro na leitura da data: ' + dado)
    return None



def ler_int_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro: return None
        int_positivo = int(string)
        if int_positivo > 0: return int_positivo
    except ValueError: pass
    print('Erro na leitura/conversão do inteiro positivo: ' + dado)
    return None

def ler_bool(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [S/N]: ')
        string = string.upper()
        if len(string) == 0 and filtro: return None
        if string == 'S': return True
        elif string == 'N': return False
    except ValueError: pass
    print('Erro na leitura do booleano: ' + dado)
    return None





def selecionar_seguros(seguros):
    filtros = 'Filtros: '
    data_minima_cadastro_seguro = ler_data('Data mínima do cadastro do seguro', filtro=True)
    if data_minima_cadastro_seguro is not None:
        filtros += '\n-- Data mínima do cadastro do seguro: ' + str(data_minima_cadastro_seguro)
    cidade_cliente = ler_str('Cidade do cliente', filtro=True)
    if cidade_cliente is not None:
        filtros += '\n-- Cidade do cliente: ' + cidade_cliente
    tempo_minimo_segurado_bem = ler_int_positivo('Tempo mínimo que o bem é segurado', filtro=True)
    if tempo_minimo_segurado_bem is not None:
        filtros += '\n-- Tempo mínimo que o bem é segurado: ' + str(tempo_minimo_segurado_bem)
    marca_veiculo = ler_str('Marca do veículo', filtro=True)
    if marca_veiculo is not None:
        filtros += '\n-- Marca do veículo: ' + marca_veiculo
    tipo_imovel = ler_str('Tipo de imóvel', filtro=True)
    if tipo_imovel is not None:
        filtros += '\n-- Tipo de imóvel: ' + tipo_imovel
    fumante_vida = ler_bool('Cliente é fumante na apólice de vida', filtro=True)
    if fumante_vida == True:
        filtros += '\n-- Cliente fumante na apólice de vida'
    elif fumante_vida == False:
        filtros += '\n-- Cliente não é fumante na apólice de vida'

    seguros_selecionados = filtrar_seguros(data_minima_cadastro_seguro, cidade_cliente,
                                           tempo_minimo_segurado_bem, marca_veiculo,
                                           tipo_imovel, fumante_vida)
    return filtros, seguros_selecionados
