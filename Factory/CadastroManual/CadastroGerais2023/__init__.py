import mysql.connector
import pandas as pd
import re


class CadastroGerais2023:

    def __init__(self,Model,View):
        querry_list = list()
        relatorio_geral_clientes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Relatorio geral de clientes 18-10-2023.xlsx')
        inadiplentes_geral = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Inadimplentes geral.xls')
        clientes_parcela_chave = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Clientes_parcela_chave_novo.xlsx')
        teste = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\teste.xlsx')
        for index, row in relatorio_geral_clientes.iterrows():
            if index !='parada':
                nome_cliente = str(row['Nome'])
                unidade = str(row['identificadorUnidade']).replace(' ', '')
                num_contrato = str(row['numContrato'])
                andar = self.extrair_andar(unidade_analise=unidade)
                torre = self.extrair_torre(unidade_analise=unidade)
                status_unidade = str(row['statusVenda'])
                total_recebido = str(row['valorRecebido'])
                saldo_atrasado = str(row['saldoDevedor'])
                saldo_a_vencer = self.extrair_saldo_a_vencer(nome_cliente=str(nome_cliente), data_frame_devedores=teste)
                saldo_vencido = self.extrair_bb(nome_cliente=str(nome_cliente), data_frame_devedores=teste)
                parcelas_a_vencer = self.extrair_total_parcelas_menos_devendo(nome_cliente=str(nome_cliente),data_frame_devedores=teste)
                parcelas_chaves = self.extrair_parcela_chave(nome_cliente=str(nome_cliente),data_frame_devedores=clientes_parcela_chave)
                total = ''
                quantidade_disponiveis = ''
                inadimplencia = self.extrair_inadiplente(nome_cliente=str(nome_cliente),data_frame_devedores=inadiplentes_geral)
                qtd_quartos = '0'
                querry_list.append(f"insert into relfinal (condominio, unidade, numerocontrato, andar, torre, statusunidade, totalrecebido, saldoatrasado, saldoavencer, parcelasvencidas, parcelasavencer, parcelachave, total, quantidadedisponiveis, nome_cliente, inadimplencia, qtd_quarto) values ('Mirante da Serra','{unidade}','{num_contrato}','{andar}','{torre}','{status_unidade}','{total_recebido}','{saldo_atrasado}','{saldo_a_vencer}','{saldo_vencido}','{parcelas_a_vencer}','{parcelas_chaves}', '{total}','{quantidade_disponiveis}','{nome_cliente}','{inadimplencia}','{qtd_quartos}')")
                print(
                    str(index) + ' ' + nome_cliente + ' ' + unidade + ' ' + andar + ' ' + torre + ' ' +
                    status_unidade + ' ' + total_recebido + ' ' + saldo_atrasado + ' ' + saldo_a_vencer +
                    ' ' + saldo_vencido + ' ' + parcelas_a_vencer + ' ' + parcelas_chaves + ' ' + total +
                    ' ' + quantidade_disponiveis + ' ' + inadimplencia + ' '
                    )
                if index == 300 or index == 1305 or index == 2000 or index == 3000 or index == 4000 or index == 4300:
                    querry_list = Model.inserir_dados_no_banco(querry_list=querry_list, index=index)
            #input('segurança')

    #Condominio//Unidade//NumeroContrato//andar//torre/statusunidade//totalrecebido//saldoatrasado//saldoavencer//parcelasvencidas//parcelasavencer//parcelachave//total//quantidadedisponiveis
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
        for index, row_devedor in data_frame_devedores.iterrows():
            nome_devedor = str(row_devedor['CLIENTE'])
            if nome_devedor == nome_cliente:
                valor_em_aberto = float(row_devedor['valorEmAberto'])
                return str(valor_em_aberto)
        return '0'

    def extrair_parcela_chave(self, nome_cliente: str, data_frame_devedores) -> str:
        for index, row_devedor in data_frame_devedores.iterrows():
            nome_devedor = str(row_devedor['Cliente'])
            if nome_devedor == nome_cliente:
                numeros_de_parcela = int(row_devedor['NumParcela'])
                valor_da_parcela = float(row_devedor['ValorParcela'])
                return str(numeros_de_parcela * valor_da_parcela)
        return '0'

    def extrair_total_parcelas_menos_devendo(self, nome_cliente: str, data_frame_devedores):
        lista_de_parcelas_em_aberto = list()
        parcelas_a_vencer = 0
        for index, row_devedor in data_frame_devedores.iterrows():
            nome_devedor = str(row_devedor['CLIENTE'])
            # print('Nome devedor: {}'.format(nome_devedor))
            # print('Nome cliente: {}'.format(nome_cliente))
            if nome_devedor == nome_cliente:
                valor_parcela_devedor = str(row_devedor['VALOR'])
                parcelas_devedor = self.retirar_letras(str(row_devedor['PARCELA'])).replace(' ', '')
                lista_de_parcelas_em_aberto.append(
                    {
                        'nome_cliente': nome_cliente,
                        'valor_parcela': valor_parcela_devedor,
                        'parcelas_devedor': self.retirar_letras(dado_com_letra=parcelas_devedor)
                    }
                )
                dict_parcela = lista_de_parcelas_em_aberto[-1]
                lista_parcela_inical_final_devedor = dict_parcela['parcelas_devedor'].split('/')
                print('lista_parcela_inical_final_devedor: {}'.format(lista_parcela_inical_final_devedor))
                parcela_inicial = int(lista_parcela_inical_final_devedor[0])
                parcela_final = int(lista_parcela_inical_final_devedor[1])
                parcelas_a_vencer = parcela_final - parcela_inicial

        return str(parcelas_a_vencer)

    def extrair_bb(self, nome_cliente: str, data_frame_devedores) -> str:
        lista_de_parcelas_em_aberto = list()
        resultado = 0
        parcela_inicial = 0
        parcela_final = 0
        valor_parcela_final = 0
        for index, row_devedor in data_frame_devedores.iterrows():
            nome_devedor = str(row_devedor['CLIENTE'])
            #print('Nome devedor: {}'.format(nome_devedor))
            #print('Nome cliente: {}'.format(nome_cliente))
            if nome_devedor == nome_cliente:
                valor_parcela_devedor = str(row_devedor['VALOR'])
                parcelas_devedor = self.retirar_letras(str(row_devedor['PARCELA'])).replace(' ', '')
                lista_de_parcelas_em_aberto.append(
                    {'nome_cliente': nome_cliente, 'valor_parcela': valor_parcela_devedor,
                     'parcelas_devedor': self.retirar_letras(dado_com_letra=parcelas_devedor)})
                dict_parcela_final = lista_de_parcelas_em_aberto[-1]
                dict_parcela_inicial = lista_de_parcelas_em_aberto[0]
                parcela_inicial = int(dict_parcela_inicial['parcelas_devedor'].split('/')[0])
                parcela_final = int(dict_parcela_final['parcelas_devedor'].split('/')[0])
                valor_parcela_final = (parcela_final - parcela_inicial) + 1
        print('Valor_Parcela {}'.format(valor_parcela_final))
        return str(valor_parcela_final)

    def extrair_saldo_a_vencer(self, nome_cliente: str, data_frame_devedores) -> str:
        valor_devido_cliente = 0
        lista_parcelas_devedor = list()
        for index_alternativo, row_devedores in data_frame_devedores.iterrows():
            nome_cliente_row_devedores = str(row_devedores['CLIENTE'])
            if nome_cliente == nome_cliente_row_devedores:
                parcelas_devedor = self.retirar_letras(dado_com_letra=str(row_devedores['PARCELA'])).replace(' ', '')
                parcelas_devedor = parcelas_devedor.split('/')
                parcela_inicial = float(parcelas_devedor[0])
                parcela_final = float(parcelas_devedor[1])
                valor_parcela = float(row_devedores['VALOR'])
                return str((parcela_final - parcela_inicial) * valor_parcela)

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

