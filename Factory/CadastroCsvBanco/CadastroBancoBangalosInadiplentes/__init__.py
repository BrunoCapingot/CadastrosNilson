from Factory.Processo import Processo
import pandas as pd


class CadastroBancoBangalosInadiplentes(Processo):
    def executar(self,Model,View):
        self.data_base_inad_estoque_bangalos_inadiplentes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Inadiplencia_geral_atualizada_30_09_2024.xlsx')
        Model.inserir_dados_no_banco(querry_list=self.executar_extracao(),index=0)

    def executar_extracao(self)->list:
        querry_list = list()
        for index, row in self.data_base_inad_estoque_bangalos_inadiplentes.iterrows():
            cliente_nome = row['nome']
            cliente_parcelas_em_aberto = row['parcelas em aberto']
            cliente_valores_em_aberto = row['valores em aberto']
            querry_list.append(f"INSERT INTO table_csv_inadiplencia_geral(cliente_nome,cliente_parcelas_em_aberto,cliente_valores_em_aberto)VALUES('{cliente_nome}','{cliente_parcelas_em_aberto}','{cliente_valores_em_aberto}')")
        return querry_list