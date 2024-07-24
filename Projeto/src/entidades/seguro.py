from entidades.cliente import get_clientes, clientes
from entidades.bem import get_bens, Veículo,Imóvel,Vida

seguros = []

def get_seguros(): return seguros

def set_seguros(seguros1):
    global seguros
    seguros = seguros1

def inserir_seguro(seguro):
    if seguro not in seguros:seguros.append(seguro)
    else: print('visitação já cadastrada --- ' + str(seguro))

def filtrar_seguros(data_minima_cadastro_seguro=None, cidade_cliente = None, tempo_minimo_segurado_bem=None,
                       marca_veículo=None, tipo_imovel = None, fumante_vida = None, ):

    seguros_selecionados = []
    for seguro in seguros:

        if data_minima_cadastro_seguro is not None and data_minima_cadastro_seguro > seguro.data_início:
            continue
        if cidade_cliente != None and seguro.cliente.endereço.cidade != cidade_cliente: continue
        if tempo_minimo_segurado_bem is not None and  tempo_minimo_segurado_bem > seguro.codigo.tempo_de_segurado   :
            continue


        if isinstance(seguro.codigo, Veículo) and marca_veículo is not None \
                and seguro.codigo.marca_veículo  != marca_veículo:
            continue

        if isinstance(seguro.codigo, Imóvel) and tipo_imovel is not None \
                and seguro.codigo.tipo  != tipo_imovel:
            continue

        if isinstance(seguro.codigo, Vida) and fumante_vida is not None \
                and seguro.codigo.fumante_vida  != fumante_vida:
            continue



        seguros_selecionados.append(seguro)
    return  seguros_selecionados

class Seguro:
    def __init__(self, cliente, inadimplência, bem, data_início):
        self.cliente = cliente
        self.inadimplência = inadimplência
        self.codigo = bem
        self.data_início = data_início

    def __to_str_inadimplência__(self):
        if self.inadimplência:
            return ' --Cliente com Inadimplência'
        else:
            return ''

    def __str__(self):
        seguro_str = 'Cadastro da Cliente' if self.cliente.sexo == 'F' else 'Cadastro do Cliente'
        seguro_str += ': ' + str(self.cliente) + '\n - com o bem: ' + str(self.codigo)  +  '\n - data início: ' + str(self.data_início) + ' ' + self.__to_str_inadimplência__()

        return seguro_str

    def __eq__(self, seguro):
        if str(self) == str(seguro):
            return True
        else:
            return False
