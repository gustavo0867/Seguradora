from util.data import Data
from entidades.endereço import Endereço
from entidades.bem import inserir_bem, get_bens, Vida,Imóvel,Veículo, set_bens
from entidades.cliente import inserir_cliente, Cliente, get_clientes, set_clientes
from entidades.seguro import inserir_seguro, get_seguros,set_seguros
from util.persistência_arquivo import carregar_arquivo, salvar_arquivo
from interfaces.interface_textual import loop_opções_execução

nome_arquivo ='seguradora'

def salvar_aplicação():
    seguradora = []
    seguradora.append(get_clientes())
    seguradora.append(get_bens())
    seguradora.append(get_seguros())
    salvar_arquivo(nome_arquivo, objetos=seguradora)

def recuperar_aplicação():
    bem = carregar_arquivo(nome_arquivo)
    if bem != None:
        set_clientes(bem[0])
        set_bens(bem[1])
        set_seguros(bem[2])

if __name__ == '__main__':
    recuperar_aplicação()
    loop_opções_execução()
    salvar_aplicação()








