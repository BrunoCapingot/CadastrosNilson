from Factory.Processo import Processo


class CadastroSiteInadiplentes(Processo):
    def __init__(self, nome, prioridade, datalist, Model, View):
        super().__init__(nome=nome, prioridade=prioridade, datalist=datalist, Model=Model, View=View)

    def executar(self):
        condicao_suporte = False
        #for row in self.csv_table['geral_clientes_2023']:
        #    pass
        for row in self.csv_table['geral_clientes_2025']:
            dict_parcelas = self.extrair_parcelas(row=row)
            self.model.insert_table_inadiplentes(
                empreendimento= row['empreendimento'],
                cliente_codigo= '00',
                cliente_nome= row['nome'],
                cpf_cnpj = row['cpf_cnpj'],
                cliente_unidade= row['unidade'],
                cliente_status= row['status'],
                unidade_contrato= row['contrato'],
                unidade_andar= row[''],
                unidade_torre= row[''],
                parcela_chave= row[''],
                parcela_valor= row['valor_das_parcelas_inadiplentes'],
                parcelas_pagas= row[''],
                parcelas_vencidas= row['quantidade_parcelas_inadiplentes'],
                parcelas_nao_vencidas= row['']
            )
            self.exetrair_parcelas(row=row)
    def extrair_parcelas(self,row) -> dict:
        for key in row:
            if key == 'janeiro_2017':
                condicao_suporte = True

        return dict(parcela_valor='',parcelas_pagas='',parcelas_vencidas='',parcelas_nao_vencidas='')