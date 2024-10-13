from Factory.Processo import Processo


class CadastroSiteCotasDisponiveisComValores(Processo):
    def __init__(self, nome, prioridade, data_list):
        super().__init__(nome=nome, prioridade=prioridade)
        self.model = None
        self.view = None
        self.csv_table_cotas_disponiveis_com_valores = data_list


    def executar(self, Model, View):
        self.model = Model
        self.view = View
        for row in self.csv_table_cotas_disponiveis_com_valores:
            self.model.insert_into_relfinal(
                condominio='Mirante da Serra',
                unidade=row[3],
                numerocontrato='0',
                andar=0,
                torre=row[1],
                statusunidade='DISPONIVEL',
                totalrecebido='0',
                saldoatrasado='0',
                saldoavencer='0',
                parcelasvencidas='0',
                parcelasavencer='0',
                total='0',
                parcelachave='0',
                quantidadedisponiveis='1',
                nome_cliente='DISPONIVEL',
                inadimplencia='0',
                qtd_quarto=row[3],
                recebivel='0'
            )