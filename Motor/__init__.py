class Motor:
    def __init__(self):
        self.lista_de_execucao = list()

    def adicionar_lista_de_execucao(self, execution_list: list) -> None:
        self.lista_de_execucao = execution_list

    def executar_motor(self):
        for processo in self.lista_de_execucao:
            processo.executar()
