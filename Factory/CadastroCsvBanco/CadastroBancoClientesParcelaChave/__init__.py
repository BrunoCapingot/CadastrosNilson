from Factory.Processo import Processo
import pandas as pd

class CadastroBancoClientesParcelaChave(Processo):

    def executar(self,Model,View):
        self.data_base_inad_estoque_bangalos_inadiplentes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Clientes_parcela_chave_novo.xlsx')
        Model.inserir_dados_no_banco(querry_list=self.executar_extracao(), index=0)

    def executar_extracao(self) -> list:
            querry_list = list()
            for index, row in self.data_base_inad_estoque_bangalos_inadiplentes.iterrows():
                cliente_nome = row['Cliente']
                cliente_numero_venda = row['NumeroVenda']
                cliente_tipo_parcela = row['TipoParcela']
                cliente_numero_parcela = row['NumParcela']
                cliente_data_vencimento = row['DataVencimento']
                cliente_valor_parcela = row['ValorParcela']
                querry_list.append(f"INSERT INTO table_csv_cliente_parcela_chave(cliente_nome,cliente_numero_venda,cliente_tipo_parcela,cliente_numero_parcela,cliente_data_vencimento,cliente_valor_parcela)VALUES ('{cliente_nome}','{cliente_numero_venda}','{cliente_tipo_parcela}','{cliente_numero_parcela}','{cliente_data_vencimento}','{cliente_valor_parcela}')")
            return querry_list