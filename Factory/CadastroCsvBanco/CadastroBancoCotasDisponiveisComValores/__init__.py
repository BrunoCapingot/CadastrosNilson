from Factory.Processo import Processo
import pandas as pd

class CadastroBancoCotasDisponiveisComValores(Processo):
    def __init__(self, nome, prioridade, datalist, Model, View):
        super().__init__(nome, prioridade, datalist, Model, View)

    def executar(self):
        for row in self.csv_table['csv_table']:
            self.model.insert_table_csv_estoque_disponivel_com_valores(estoque_torre=row['estoque_torre'],estoque_unidade=row['estoque_unidade'],estoque_quartos=row['estoque_quartos'],estoque_valor_venda=row['estoque_valor_venda'])

