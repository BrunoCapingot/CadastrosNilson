from Factory.Processo import Processo
import pandas as pd


class CadastroBancoRelatorioGeralClientes2023(Processo):
    def __init__(self,nome,prioridade):
        super().__init__(nome=nome, prioridade=prioridade)
        self.table_csv_relatorio_geral_clientes2023 = None

class CadastroBancoRelatorioGeralClientes2023(Processo):
    def executar(self, Model, View):
        self.table_csv_relatorio_geral_clientes2023 = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Relatorio geral de clientes 18-10-2023.xlsx')
        querry_list = list()
        for index, row in self.table_csv_relatorio_geral_clientes2023.iterrows():
            if index != 'parada':
                cliente_codigo = str(row['codCliente'])
                cliente_numero_de_contrato = str(row['numContrato'])
                cliente_identificador_unidade = str(row['identificadorUnidade'])
                cliente_nome = str(row['Nome'])
                cliente_cpf_cnpj = str(row['cpf/cnpj'])
                cliente_endereco = str(row['endereco'])
                cliente_valor_venda = str(row['valorVenda'])
                cliente_status_venda = str(row['statusVenda'])
                cliente_total_de_parcelas_pagas = str(row['totalDeParcelasPagas'])
                cliente_valor_recebido = str(row['valorRecebido'])
                cliente_qtd_de_parcelas_a_pagar = str(row['qtdParcelasApagar'])
                cliente_saldo_devedor = str(row['saldoDevedor'])
                querry_list.append(f"insert into table_cvs_relatorio_geral_clientes_2023(cliente_codigo,cliente_numero_contrato,cliente_identificador_unidade,cliente_nome,cliente_cpf_cnpj,cliente_endereco,cliente_valor_venda,cliente_status_venda,cliente_total_de_parcelas_pagas,cliente_valor_recebido,qtd_parcelas_a_pagar,saldo_devedor)VALUES('{cliente_codigo}','{cliente_numero_de_contrato}','{cliente_identificador_unidade}','{cliente_nome}','{cliente_cpf_cnpj}','{cliente_endereco}','{cliente_valor_venda}','{cliente_status_venda}','{cliente_total_de_parcelas_pagas}','{cliente_valor_recebido}','{cliente_qtd_de_parcelas_a_pagar}','{cliente_saldo_devedor}')")
                if index == 1305 or index == 2000 or index == 3000 or index == 4000 or index == 4300:
                    querry_list = Model.inserir_dados_no_banco(querry_list=querry_list, index=index)