from Factory.Processo import Processo


class CadastroBancoClientesCadastrados(Processo):
    def __init__(self, nome, prioridade, datalist, Model, View):
        super().__init__(nome=nome, prioridade=prioridade, datalist=datalist, Model=Model, View=View)

    def executar(self):
        for row in self.csv_table['geral_clientes_2023']:
            self.model.insert_table_csv_clientes_cadastrados(
                cliente_codigo = str(row[1]),
                cliente_nome = str(row[4]),
                cliente_cpf_cnpj = str(row[5]),
                cliente_endereco = str(row[6]),
                cliente_cep = str('analisar'),
                cliente_cidade = str('analisar'),
                cliente_uf = str('analisar'),
                cliente_indexacao = str('analisar'),
                cliente_status = str('analisar'))

        for row in self.csv_table['geral_clientes_2025']:
            self.model.insert_table_csv_clientes_cadastrados(
                cliente_codigo = str('analisar'),
                cliente_nome = str(row['nome']),
                cliente_cpf_cnpj = str(row['cpf_cnpj']),
                cliente_endereco = str(row['endereco']),
                cliente_cep = str(row['cep']),
                cliente_cidade = str(row['cidade']),
                cliente_uf = str(row['uf']),
                cliente_indexacao = str(row['indexador']),
                cliente_status = str('analisar')
            )
