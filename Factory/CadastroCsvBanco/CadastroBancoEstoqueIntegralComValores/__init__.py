from Factory.Processo import Processo
import pandas as pd


class CadastroBancoEstoqueIntegralComValores(Processo):
    def __init__(self, nome, prioridade, datalist, Model, View):
        super().__init__(nome=nome, prioridade=prioridade, datalist=datalist, Model=Model, View=View)

    def executar(self):
        for row in self.csv_table:
            self.model.insert_into_estoque_integral_com_valores(unidade_torre=str(row['unidade_torre']),
                                                                unidade_unidade=str(row['unidade_unidade']),
                                                                unidade_quartos=self.remover_letras(string=str(row['unidade_quartos'])),
                                                                unidade_valor=str(row['unidade_valor']))


    def remover_letras(self, string):
        return ''.join(filter(str.isdigit, string))
