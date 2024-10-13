import pandas as pd


class CadastroGerais2023NoBanco:

    def __init__(self,Model,View):
        self.model = Model
        self.view = View
        querry_list = list()
        relatorio_geral_clientes = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\Relatorio geral de clientes 18-10-2023.xlsx')
        for index, row in relatorio_geral_clientes.iterrows():
            if index !='parada':
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
                querry_list.append(f"insert into table_cvs_relatorio_geral_clientes_2023(cliente_codigo,cliente_numero_contrato,cliente_identificador_unidade,cliente_nome,cliente_cpf_cnpj,cliente_endereco,cliente_valor_venda,cliente_status_venda,cliente_total_de_parcelas_pagas,cliente_valor_recebido,qtd_parcelas_a_pagar,saldo_devedor)VALUES('{cliente_codigo}','{cliente_numero_de_contrato}','{cliente_identificador_unidade}','{cliente_nome}','{cliente_cpf_cnpj}','{cliente_endereco}','{cliente_valor_venda}','{cliente_status_venda }','{cliente_total_de_parcelas_pagas}','{cliente_valor_recebido}','{cliente_qtd_de_parcelas_a_pagar }','{cliente_saldo_devedor}')")
                if index == 500 or index == 1305 or index == 2000 or index == 3000 or index == 4000 or index == 4300:
                    querry_list = Model.inserir_dados_no_banco(querry_list=querry_list, index=index)

    def inserir_dados_no_banco(self, querry_list: list, cursor, cnx, index) -> list:
        if index == 500:
            del_querry_list = ['set sql_safe_updates = 0', 'delete from relfinal']
            cursor.execute(del_querry_list[0])
            cnx.commit()
            cursor.fetchall()
            cursor.execute(del_querry_list[1])
            cnx.commit()
            cursor.fetchall()
        while querry_list.__len__() != 0:
            cursor.execute(querry_list.pop())
            cnx.commit()
            cursor.fetchall()
        return querry_list

