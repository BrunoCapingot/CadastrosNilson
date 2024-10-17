from Factory.Processo import Processo


class CadastroBancoDisponiveis(Processo):
    def __init__(self, nome, prioridade, datalist, Model, View):
        super().__init__(nome=nome, prioridade=prioridade, datalist=datalist, Model=Model, View=View)

    def executar(self):
        for row in self.csv_table['csv_table_bangalo']:
            self.model.insert_into_disponiveis(unidade_nome=str(row[2]), unidade_localizacao=str(row[1]),unidade_valor=str(row[3]), unidade_quantidade_quartos='2')

        for row in self.csv_table['csv_table_estoque_disponivel_com_valores']:
            self.model.insert_into_disponiveis(unidade_nome=str(row[2]), unidade_localizacao=str(row[1]),unidade_valor=str(row[4]), unidade_quantidade_quartos=self.remover_letras(string=str(row[3])))

        for row in self.csv_table['csv_table_estoque_integral_com_valores']:
            self.model.insert_into_disponiveis(unidade_nome=str(row[2]), unidade_localizacao=str(row[1]),unidade_valor=str(row[4]), unidade_quantidade_quartos=str(row[3]))

    def remover_letras(self, string):
        return ''.join(filter(str.isdigit, string))