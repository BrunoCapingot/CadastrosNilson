from Factory.Processo import Processo
import pandas as pd


class CadastroBancoDadosPagamentoPadrao(Processo):
    def executar(self, Model, View):
        self.data_base_inad_estoque_bangalos_inadiplentes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Dados_De_Pagamento_Padrao.xlsx')
        Model.inserir_dados_no_banco(querry_list=self.executar_extracao(),index=0)

    def executar_extracao(self)->list:
        querry_list = list()
        for index, row in self.data_base_inad_estoque_bangalos_inadiplentes.iterrows():
            cliente_nome = row['CLIENTE']
            cliente_vencimento_da_parcela = row['VENCIMENTO DA PARCELA']
            cliente_valor = row['VALOR']
            cliente_parcela = row['PARCELA']
            querry_list.append(f"insert into table_csv_dados_de_pagamento_padrao(cliente_nome, cliente_vencimento_da_parcela, cliente_valor,cliente_parcela)VALUES('{cliente_nome}', '{cliente_vencimento_da_parcela}', '{cliente_valor}', '{cliente_parcela}')")
        return querry_list




