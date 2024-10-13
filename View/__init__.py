class View:
    def __init__(self) -> None:
        pass

    def mostrar_base_dados_carregadas(self, base_dict):
        print(base_dict)

    def mostrar_execucao(self,nome_processo:str):
        print('View :: Executanto processo ->> {}'.format(nome_processo))