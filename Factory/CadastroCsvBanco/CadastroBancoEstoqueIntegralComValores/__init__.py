from Factory.Processo import Processo
import pandas as pd

class CadastroBancoEstoqueIntegralComValores(Processo):
    def __init__(self, nome, prioridade):
        super().__init__(nome=nome, prioridade=prioridade)
        self.model = None
        self.view = None
        self.csv_table_estoque_integral_com_valores = None
class CadastroBancoEstoqueIntegralComValores(Processo):
    def executar(self,Model,View):
        self.model = Model
        self.view = View
        self.csv_table_estoque_integral_com_valores = pd.read_excel('')
