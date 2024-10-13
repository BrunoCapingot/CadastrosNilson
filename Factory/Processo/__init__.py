class Processo:
    def __init__(self, nome, prioridade, datalist, Model, View):
        self.nome = nome
        self.prioridade = prioridade
        self.model = Model
        self.view = View
        self.csv_table = datalist

    def executar(self):
        pass
