import pandas as pd
import re

class EstoqueCotasDisponiveis:
    def __init__(self, Model, View):
        self.model = Model
        self.view = View
        self.data_base_inad_estoque_bcotas_disponiveis = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\estoque cotas disponiveis_novo.xlsx')
        self.lista_dados_necessarios = list()

    def retirar_letras(self, dado_com_letra) -> str:
        return str(re.sub(r'[a-zA-Z]', '', dado_com_letra))

    def extrair_dados_necessarios(self) -> None:
        for index, row in self.data_base_inad_estoque_bcotas_disponiveis.iterrows():
            self.lista_dados_necessarios.append(dict(
                index=index,
                cliente='Mirante da Serra',
                valor_venda=row['valor venda'],
                quartos=row['quartos'],
                unidade=row['unidade'],
                torre=row['torre'],

            ))

    def cadastrar_dados_necessarios(self) -> None:
        querry_list = list()
        for dict_row in self.lista_dados_necessarios:
            unidade = dict_row['unidade']
            num_contrato = '0'
            andar = '0'
            torre = dict_row['torre']
            status_unidade = 'NORMAL'
            total_recebido = '0'
            saldo_atrasado = '0'
            saldoavencer = '0'
            saldo_vencido = '0'
            parcelas_a_vencer = '0'
            parcelas_chaves = '0'
            total = '0'
            quantidade_disponiveis = '0'
            nome_cliente = dict_row['cliente']
            inadimplencia = '0'
            qtd_quartos = self.retirar_letras(dado_com_letra=dict_row['quartos'])
            querry_list.append(f"insert into relfinal (condominio, unidade, numerocontrato, andar, torre, statusunidade, totalrecebido, saldoatrasado, saldoavencer, parcelasvencidas, parcelasavencer, parcelachave, total, quantidadedisponiveis, nome_cliente, inadimplencia, qtd_quarto) values ('Mirante da Serra','{unidade}','{num_contrato}','{andar}','{torre}','{status_unidade}','{total_recebido}','{saldo_atrasado}','{saldoavencer}','{saldo_vencido}','{parcelas_a_vencer}','{parcelas_chaves}', '{total}','{quantidade_disponiveis}','{nome_cliente}','{inadimplencia}','{qtd_quartos}')")

        self.model.inserir_dados_no_banco(querry_list=querry_list, index=0)



