from Factory.Processo import Processo
import pandas as pd

class CadastroBancoCotasDisponiveisComValores(Processo):

    def executar(self, Model, View):
        self.data_base_inad_estoque_bangalos_inadiplentes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\estoque cotas disponiveis_novo.xlsx')
        Model.inserir_dados_no_banco(querry_list=self.executar_extracao(), index=0)

    def executar_extracao(self) -> list:
        querry_list = list()
        for index, row in self.data_base_inad_estoque_bangalos_inadiplentes.iterrows():
            estoque_torre = row['torre']
            estoque_unidade = row['unidade']
            estoque_quartos = row['quartos']
            estoque_valor_venda = row['valor venda']
            querry_list.append(
                f"INSERT INTO table_csv_estoque_disponive_com_valores(estoque_torre,estoque_unidade,estoque_quartos,estoque_valor_venda)VALUES('{estoque_torre}','{estoque_unidade}','{estoque_quartos}','{estoque_valor_venda}')")
        return querry_list
