import time

from Factory.Processo import Processo
import re


class CadastroDadosSiteGerais2023(Processo):
    def __init__(self, nome, prioridade):
        super().__init__(nome, prioridade)
        self.data_base_table_cvs_relatorio_geral_clientes_2023 = None
        self.data_base_table_csv_dados_de_pagamento_padrao = None
        self.data_base_table_csv_cliente_parcela_chave = None
        self.data_base_table_cvs_inadiplencia_geral = None
        self.querry_list = None

    def executar(self, Model, View):
        self.data_base_table_cvs_relatorio_geral_clientes_2023 = Model.get_table_cvs_relatorio_geral_clientes_2023_padronizada()
        self.data_base_table_cvs_inadiplencia_geral = Model.get_table_cvs_inadiplencia_geral()
        self.data_base_table_csv_cliente_parcela_chave = Model.get_table_cvs_parcela_chave()
        self.data_base_table_csv_dados_de_pagamento_padrao = Model.get_table_csv_dados_de_pagamento_padrao()
        self.querry_list = list()
        index_final = self.data_base_table_cvs_relatorio_geral_clientes_2023[-1][0]
        index_inicial = self.data_base_table_cvs_relatorio_geral_clientes_2023[0][0]
        print(index_final - index_inicial)
        time.sleep(1)
        for row in self.data_base_table_cvs_relatorio_geral_clientes_2023:
            index = row[0]
            if row != 'parada':
                nome_cliente = str(row[4])
                unidade = str(row[3]).replace(' ', '')
                num_contrato = str(row[2])
                andar = self.extrair_andar(unidade_analise=unidade)
                torre = self.extrair_torre(unidade_analise=unidade)
                status_unidade = str(row[8])
                total_recebido = str(row[10])
                saldo_atrasado = str(row[12])
                saldo_a_vencer = self.extrair_saldo_a_vencer(nome_cliente=str(nome_cliente), data_frame_devedores=self.data_base_table_csv_dados_de_pagamento_padrao)
                parcelas_vencidas = self.extrair_qtd_parcelas_vencidas(nome_cliente=str(nome_cliente),data_frame_devedores=self.data_base_table_csv_dados_de_pagamento_padrao)
                parcelas_a_vencer = self.extrair_total_parcela_final_menos_parcela_aberta(nome_cliente=str(nome_cliente),data_frame_devedores=self.data_base_table_csv_dados_de_pagamento_padrao)
                parcelas_chaves = self.extrair_parcela_chave(nome_cliente=str(nome_cliente), data_frame_devedores=self.data_base_table_csv_cliente_parcela_chave)
                total = str(float(saldo_a_vencer) + float(saldo_atrasado) + float(parcelas_chaves))
                quantidade_disponiveis = '0'
                inadimplencia = self.extrair_inadiplente(nome_cliente=str(nome_cliente),data_frame_devedores=self.data_base_table_cvs_inadiplencia_geral)
                qtd_quartos = '0'
                recebivel = str(float(saldo_a_vencer) + float(parcelas_chaves) + float(saldo_atrasado))
                self.querry_list.append(f"insert into relfinal (condominio, unidade, numerocontrato, andar, torre, statusunidade, totalrecebido, saldoatrasado, saldoavencer, parcelasvencidas, parcelasavencer, parcelachave, total, quantidadedisponiveis, nome_cliente, inadimplencia, qtd_quarto, recebivel) values ('Mirante da Serra','{unidade}','{num_contrato}','{andar}','{torre}','{status_unidade}','{total_recebido}','{saldo_atrasado}','{saldo_a_vencer}','{parcelas_vencidas}','{parcelas_a_vencer}','{parcelas_chaves}', '{total}','{quantidade_disponiveis}','{nome_cliente}','{inadimplencia}','{qtd_quartos}','{recebivel}')")
                print(str(index) + ' ' + nome_cliente + ' ' + unidade + ' ' + andar + ' ' + torre + ' ' + status_unidade + ' ' + total_recebido + ' ' + saldo_atrasado + ' ' + saldo_a_vencer + ' ' + parcelas_vencidas + ' ' + parcelas_a_vencer + ' ' + parcelas_chaves + ' ' + total + ' ' + quantidade_disponiveis + ' ' + inadimplencia + ' ')
                if index == index_final:
                    self.querry_list = Model.inserir_dados_no_banco(querry_list=self.querry_list, index=0)
    def somar_valores(self,list_value: list) -> str:
        soma = 0
        while list_value.__len__()!=0:
            dt = float(list_value.pop())
            soma = dt + soma

        return str(soma)

    # Condominio//Unidade//NumeroContrato//andar//torre/statusunidade//totalrecebido//saldoatrasado//saldoavencer//parcelasvencidas//parcelasavencer//parcelachave//total//quantidadedisponiveis
    def inserir_dados_no_banco(self, querry_list: list, cursor, cnx, index) -> list:
        if index == 500:
            del_querry_list = ['set sql_safe_updates = 0', 'delete from relfinal']
            cursor.execute(del_querry_list[0])
            cnx.commit()
            cursor.fetchall()
            cursor.execute(del_querry_list[1])
            cnx.commit()
            cursor.fetchall()
        while querry_list.__len__() != 0:
            cursor.execute(querry_list.pop())
            cnx.commit()
            cursor.fetchall()
        return querry_list

    def extrair_inadiplente(self, nome_cliente: str, data_frame_devedores) -> str:
        for row_devedor in data_frame_devedores:
            nome_devedor = str(row_devedor[1])
            if nome_devedor == nome_cliente:
                parcelas_da_tabela = float(row_devedor[2])
                valor_em_aberto = float(row_devedor[3])
                return str(valor_em_aberto)
        return '0'

    def extrair_parcela_chave(self, nome_cliente: str, data_frame_devedores) -> str:
        for row_devedor in data_frame_devedores:
            nome_devedor = str(row_devedor[1])
            if nome_devedor == nome_cliente:
                numeros_de_parcela = int(row_devedor[4])
                valor_da_parcela = float(row_devedor[6])
                return str(numeros_de_parcela * valor_da_parcela)
        return '0'

    def extrair_total_parcela_final_menos_parcela_aberta(self, nome_cliente: str, data_frame_devedores):

        lista_de_parcelas_em_aberto = list()
        parcelas_a_vencer = 0
        for row_devedor in data_frame_devedores:
            nome_devedor = str(row_devedor[1])
            # print('Nome devedor: {}'.format(nome_devedor))
            # print('Nome cliente: {}'.format(nome_cliente))
            if nome_devedor == nome_cliente:
                valor_parcela_devedor = str(row_devedor[3])
                parcelas_devedor = self.retirar_letras(str(row_devedor[4])).replace(' ', '')
                lista_de_parcelas_em_aberto.append(
                    {
                        'nome_cliente': nome_cliente,
                        'valor_parcela': valor_parcela_devedor,
                        'parcelas_devedor': self.retirar_letras(dado_com_letra=parcelas_devedor)
                    }
                )
        if lista_de_parcelas_em_aberto.__len__() != 0:
            dict_parcela = lista_de_parcelas_em_aberto[0]
            lista_parcela_inical_final_devedor = dict_parcela['parcelas_devedor'].split('/')
            parcela_inicial = int(lista_parcela_inical_final_devedor[0])
            parcela_final = int(lista_parcela_inical_final_devedor[1])
            parcelas_a_vencer = parcela_final - parcela_inicial
        return str(parcelas_a_vencer)

    def extrair_qtd_parcelas_vencidas(self, nome_cliente: str, data_frame_devedores) -> str:

        lista_de_parcelas_em_aberto = list()
        resultado = 0
        parcela_inicial = 0
        parcela_final = 0
        qtd_parcelas_vencidas = 0
        for row_devedor in data_frame_devedores:
            nome_devedor = str(row_devedor[1])

            # print('Nome devedor: {}'.format(nome_devedor))
            # print('Nome cliente: {}'.format(nome_cliente))
            if nome_devedor == nome_cliente:
                valor_parcela_devedor = str(row_devedor[3])
                parcelas_devedor = self.retirar_letras(str(row_devedor[4])).replace(' ', '')
                lista_de_parcelas_em_aberto.append(
                    {
                        'nome_cliente': nome_cliente, 'valor_parcela': valor_parcela_devedor,
                        'parcelas_devedor': self.retirar_letras(dado_com_letra=parcelas_devedor)
                    }
                )
        if lista_de_parcelas_em_aberto.__len__() != 0:
            dict_parcela_final = lista_de_parcelas_em_aberto[0]
            dict_parcela_inicial = lista_de_parcelas_em_aberto[-1]
            parcela_inicial = int(dict_parcela_inicial['parcelas_devedor'].split('/')[0])
            parcela_final = int(dict_parcela_final['parcelas_devedor'].split('/')[0])
            qtd_parcelas_vencidas = (parcela_final - parcela_inicial)
        return str(qtd_parcelas_vencidas)

    def extrair_saldo_a_vencer(self, nome_cliente: str, data_frame_devedores) -> str:
        valor_devido_cliente = 0

        lista_parcelas_devedor = list()
        for row_devedores in data_frame_devedores:
            nome_cliente_row_devedores = str(row_devedores[1])
            if nome_cliente == nome_cliente_row_devedores:
                parcelas_devedor = self.retirar_letras(dado_com_letra=str(row_devedores[4])).replace(' ', '')
                valor_parcela_devedor = str(row_devedores[3])
                lista_parcelas_devedor.append(
                    {
                        'nome_cliente': nome_cliente, 'valor_parcela': valor_parcela_devedor,
                        'parcelas_devedor': self.retirar_letras(dado_com_letra=parcelas_devedor)
                    }
                )
        if lista_parcelas_devedor.__len__() != 0:
            dict_parcela_final = lista_parcelas_devedor[0]
            parcelas_devedor = dict_parcela_final['parcelas_devedor'].split('/')
            parcela_inicial = float(parcelas_devedor[0])
            parcela_final = float(parcelas_devedor[1])
            valor_parcela = float(dict_parcela_final['valor_parcela'])
            resultado = (parcela_final - parcela_inicial) * valor_parcela
            return str(resultado)

        """for index, row_cliente_devedor in data_frame_devedores.iterrows():
            valor_row_parcela = row_cliente_devedor['VALOR']
            nome_cliente_tabela_devedor = row_cliente_devedor['CLIENTE']
            if nome_cliente_tabela_devedor == nome_cliente:
                parcela = str(row_cliente_devedor['PARCELA']).replace(' ','')
                parcela = parcela.split('/')
                parcela_paga =  parcela[0]
                parcela_nao_paga =  parcela[1]
                return str((int(parcela_nao_paga) - int(parcela_paga)) * valor_row_parcela)

            else:
                pass"""

        return '0'

    def extrair_parcelas_a_vencer(self, nome_cliente: str, data_frame_devedores) -> str:
        if nome_cliente.upper() == 'AULUS CARVALHO DE OLIVEIRA':
            pass
        valor_devido_cliente = 0
        data_frame_devedores = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\teste.xlsx')
        for index, row_cliente_devedor in data_frame_devedores.iterrows():
            valor_row_parcela = row_cliente_devedor['VALOR']
            nome_cliente_tabela_devedor = row_cliente_devedor['CLIENTE']
            if nome_cliente_tabela_devedor == nome_cliente:
                parcela = str(row_cliente_devedor['PARCELA']).replace(' ', '')
                parcela = parcela.split('/')
                parcela_paga = parcela[0]
                parcela_nao_paga = parcela[1]
                return str(parcela_nao_paga)

            else:
                pass

        return '0'

    def extrair_torre(self, unidade_analise: str) -> str:
        if '/' in unidade_analise:
            return 'B'
        else:
            return 'A'

    def extrair_andar(self, unidade_analise: str) -> str:
        lista_comparacao_de_final = ['14', '16', '18', '19', '17', '13']
        if '/' in unidade_analise:
            data = unidade_analise.split('/')[0].replace(' ', '')
            if data.__len__() == 4:
                andar = '{}{}'.format(str(data[0]), str(data[1]))
                return andar
            elif data.__len__() == 3:
                andar = '{}'.format(str(data[0]))
                return andar
        else:
            data = unidade_analise
            if data.__len__() == 4:
                for numero_final_apartamento in lista_comparacao_de_final:
                    type_aparmento = '{}'.format(str(data[-2:]))
                    if numero_final_apartamento == type_aparmento:
                        return '2'

                    else:
                        return '1'

            elif data.__len__() == 3:
                for numero_final_apartamento in lista_comparacao_de_final:
                    type_aparmento = '{}'.format(str(data[-2:]))
                    if numero_final_apartamento == type_aparmento:
                        return '2'

                    else:
                        return '1'
        return '0'

    def retirar_letras(self, dado_com_letra) -> str:
        return re.sub(r'[a-zA-Z]', '', dado_com_letra)
