from Factory.Processo import Processo


class CadastroBancoBangalosDisponiveisComValor(Processo):
    def __init__(self, nome, prioridade, datalist, Model, View):
        super().__init__(nome=nome, prioridade=prioridade, datalist=datalist, Model=Model, View=View)

    def executar(self):
        for row in self.csv_table:
            self.model.insert_into_csv_bangalo_disponivel_com_valor(estoque_unidade,estoque_nome,estoque_valor,estoque_quantidade_quartos)
