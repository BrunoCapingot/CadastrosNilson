from Factory.Processo import Processo
import re
import pandas as pd
from collections import Counter


class CadastroDadosBancoGerais2023Padronizada(Processo):
    def __init__(self, nome, prioridade):
        super().__init__(nome, prioridade)
        self.data_base_table_cvs_relatorio_geral_clientes_2023 = None
        self.querry_list = None
        self.data_list_dict = None
        self.data_list_padronizado = None

    def executar(self, Model, View):
        self.data_base_table_cvs_relatorio_geral_clientes_2023 = Model.get_table_cvs_relatorio_geral_clientes_2023()
        self.querry_list = list()
        self.data_list_dict = list()
        self.data_list_padronizado = list()
        for row in self.data_base_table_cvs_relatorio_geral_clientes_2023:
            index = row[0]
            if row != 'parada':
                valor_subs = row[-3]
                if row[-3] == 'nan' or row[-3] == '':
                    valor_subs = 0
                self.data_list_dict.append(dict(cliente_codigo=[str(row[1])],cliente_numero_de_contrato=[str(row[2])],cliente_identificador_unidade=[str(row[3]).replace(' ', '')],cliente_nome=str(row[4]),cliente_cpf_cnpj=str(row[5]),cliente_endereco=str(row[6]),cliente_valor_venda=[str(row[7])],cliente_status_venda=[str(row[8])],cliente_total_de_parcelas_pagas=[str(row[9])],cliente_valor_recebido=[valor_subs],cliente_qtd_de_parcelas_a_pagar=[str(row[11])],cliente_saldo_devedor=[str(row[12])]))
        dt_dict = self.separar_elementos(Model=Model)
        self.concatenar_clientes_com_unidades(dt_dict_list=dt_dict['lista_dois_dado'])


    def concatenar_clientes_com_unidades(self,dt_dict_list:dict)->None:
        list_dicionario_final = [{'cliente_nome': ''}]
        while dt_dict_list.__len__():
            cliente_nao_encontrado = True
            dt = dt_dict_list.pop()
            for index, dicionario_cliente in enumerate(list_dicionario_final):
                nome_cliente = dt['cliente_nome']
                contrato_cliente = dt['cliente_numero_de_contrato']
                if dt['cliente_nome'] == dicionario_cliente['cliente_nome']:
                    data = list_dicionario_final[index]
                    list_dicionario_final.append(dt)
                    cliente_nao_encontrado = False
                    pass
            if cliente_nao_encontrado:
                    list_dicionario_final.append(dt)




        #dict_de_colecoes = self.colecao_de_elementos()
        #list_dict_clientes_mais_de_uma_unidade = self.clientes_com_varias_unidades(dict_de_colecoes=dict_de_colecoes)
        #list_dict_clientes_uma_unidade = self.clientes_com_uma_unidades(dict_de_colecoes=dict_de_colecoes)
        #self.soma_unitarios_e_duplicados(list_dict_clientes_uma_unidade=list_dict_clientes_uma_unidade, list_dict_clientes_mais_de_uma_unidade=list_dict_clientes_mais_de_uma_unidade)



        input('calma jovem')

    def separar_elementos(self, Model):
        lista_um_dado = list()
        lista_dois_dado = list()
        for dicionario in self.data_list_dict:
            cliente_nome = dicionario['cliente_nome']
            dado = Model.get_cliente_nome_geral_2023(cliente_nome)
            if dado.__len__() != 1:
                dado = dado.pop()
                for index, cliente_nome_lista_dado in enumerate(lista_dois_dado):
                    pass
                lista_dois_dado.append(dict(cliente_codigo=dado[1], cliente_numero_de_contrato=dado[2],cliente_identificador_unidade=dado[3],cliente_nome=dado[4],cliente_cpf_cnpj=dado[5],cliente_endereco=dado[6],cliente_valor_venda=dado[7],cliente_status_venda=dado[8],cliente_total_de_parcelas_pagas=dado[7],cliente_valor_recebido=dado[8],cliente_valor_quantidade_parcelas_a_pagar=dado[9],cliente_saldo_devedor=dado[10]))

            elif dado.__len__() == 1:
                dado = dado.pop()
                lista_um_dado.append(dict(cliente_codigo=dado[1],cliente_numero_de_contrato=dado[2],cliente_identificador_unidade=dado[3],cliente_nome=dado[4],cliente_cpf_cnpj=dado[5],cliente_endereco=dado[6],cliente_valor_venda=dado[7],cliente_status_venda=dado[8],cliente_total_de_parcelas_pagas=dado[7],cliente_valor_recebido=dado[8],cliente_valor_quantidade_parcelas_a_pagar=dado[9],cliente_saldo_devedor=dado[10]))
        return dict(lista_um_dado=lista_um_dado,lista_dois_dado=lista_dois_dado)


    def soma_unitarios_e_duplicados(self,list_dict_clientes_uma_unidade,list_dict_clientes_mais_de_uma_unidade):
        valor_a_ser_somado = 0
        while list_dict_clientes_mais_de_uma_unidade.__len__()!=0:
            data = list_dict_clientes_mais_de_uma_unidade.pop()
            valor_a_ser_somado += float(data['cliente_valor_recebido'][0])
        print(valor_a_ser_somado)
        while list_dict_clientes_uma_unidade.__len__()!=0:
            data = list_dict_clientes_uma_unidade.pop()
            valor_recebido = data['cliente_valor_recebido'][0]
            valor_a_ser_somado += float(valor_recebido)
        print(valor_a_ser_somado)

    def clientes_com_uma_unidades(self,dict_de_colecoes):
        list_dict = list()
        while dict_de_colecoes['lista_de_elementos_unitarios'].__len__() != 0:
            codigo_unitario = dict_de_colecoes['lista_de_elementos_unitarios'].pop()
            for dict_list in self.data_list_dict:
                cliente_codigo = dict_list['cliente_codigo'][0]
                if codigo_unitario == cliente_codigo:
                    list_dict.append(dict_list)
        return list_dict

    def clientes_com_varias_unidades(self,dict_de_colecoes):
        list_dict = list()
        while dict_de_colecoes['lista_de_elementos_duplicados'].__len__()!=0:
            codigo_duplicado = dict_de_colecoes['lista_de_elementos_duplicados'].pop()
            for dict_list in self.data_list_dict:
                cliente_codigo = dict_list['cliente_codigo'][0]
                if codigo_duplicado == cliente_codigo:
                    list_dict.append(dict_list)
        return list_dict





    def colecao_de_elementos(self):
        lista_de_elementos_duplicados = list()
        lista_de_elementos_unitarios = list()
        todos_os_elementos = Counter([dict_cliente['cliente_codigo'][0] for dict_cliente in self.data_list_dict])
        for dict_cliente in self.data_list_dict:
            codigo_principal = dict_cliente['cliente_codigo'][0]
            if todos_os_elementos[codigo_principal] > 1:
                lista_de_elementos_duplicados.append(codigo_principal)
            elif todos_os_elementos[codigo_principal] == 1:
                lista_de_elementos_unitarios.append(codigo_principal)
        return dict(lista_de_elementos_duplicados=lista_de_elementos_duplicados,lista_de_elementos_unitarios=lista_de_elementos_unitarios)

    def busca_linear(self, data_list_dict: list, chave_de_busca: str) -> None:
        elementos_duplicados = list()
        i = 0
        while i < data_list_dict.__len__():
            nome_cliente = data_list_dict[i]['cliente_nome']
            if nome_cliente == chave_de_busca:
                elementos_duplicados.append(data_list_dict[i])
            i += 1
        print(elementos_duplicados)

    def concatenar_elementos_duplicados(self,lista_elementos_duplicados:list)->None:
        pass

    def somar_posicoes_em_string_padrao_banco(self, data_para_adicionar, data_list_local_add):
        data_um = data_list_local_add
        data_dois = data_para_adicionar
        # valor = float(data_um) + float(data_dois)
        return ''

    def tratar_lista_padronizada_por_contrato(self, querry_list: list) -> list:
        for dado in self.data_list_padronizado:
            pos = self.data_list_padronizado.index(dado)
            if dado['cliente_numero_de_contrato'] == ['0']:
                self.data_list_padronizado.remove(dado)
            elif dado['cliente_numero_de_contrato'] != ['0']:
                print(dado)
                querry_list.append(
                    f"insert into table_cvs_relatorio_geral_clientes_2023_padronizada (cliente_codigo,cliente_numero_contrato,cliente_identificador_unidade,cliente_nome,cliente_cpf_cnpj,cliente_endereco,cliente_valor_venda,cliente_status_venda,cliente_total_de_parcelas_pagas,cliente_valor_recebido,qtd_parcelas_a_pagar,saldo_devedor) values ('{self.data_list_padronizado[pos]['cliente_codigo'].pop()}','{self.data_list_padronizado[pos]['cliente_numero_de_contrato'].pop()}','{self.data_list_padronizado[pos]['cliente_identificador_unidade'].pop()}','{self.data_list_padronizado[pos]['cliente_nome']}','{self.data_list_padronizado[pos]['cliente_cpf_cnpj']}','{self.data_list_padronizado[pos]['cliente_endereco']}','{self.data_list_padronizado[pos]['cliente_valor_venda'].pop()}','{self.data_list_padronizado[pos]['cliente_status_venda'].pop()}','{self.data_list_padronizado[pos]['cliente_total_de_parcelas_pagas'].pop()}','{self.data_list_padronizado[pos]['cliente_valor_recebido'].pop()}','{self.data_list_padronizado[pos]['cliente_qtd_de_parcelas_a_pagar'].pop()}','{self.data_list_padronizado[pos]['cliente_saldo_devedor'].pop()}')")

        return querry_list

    def tratar_valor_vazio(self, valor):
        if valor == '' or valor.__len__() == 0:
            return '0'
        return valor

    def juntar_posicoes_em_string_padrao_banco(self, data_para_adicionar: str, data_list_local_add: list) -> list:
        data = data_list_local_add.pop()
        data += f'*{data_para_adicionar}'
        return [data]

        # Model.inserir_dados_no_banco(querry_list=querry_list,index=666)

        # self.querry_list.append(f"insert into relfinal (condominio, unidade, numerocontrato, andar, torre, statusunidade, totalrecebido, saldoatrasado, saldoavencer, parcelasvencidas, parcelasavencer, parcelachave, total, quantidadedisponiveis, nome_cliente, inadimplencia, qtd_quarto, recebivel) values ('Mirante da Serra','{unidade}','{num_contrato}','{andar}','{torre}','{status_unidade}','{total_recebido}','{saldo_atrasado}','{saldo_a_vencer}','{parcelas_vencidas}','{parcelas_a_vencer}','{parcelas_chaves}', '{total}','{quantidade_disponiveis}','{nome_cliente}','{inadimplencia}','{qtd_quartos}','{recebivel}')")
        # print(str(index) + ' ' + nome_cliente + ' ' + unidade + ' ' + andar + ' ' + torre + ' ' + status_unidade + ' ' + total_recebido + ' ' + saldo_atrasado + ' ' + saldo_a_vencer + ' ' + parcelas_vencidas + ' ' + parcelas_a_vencer + ' ' + parcelas_chaves + ' ' + total + ' ' + quantidade_disponiveis + ' ' + inadimplencia + ' ')
        # self.querry_list = Model.inserir_dados_no_banco(querry_list=self.querry_list, index=0)

        # for dict_para_analise in self.data_list_dict:
        #    print(dict_para_analise['cliente_nome'], dict_para_analise['cliente_numero_de_contrato'])

        #    dict_analise_para_padronizacao = dict(
        #        cliente_codigo=str(dict_para_analise['cliente_codigo']),
        #        cliente_numero_de_contrato=str(dict_para_analise['cliente_numero_de_contrato']),
        #        cliente_identificador_unidade=str(dict_para_analise['cliente_numero_de_contrato']).replace(' ', ''),
        #        cliente_nome=str(dict_para_analise['cliente_numero_de_contrato']),
        #        cliente_cpf_cnpj=str(dict_para_analise['cliente_numero_de_contrato']),
        #        cliente_endereco=str(dict_para_analise['cliente_endereco']),
        #        cliente_valor_venda=str(dict_para_analise['cliente_valor_venda']),
        #        cliente_status_venda=str(dict_para_analise['cliente_status_venda']),
        #        cliente_total_de_parcelas_pagas=str(dict_para_analise['cliente_total_de_parcelas_pagas']),
        #        cliente_valor_recebido=str(dict_para_analise['cliente_valor_recebido']),
        #        cliente_qtd_de_parcelas_a_pagar=str(dict_para_analise['cliente_qtd_de_parcelas_a_pagar']),
        #        cliente_saldo_devedor=str(dict_para_analise['cliente_saldo_devedor'])
        #    )

        """
        """

        pass
