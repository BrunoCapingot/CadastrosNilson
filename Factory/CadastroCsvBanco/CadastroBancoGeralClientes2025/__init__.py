from Factory.Processo import Processo


class CadastroBancoGeralClientes2025(Processo):
    def __init__(self, nome, prioridade, datalist, Model, View):
        super().__init__(nome=nome, prioridade=prioridade, datalist=datalist, Model=Model, View=View)

    def executar(self):
        for row in self.csv_table:
            self.model.insert_into_table_csv_cliente_geral_2025( contrato=row['contrato'],status=row['status'],empreendimento=row['empreendimento'],unidade=row['unidade'],
            area=row['area'], nome=row['nome'],cpf_cnpj=row['cpf_cnpj'],data_nascimento=row['data_nascimento'],endereco=row['endereco'],
            bairro=row['bairro'],cidade=row['cidade'],uf=row['uf'],cep=row['cep'],juros_contrato=row['juros_contrato'],indexador=row['indexador'],adm_carteira=row['adm_carteira'],
            data_contrato=row['data_contrato'],valor_imovel=row['valor_imovel'],quantidade_de_entrada=row['quantidade_de_entrada'],sistema_de_amortizacao=row['sistema_de_amortizacao'],
            quantidade_parcelas_inadiplentes=row['quantidade_parcelas_inadiplentes'],valor_das_parcelas_inadiplentes=row['valor_das_parcelas_inadiplentes'],prazo_amortizacao=row['prazo_amortizacao'],
            prazo_amortizacao_remanescente=row['prazo_amortizacao_remanescente'],valor_financiamento=row['valor_financiamento'],dia_vencimento_parcela=row['dia_vencimento_parcela'],
            total_recebido=row['total_recebido'],total_a_receber=row['total_a_receber'],janeiro_2017=row['janeiro_2017'],fevereiro_2017=row['fevereiro_2017'],marco_2017=row['marco_2017'],
            abril_2017=row['abril_2017'],maio_2017=row['maio_2017'],junho_2017=row['junho_2017'],julho_2017=row['julho_2017'],agosto_2017=row['agosto_2017'],setembro_2017=row['setembro_2017'],
            outubro_2017=row['outubro_2017'],novembro_2017=row['novembro_2017'],dezembro_2017=row['dezembro_2017'],janeiro_2018=row['janeiro_2018'],fevereiro_2018=row['fevereiro_2018'],
            marco_2018=row['marco_2018'],abril_2018=row['abril_2018'],maio_2018=row['maio_2018'],junho_2018=row['junho_2018'],julho_2018=row['julho_2018'],agosto_2018=row['agosto_2018'],
            setembro_2018=row['setembro_2018'],outubro_2018=row['outubro_2018'],novembro_2018=row['novembro_2018'],dezembro_2018=row['dezembro_2018'],janeiro_2019=row['janeiro_2019'],
            fevereiro_2019=row['fevereiro_2019'],marco_2019=row['marco_2019'],abril_2019=row['abril_2019'],maio_2019=row['maio_2019'],junho_2019=row['junho_2019'],julho_2019=row['julho_2019'],
            agosto_2019=row['agosto_2019'],setembro_2019=row['setembro_2019'],outubro_2019=row['outubro_2019'],novembro_2019=row['novembro_2019'],dezembro_2019=row['dezembro_2019'],
            janeiro_2020=row['janeiro_2020'],fevereiro_2020=row['fevereiro_2020'],marco_2020=row['marco_2020'],abril_2020=row['abril_2020'],maio_2020=row['maio_2020'],junho_2020=row['junho_2020'],
            julho_2020=row['julho_2020'],agosto_2020=row['agosto_2020'],setembro_2020=row['setembro_2020'],outubro_2020=row['outubro_2020'],novembro_2020=row['novembro_2020'],dezembro_2020=row['dezembro_2020'],
            janeiro_2021=row['janeiro_2021'],fevereiro_2021=row['fevereiro_2021'],marco_2021=row['marco_2021'],abril_2021=row['abril_2021'],maio_2021=row['maio_2021'],junho_2021=row['junho_2021'],
            julho_2021=row['julho_2021'],agosto_2021=row['agosto_2021'],setembro_2021=row['setembro_2021'],outubro_2021=row['outubro_2021'],novembro_2021=row['novembro_2021'],dezembro_2021=row['dezembro_2021'],
            janeiro_2022=row['janeiro_2022'],fevereiro_2022=row['fevereiro_2022'],marco_2022=row['marco_2022'],abril_2022=row['abril_2022'],maio_2022=row['maio_2022'],junho_2022=row['junho_2022'],
            julho_2022=row['julho_2022'],agosto_2022=row['agosto_2022'],setembro_2022=row['setembro_2022'],outubro_2022=row['outubro_2022'],novembro_2022=row['novembro_2022'],dezembro_2022=row['dezembro_2022'],
            janeiro_2023=row['janeiro_2023'],fevereiro_2023=row['fevereiro_2023'],marco_2023=row['marco_2023'],abril_2023=row['abril_2023'],maio_2023=row['maio_2023'],junho_2023=row['junho_2023'],
            julho_2023=row['julho_2023'],agosto_2023=row['agosto_2023'],setembro_2023=row['setembro_2023'],outubro_2023=row['outubro_2023'],novembro_2023=row['novembro_2023'],dezembro_2023=row['dezembro_2023'],
            janeiro_2024=row['janeiro_2024'],fevereiro_2024=row['fevereiro_2024'],marco_2024=row['marco_2024'],abril_2024=row['abril_2024'],maio_2024=row['maio_2024'],junho_2024=row['junho_2024'],
            julho_2024=row['julho_2024'],agosto_2024=row['agosto_2024'],setembro_2024=row['setembro_2024'],outubro_2024=row['outubro_2024'],novembro_2024=row['novembro_2024'],dezembro_2024=row['dezembro_2024'],
            janeiro_2025=row['janeiro_2025'],fevereiro_2025=row['fevereiro_2025'],marco_2025=row['marco_2025'],abril_2025=row['abril_2025'],maio_2025=row['maio_2025'],junho_2025=row['junho_2025'],
            julho_2025=row['julho_2025'],agosto_2025=row['agosto_2025'],setembro_2025=row['setembro_2025'],outubro_2025=row['outubro_2025'],novembro_2025=row['novembro_2025'],
            dezembro_2025=row['dezembro_2025'],janeiro_2026=row['janeiro_2026'],fevereiro_2026=row['fevereiro_2026'],marco_2026=row['marco_2026'],abril_2026=row['abril_2026'],maio_2026=row['maio_2026'],
            junho_2026=row['junho_2026'],julho_2026=row['julho_2026'],agosto_2026=row['agosto_2026'],setembro_2026=row['setembro_2026'],outubro_2026=row['outubro_2026'],novembro_2026=row['novembro_2026'],
            dezembro_2026=row['dezembro_2026'],janeiro_2027=row['janeiro_2027'],fevereiro_2027=row['fevereiro_2027'],marco_2027=row['marco_2027'],abril_2027=row['abril_2027'],maio_2027=row['maio_2027'],
            junho_2027=row['junho_2027'],julho_2027=row['julho_2027'],agosto_2027=row['agosto_2027'],setembro_2027=row['setembro_2027'],outubro_2027=row['outubro_2027'],novembro_2027=row['novembro_2027'],
            dezembro_2027=row['dezembro_2027'],janeiro_2028=row['janeiro_2028'],fevereiro_2028=row['fevereiro_2028'],marco_2028=row['marco_2028'],abril_2028=row['abril_2028'],maio_2028=row['maio_2028'],
            junho_2028=row['junho_2028'],julho_2028=row['julho_2028'],agosto_2028=row['agosto_2028'],setembro_2028=row['setembro_2028'],outubro_2028=row['outubro_2028'],novembro_2028=row['novembro_2028'],
            dezembro_2028=row['dezembro_2028'],janeiro_2029=row['janeiro_2029'],fevereiro_2029=row['fevereiro_2029'],marco_2029=row['marco_2029'],abril_2029=row['abril_2029'],maio_2029=row['maio_2029'],
            junho_2029=row['junho_2029'],julho_2029=row['julho_2029'])
