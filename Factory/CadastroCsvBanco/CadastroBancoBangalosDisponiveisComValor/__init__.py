from Factory.Processo import Processo
import pandas as pd


class CadastroBancoBangalosDisponiveisComValor(Processo):
    def executar(self, Model, View):
        self.data_base_inad_estoque_bangalos_inadiplentes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Bangalo_disponiveis_com_valor.xlsx')
        Model.inserir_dados_no_banco(querry_list=self.executar_extracao(), index=0)

    def executar_extracao(self) -> list:
        querry_list = list()
        for index, row in self.data_base_inad_estoque_bangalos_inadiplentes.iterrows():
            estoque_estoque = row['Estoque']
            estoque_nome = row['nome']
            estoque_valor = row['valor']
            querry_list.append(f"INSERT INTO table_csv_bangalo_disponivel_com_valor(estoque_estoque,estoque_nome,estoque_valor)VALUES('{estoque_estoque}','{estoque_nome}','{estoque_valor}')")
        return querry_list
