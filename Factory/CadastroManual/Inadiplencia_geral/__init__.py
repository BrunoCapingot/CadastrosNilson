import pandas as pd

class Inadiplencia_geral:
    def __init__(self, Model):
        self.model = Model
        self.data_base_inad_estoque_bangalos_inadiplentes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Inadiplencia_geral_atualizada_30_09_2024.xlsx')
        self.lista_dados_necessarios = list()

    def extrair_dados_necessarios(self) -> None:
        for index, row in self.data_base_inad_estoque_bangalos_inadiplentes.iterrows():
            self.lista_dados_necessarios.append(dict(index=index, empreendimento='Mirante Da Serra', nome=row['nome'], valor_em_aberto=row['valores em aberto'], parcelas_em_aberto=row['parcelas em aberto']))

    def cadastrar_dados_necessarios(self) -> None:
        querry_list = list()
        for dict_row in self.lista_dados_necessarios:
            unidade = '0'
            num_contrato = '0'
            andar = '0'
            torre = '0'
            status_unidade = 'NORMAL'
            total_recebido = '0'
            saldo_atrasado = '0'
            saldoavencer = '0'
            saldo_vencido = '0'
            parcelas_a_vencer = str(dict_row['parcelas_em_aberto'])
            parcelas_chaves = '0'
            total = str(dict_row['valor_em_aberto'])
            quantidade_disponiveis = '0'
            nome_cliente = str(dict_row['nome'])
            inadimplencia = '0'
            qtd_quartos = '0'
            querry_list.append(f"insert into relfinal (condominio, unidade, numerocontrato, andar, torre, statusunidade, totalrecebido, saldoatrasado, saldoavencer, parcelasvencidas, parcelasavencer, parcelachave, total, quantidadedisponiveis, nome_cliente, inadimplencia, qtd_quarto) values ('Mirante da Serra','{unidade}','{num_contrato}','{andar}','{torre}','{status_unidade}','{total_recebido}','{saldo_atrasado}','{saldoavencer}','{saldo_vencido}','{parcelas_a_vencer}','{parcelas_chaves}', '{total}','{quantidade_disponiveis}','{nome_cliente}','{inadimplencia}','{qtd_quartos}')")
        self.model.inserir_dados_no_banco(querry_list=querry_list, index=0)


