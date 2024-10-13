import pandas as pd

class Cadastro_inad_estoque_bangalos_inadiplentes:
    def __init__(self, Model, View):
        self.model = Model
        self.view = View
        self.data_base_inad_estoque_bangalos_inadiplentes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\inad_estoque.xltx')
        self.lista_dados_necessarios = list()

    def extrair_dados_necessarios(self) -> None:
        for index, row in self.data_base_inad_estoque_bangalos_inadiplentes.iterrows():
            self.lista_dados_necessarios.append(dict(index=index, contrato=row['n. contrato'], status=row['status'],empreendimento=row['empreendimento'], unidade=row['unidade'],nome=row['nome'], valor_inadimplente=row['valor inadimplente']))

    def cadastrar_dados_necessarios(self) -> None:
        querry_list = list()
        for dict_row in self.lista_dados_necessarios:
            unidade = str(dict_row['unidade'])
            num_contrato = str(dict_row['contrato'])
            andar = ''
            torre = ''
            status_unidade = str(dict_row['status'])
            total_recebido = '0'
            saldo_atrasado = '0'
            saldo_a_vencer = '0'
            saldo_vencido = '0'
            parcelas_a_vencer = '0'
            parcelas_chaves = '0'
            total = '0'
            quantidade_disponiveis = '0'
            nome_cliente = str(dict_row['nome'])
            inadimplencia = str(dict_row['valor_inadimplente'])
            qtd_quartos = '0'
            querry_list.append(f"insert into relfinal (condominio, unidade, numerocontrato, andar, torre, statusunidade, totalrecebido, saldoatrasado, saldoavencer, parcelasvencidas, parcelasavencer, parcelachave, total, quantidadedisponiveis, nome_cliente, inadimplencia, qtd_quarto) values ('Mirante da Serra','{unidade}','{num_contrato}','{andar}','{torre}','{status_unidade}','{total_recebido}','{saldo_atrasado}','{saldo_a_vencer}','{saldo_vencido}','{parcelas_a_vencer}','{parcelas_chaves}', '{total}','{quantidade_disponiveis}','{nome_cliente}','{inadimplencia}','{qtd_quartos}')")

        self.model.inserir_dados_no_banco(querry_list=querry_list, index=0)


