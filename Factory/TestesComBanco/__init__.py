from Factory.Processo import Processo


class TestesComBanco(Processo):
    def __init__(self, nome, prioridade):
        super().__init__(nome=nome, prioridade=prioridade)
        self.table_cvs_relatorio_geral_clientes_2023 = None
        self.table_cvs_relatorio_geral_clientes_2023_padronizada = None

    def executar(self, Model, View):
        self.table_cvs_relatorio_geral_clientes_2023_padronizada=Model.select(coluna='saldo_devedor', tabela='table_cvs_relatorio_geral_clientes_2023_padronizada')
        self.table_cvs_relatorio_geral_clientes_2023=Model.select(coluna='saldo_devedor', tabela='table_cvs_relatorio_geral_clientes_2023')
        self.somar_valores(tabela_um=self.table_cvs_relatorio_geral_clientes_2023_padronizada,tabela_dois=self.table_cvs_relatorio_geral_clientes_2023)

    def somar_valores(self,tabela_um:list,tabela_dois:list):
        valor_soma_tabel_um = 0
        valor_soma_tabel_dois = 0
        for elemento in tabela_um:
            suporte_list = 0
            suporte_number = 0
            if '*' in elemento[0]:
                suporte_list = elemento[0].split('*')
                for valor in suporte_list:
                    suporte_number = suporte_number + float(valor)
                valor_soma_tabel_um = valor_soma_tabel_um + suporte_number
            else:
                suporte_number = suporte_number + float(elemento[0])
                valor_soma_tabel_um = valor_soma_tabel_um + suporte_number

        pass

        for elemento in tabela_dois:
            pass



