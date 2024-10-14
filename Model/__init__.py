import datetime

import mysql.connector
import pandas as pd


class Model:

    def __init__(self):
        dbname = "plannextsistem"
        #dbname = "cadastrosnilson"
        usuario = "plannextsistem"
        #usuario = "root"
        password = "plannex2211"
        #password = "cpgt123789"
        localBanco = "mysql.plannextsistema.com.br"
        #localBanco = "localhost"
        self.cnx = mysql.connector.connect(host=localBanco, user=usuario, passwd=password, db=dbname, connection_timeout=5000)
        self.cursor = self.cnx.cursor()


    def insert_table_csv_clientes_cadastrados(self,cliente_codigo,cliente_nome,cliente_cpf_cnpj,cliente_endereco,cliente_cep,cliente_cidade,cliente_uf ,cliente_indexacao,cliente_status):
        self.cursor.execute(f"insert into table_csv_clientes_cadastrados (cliente_codigo,cliente_nome,cliente_cpf_cnpj,cliente_endereco,cliente_cep,cliente_cidade ,cliente_uf ,cliente_indexacao,cliente_status)VALUES('{estoque_torre}','{estoque_unidade}','{estoque_quartos}','{estoque_valor_venda}')")
        dado = self.cursor.fetchall()
        self.cnx.commit()


    def insert_table_csv_estoque_disponivel_com_valores(self,estoque_torre,estoque_unidade,estoque_quartos,estoque_valor_venda):
        self.cursor.execute(f"insert into table_csv_estoque_disponivel_com_valores (estoque_torre,estoque_unidade,estoque_quartos,estoque_valor_venda)VALUES('{estoque_torre}','{estoque_unidade}','{estoque_quartos}','{estoque_valor_venda}')")
        dado = self.cursor.fetchall()
        self.cnx.commit()


    def get_excel_estoque_cotas_disponiveis_novo(self):
        suport_list = list()
        data_base_estoque_disponivel = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\estoque cotas disponiveis_novo.xlsx')
        for index, row in data_base_estoque_disponivel.iterrows():
            estoque_torre = row['torre']
            estoque_unidade = row['unidade']
            estoque_quartos = row['quartos']
            estoque_valor_venda = row['valor venda']
            suport_list.append(dict(index=index, estoque_torre=estoque_torre, estoque_unidade=estoque_unidade,estoque_quartos=estoque_quartos, estoque_valor_venda=estoque_valor_venda))
        return suport_list

    def get_csv_geral_clientes_2025(self):
        dt_list = list()
        csv_table = pd.read_excel(r'C:\Users\CPGT\Desktop\CadastrosNilson\planilias\GeralClientes2025.xlsx')
        for index, row in csv_table.iterrows():
            dt_list.append(dict(
                contrato=str(row['Contrato']),
                status=str(row['Status']),
                empreendimento=str(row['Empreendimento']),
                unidade=str(row['Unidade']),
                area=str(row['Area m²']),
                nome=str(row['Nome']),
                cpf_cnpj=str(row['CPF/CNPJ']),
                data_nascimento=str(row['Data Nasc']),
                endereco=str(row['Endereço']),
                bairro=str(row['Bairro']),
                cidade=str(row['Cidade']),
                uf=str(row['UF']),
                cep=str(row['CEP']),
                juros_contrato=str(row['Juros Contrato']),
                indexador=str(row['indexador']),
                adm_carteira=str(row['admCarteira']),
                data_contrato=str(row['DataContrato']),
                valor_imovel=str(row['Valor Imóvel']),
                quantidade_de_entrada=str(row['QTD de entrada']),
                sistema_de_amortizacao=str(row['Sistema Amortização']),
                quantidade_parcelas_inadiplentes=str(row['Qtde de parcelas Inadimplentes']),
                valor_das_parcelas_inadiplentes=str(row['Valor das Parcelas Inadimplentes']),
                prazo_amortizacao=str(row['Prazo Amortização']),
                prazo_amortizacao_remanescente=str(row['Prazo Amortização Remanescente']),
                valor_financiamento=str(row['Valor Financiamento']),
                dia_vencimento_parcela=str(row['Dia Venc Parcela']),
                total_recebido=str(row['Total Recebido']),
                total_a_receber=str(row['Total a Receber']),

                janeiro_2017=str(row['01/01/2017']),
                fevereiro_2017=str(row['01/02/2017']),
                marco_2017=str(row['01/03/2017']),
                abril_2017=str(row['01/04/2017']),
                maio_2017=str(row['01/05/2017']),
                junho_2017=str(row['01/06/2017']),
                julho_2017=str(row['01/07/2017']),
                agosto_2017=str(row['01/08/2017']),
                setembro_2017=str(row['01/09/2017']),
                outubro_2017=str(row['01/10/2017']),
                novembro_2017=str(row['01/11/2017']),
                dezembro_2017=str(row['01/12/2017']),

                janeiro_2018=str(row['01/01/2018']),
                fevereiro_2018=str(row['01/02/2018']),
                marco_2018=str(row['01/03/2018']),
                abril_2018=str(row['01/04/2018']),
                maio_2018=str(row['01/05/2018']),
                junho_2018=str(row['01/06/2018']),
                julho_2018=str(row['01/07/2018']),
                agosto_2018=str(row['01/08/2018']),
                setembro_2018=str(row['01/09/2018']),
                outubro_2018=str(row['01/10/2018']),
                novembro_2018=str(row['01/11/2018']),
                dezembro_2018=str(row['01/12/2018']),

                janeiro_2019=str(row['01/01/2019']),
                fevereiro_2019=str(row['01/02/2019']),
                marco_2019=str(row['01/03/2019']),
                abril_2019=str(row['01/04/2019']),
                maio_2019=str(row['01/05/2019']),
                junho_2019=str(row['01/06/2019']),
                julho_2019=str(row['01/07/2019']),
                agosto_2019=str(row['01/08/2019']),
                setembro_2019=str(row['01/09/2019']),
                outubro_2019=str(row['01/10/2019']),
                novembro_2019=str(row['01/11/2019']),
                dezembro_2019=str(row['01/12/2019']),

                janeiro_2020=str(row['01/01/2020']),
                fevereiro_2020=str(row['01/02/2020']),
                marco_2020=str(row['01/03/2020']),
                abril_2020=str(row['01/04/2020']),
                maio_2020=str(row['01/05/2020']),
                junho_2020=str(row['01/06/2020']),
                julho_2020=str(row['01/07/2020']),
                agosto_2020=str(row['01/08/2020']),
                setembro_2020=str(row['01/09/2020']),
                outubro_2020=str(row['01/10/2020']),
                novembro_2020=str(row['01/11/2020']),
                dezembro_2020=str(row['01/12/2020']),

                janeiro_2021=str(row['01/01/2021']),
                fevereiro_2021=str(row['01/02/2021']),
                marco_2021=str(row['01/03/2021']),
                abril_2021=str(row['01/04/2021']),
                maio_2021=str(row['01/05/2021']),
                junho_2021=str(row['01/06/2021']),
                julho_2021=str(row['01/07/2021']),
                agosto_2021=str(row['01/08/2021']),
                setembro_2021=str(row['01/09/2021']),
                outubro_2021=str(row['01/10/2021']),
                novembro_2021=str(row['01/11/2021']),
                dezembro_2021=str(row['01/12/2021']),

                janeiro_2022=str(row['01/01/2022']),
                fevereiro_2022=str(row['01/02/2022']),
                marco_2022=str(row['01/03/2022']),
                abril_2022=str(row['01/04/2022']),
                maio_2022=str(row['01/05/2022']),
                junho_2022=str(row['01/06/2022']),
                julho_2022=str(row['01/07/2022']),
                agosto_2022=str(row['01/08/2022']),
                setembro_2022=str(row['01/09/2022']),
                outubro_2022=str(row['01/10/2022']),
                novembro_2022=str(row['01/11/2022']),
                dezembro_2022=str(row['01/12/2022']),

                janeiro_2023=str(row['01/01/2023']),
                fevereiro_2023=str(row['01/02/2023']),
                marco_2023=str(row['01/03/2023']),
                abril_2023=str(row['01/04/2023']),
                maio_2023=str(row['01/05/2023']),
                junho_2023=str(row['01/06/2023']),
                julho_2023=str(row['01/07/2023']),
                agosto_2023=str(row['01/08/2023']),
                setembro_2023=str(row['01/09/2023']),
                outubro_2023=str(row['01/10/2023']),
                novembro_2023=str(row['01/11/2023']),
                dezembro_2023=str(row['01/12/2023']),

                janeiro_2024=str(row['01/01/2024']),
                fevereiro_2024=str(row['01/02/2024']),
                marco_2024=str(row['01/03/2024']),
                abril_2024=str(row['01/04/2024']),
                maio_2024=str(row['01/05/2024']),
                junho_2024=str(row['01/06/2024']),
                julho_2024=str(row['01/07/2024']),
                agosto_2024=str(row['01/08/2024']),
                setembro_2024=str(row['01/09/2024']),
                outubro_2024=str(row['01/10/2024']),
                novembro_2024=str(row['01/11/2024']),
                dezembro_2024=str(row['01/12/2024']),

                janeiro_2025=str(row['01/01/2025']),
                fevereiro_2025=str(row['01/02/2025']),
                marco_2025=str(row['01/03/2025']),
                abril_2025=str(row['01/04/2025']),
                maio_2025=str(row['01/05/2025']),
                junho_2025=str(row['01/06/2025']),
                julho_2025=str(row['01/07/2025']),
                agosto_2025=str(row['01/08/2025']),
                setembro_2025=str(row['01/09/2025']),
                outubro_2025=str(row['01/10/2025']),
                novembro_2025=str(row['01/11/2025']),
                dezembro_2025=str(row['01/12/2025']),

                janeiro_2026=str(row['01/01/2026']),
                fevereiro_2026=str(row['01/02/2026']),
                marco_2026=str(row['01/03/2026']),
                abril_2026=str(row['01/04/2026']),
                maio_2026=str(row['01/05/2026']),
                junho_2026=str(row['01/06/2026']),
                julho_2026=str(row['01/07/2026']),
                agosto_2026=str(row['01/08/2026']),
                setembro_2026=str(row['01/09/2026']),
                outubro_2026=str(row['01/10/2026']),
                novembro_2026=str(row['01/11/2026']),
                dezembro_2026=str(row['01/12/2026']),

                janeiro_2027=str(row['01/01/2027']),
                fevereiro_2027=str(row['01/02/2027']),
                marco_2027=str(row['01/03/2027']),
                abril_2027=str(row['01/04/2027']),
                maio_2027=str(row['01/05/2027']),
                junho_2027=str(row['01/06/2027']),
                julho_2027=str(row['01/07/2027']),
                agosto_2027=str(row['01/08/2027']),
                setembro_2027=str(row['01/09/2027']),
                outubro_2027=str(row['01/10/2027']),
                novembro_2027=str(row['01/11/2027']),
                dezembro_2027=str(row['01/12/2027']),

                janeiro_2028=str(row['01/01/2028']),
                fevereiro_2028=str(row['01/02/2028']),
                marco_2028=str(row['01/03/2028']),
                abril_2028=str(row['01/04/2028']),
                maio_2028=str(row['01/05/2028']),
                junho_2028=str(row['01/06/2028']),
                julho_2028=str(row['01/07/2028']),
                agosto_2028=str(row['01/08/2028']),
                setembro_2028=str(row['01/09/2028']),
                outubro_2028=str(row['01/10/2028']),
                novembro_2028=str(row['01/11/2028']),
                dezembro_2028=str(row['01/12/2028']),

                janeiro_2029=str(row['01/01/2029']),
                fevereiro_2029=str(row['01/02/2029']),
                marco_2029=str(row['01/03/2029']),
                abril_2029=str(row['01/04/2029']),
                maio_2029=str(row['01/05/2029']),
                junho_2029=str(row['01/06/2029']),
                julho_2029=str(row['01/07/2029']),


            ))
        return dt_list

    def insert_into_table_csv_cliente_geral_2025(self, contrato,status,empreendimento,unidade,area,nome,cpf_cnpj,data_nascimento,endereco,
        bairro,cidade,uf,cep,juros_contrato,indexador,adm_carteira,data_contrato,valor_imovel,quantidade_de_entrada,sistema_de_amortizacao,quantidade_parcelas_inadiplentes,
        valor_das_parcelas_inadiplentes,prazo_amortizacao,prazo_amortizacao_remanescente,valor_financiamento,dia_vencimento_parcela,total_recebido,total_a_receber,
        janeiro_2017,fevereiro_2017,marco_2017,abril_2017,maio_2017,junho_2017,julho_2017,agosto_2017,setembro_2017,outubro_2017,novembro_2017,dezembro_2017,janeiro_2018,
        fevereiro_2018,marco_2018,abril_2018,maio_2018,junho_2018,julho_2018,agosto_2018,setembro_2018,outubro_2018,novembro_2018,dezembro_2018,janeiro_2019,fevereiro_2019,
        marco_2019,abril_2019,maio_2019,junho_2019,julho_2019,agosto_2019,setembro_2019,outubro_2019,novembro_2019,dezembro_2019,janeiro_2020,fevereiro_2020,marco_2020,abril_2020,
        maio_2020,junho_2020,julho_2020,agosto_2020,setembro_2020,outubro_2020,novembro_2020,dezembro_2020,janeiro_2021,fevereiro_2021,marco_2021,abril_2021,maio_2021,junho_2021,
        julho_2021,agosto_2021,setembro_2021,outubro_2021,novembro_2021,dezembro_2021,janeiro_2022,fevereiro_2022,marco_2022,abril_2022,maio_2022,junho_2022,julho_2022,agosto_2022,
        setembro_2022,outubro_2022,novembro_2022,dezembro_2022,janeiro_2023,fevereiro_2023,marco_2023,abril_2023,maio_2023,junho_2023,julho_2023,agosto_2023,setembro_2023,outubro_2023,
        novembro_2023,dezembro_2023,janeiro_2024,fevereiro_2024,marco_2024,abril_2024,maio_2024,junho_2024,julho_2024,agosto_2024,setembro_2024,outubro_2024,novembro_2024,dezembro_2024,
        janeiro_2025,fevereiro_2025,marco_2025,abril_2025,maio_2025,junho_2025,julho_2025,agosto_2025,setembro_2025,outubro_2025,novembro_2025,dezembro_2025,janeiro_2026,fevereiro_2026,
        marco_2026,abril_2026,maio_2026,junho_2026,julho_2026,agosto_2026,setembro_2026,outubro_2026,novembro_2026,dezembro_2026,janeiro_2027,fevereiro_2027,marco_2027,abril_2027,maio_2027,
        junho_2027,julho_2027,agosto_2027,setembro_2027,outubro_2027,novembro_2027,dezembro_2027,janeiro_2028,fevereiro_2028,marco_2028,abril_2028,maio_2028,junho_2028,julho_2028,agosto_2028,
        setembro_2028,outubro_2028,novembro_2028,dezembro_2028,janeiro_2029,fevereiro_2029,marco_2029,abril_2029,maio_2029,junho_2029,julho_2029):



        self.cursor.execute(
            f"""insert into table_csv_geral_clientes_2025(
            contrato,status_tabela,empreendimento,unidade,area,nome,CPF_CNPJ,data_nascimento,endereço,bairro,cidade,uf,
            cep,juros_contrato,indexador,adm_carteira,data_contrato,valor_imovel,quantidade_de_entrada,sistema_amortização,quantidade_parcelas_inadiplentes,
            valor_das_parcelas_inadimplentes,prazo_amortização,prazo_amortização_remanescente,valor_financiamento,dia_venc_parcela,total_recebido,total_a_receber,
            `01/01/2017`, `01/02/2017`, `01/03/2017`, `01/04/2017`, `01/05/2017`, `01/06/2017`,
            `01/07/2017`, `01/08/2017`, `01/09/2017`, `01/10/2017`, `01/11/2017`, `01/12/2017`, 
            `01/01/2018`, `01/02/2018`, `01/03/2018`, `01/04/2018`, `01/05/2018`, `01/06/2018`, 
            `01/07/2018`, `01/08/2018`, `01/09/2018`, `01/10/2018`, `01/11/2018`, `01/12/2018`, 
            `01/01/2019`, `01/02/2019`, `01/03/2019`, `01/04/2019`, `01/05/2019`, `01/06/2019`, 
            `01/07/2019`, `01/08/2019`, `01/09/2019`, `01/10/2019`, `01/11/2019`, `01/12/2019`, 
            `01/01/2020`, `01/02/2020`, `01/03/2020`, `01/04/2020`, `01/05/2020`, `01/06/2020`, 
            `01/07/2020`, `01/08/2020`, `01/09/2020`, `01/10/2020`, `01/11/2020`, `01/12/2020`, 
            `01/01/2021`, `01/02/2021`, `01/03/2021`, `01/04/2021`, `01/05/2021`, `01/06/2021`, 
            `01/07/2021`, `01/08/2021`, `01/09/2021`, `01/10/2021`, `01/11/2021`, `01/12/2021`, 
            `01/01/2022`, `01/02/2022`, `01/03/2022`, `01/04/2022`, `01/05/2022`, `01/06/2022`, 
            `01/07/2022`, `01/08/2022`, `01/09/2022`, `01/10/2022`, `01/11/2022`, `01/12/2022`, 
            `01/01/2023`, `01/02/2023`, `01/03/2023`, `01/04/2023`, `01/05/2023`, `01/06/2023`, 
            `01/07/2023`, `01/08/2023`, `01/09/2023`, `01/10/2023`, `01/11/2023`, `01/12/2023`, 
            `01/01/2024`, `01/02/2024`, `01/03/2024`, `01/04/2024`, `01/05/2024`, `01/06/2024`, 
            `01/07/2024`, `01/08/2024`, `01/09/2024`, `01/10/2024`, `01/11/2024`, `01/12/2024`, 
            `01/01/2025`, `01/02/2025`, `01/03/2025`, `01/04/2025`, `01/05/2025`, `01/06/2025`, 
            `01/07/2025`, `01/08/2025`, `01/09/2025`, `01/10/2025`, `01/11/2025`, `01/12/2025`, 
            `01/01/2026`, `01/02/2026`, `01/03/2026`, `01/04/2026`, `01/05/2026`, `01/06/2026`, 
            `01/07/2026`, `01/08/2026`, `01/09/2026`, `01/10/2026`, `01/11/2026`, `01/12/2026`, 
            `01/01/2027`, `01/02/2027`, `01/03/2027`, `01/04/2027`, `01/05/2027`, `01/06/2027`, 
            `01/07/2027`, `01/08/2027`, `01/09/2027`, `01/10/2027`, `01/11/2027`, `01/12/2027`, 
            `01/01/2028`, `01/02/2028`, `01/03/2028`, `01/04/2028`, `01/05/2028`, `01/06/2028`, 
            `01/07/2028`, `01/08/2028`, `01/09/2028`, `01/10/2028`, `01/11/2028`, `01/12/2028`, 
            `01/01/2029`, `01/02/2029`, `01/03/2029`, `01/04/2029`, `01/05/2029`, `01/06/2029`, 
            `01/07/2029`)VALUES(
            '{contrato}','{status}','{empreendimento}','{unidade}','{area}','{nome}','{cpf_cnpj}','{data_nascimento}','{endereco}','{bairro}','{cidade}',
            '{uf}','{cep}','{juros_contrato}','{indexador}','{adm_carteira}','{data_contrato}','{valor_imovel}','{quantidade_de_entrada}','{sistema_de_amortizacao}',
            '{quantidade_parcelas_inadiplentes}','{valor_das_parcelas_inadiplentes}','{prazo_amortizacao}','{prazo_amortizacao_remanescente}','{valor_financiamento}',
            '{dia_vencimento_parcela}','{total_recebido}','{total_a_receber}','{janeiro_2017}','{fevereiro_2017}','{marco_2017}','{abril_2017}','{maio_2017}','{junho_2017}','{julho_2017}','{agosto_2017}',
            '{setembro_2017}','{outubro_2017}','{novembro_2017}','{dezembro_2017}','{janeiro_2018}','{fevereiro_2018}','{marco_2018}','{abril_2018}','{maio_2018}','{junho_2018}','{julho_2018}',
            '{agosto_2018}','{setembro_2018}','{outubro_2018}','{novembro_2018}','{dezembro_2018}','{janeiro_2019}','{fevereiro_2019}','{marco_2019}','{abril_2019}','{maio_2019}','{junho_2019}',
            '{julho_2019}','{agosto_2019}','{setembro_2019}','{outubro_2019}','{novembro_2019}','{dezembro_2019}','{janeiro_2020}','{fevereiro_2020}','{marco_2020}','{abril_2020}', '{maio_2020}',
            '{junho_2020}','{julho_2020}','{agosto_2020}','{setembro_2020}','{outubro_2020}','{novembro_2020}','{dezembro_2020}','{janeiro_2021}','{fevereiro_2021}','{marco_2021}','{abril_2021}','{maio_2021}',
            '{junho_2021}', '{julho_2021}','{agosto_2021}','{setembro_2021}','{outubro_2021}','{novembro_2021}','{dezembro_2021}','{janeiro_2022}','{fevereiro_2022}','{marco_2022}','{abril_2022}','{maio_2022}',
            '{junho_2022}','{julho_2022}','{agosto_2022}', '{setembro_2022}','{outubro_2022}','{novembro_2022}','{dezembro_2022}','{janeiro_2023}','{fevereiro_2023}','{marco_2023}','{abril_2023}','{maio_2023}',
            '{junho_2023}','{julho_2023}','{agosto_2023}','{setembro_2023}','{outubro_2023}', '{novembro_2023}','{dezembro_2023}','{janeiro_2024}','{fevereiro_2024}','{marco_2024}','{abril_2024}','{maio_2024}',
            '{junho_2024}','{julho_2024}','{agosto_2024}','{setembro_2024}','{outubro_2024}','{novembro_2024}','{dezembro_2024}', '{janeiro_2025}','{fevereiro_2025}','{marco_2025}','{abril_2025}','{maio_2025}',
            '{junho_2025}','{julho_2025}','{agosto_2025}','{setembro_2025}','{outubro_2025}','{novembro_2025}','{dezembro_2025}','{janeiro_2026}','{fevereiro_2026}', '{marco_2026}','{abril_2026}','{maio_2026}',
            '{junho_2026}','{julho_2026}','{agosto_2026}','{setembro_2026}','{outubro_2026}','{novembro_2026}','{dezembro_2026}','{janeiro_2027}','{fevereiro_2027}','{marco_2027}','{abril_2027}','{maio_2027}',
            '{junho_2027}','{julho_2027}','{agosto_2027}','{setembro_2027}','{outubro_2027}','{novembro_2027}','{dezembro_2027}','{janeiro_2028}','{fevereiro_2028}','{marco_2028}','{abril_2028}','{maio_2028}',
            '{junho_2028}','{julho_2028}','{agosto_2028}', '{setembro_2028}','{outubro_2028}','{novembro_2028}','{dezembro_2028}','{janeiro_2029}','{fevereiro_2029}','{marco_2029}','{abril_2029}','{maio_2029}',
            '{junho_2029}','{julho_2029}'
            )"""
        )
        dado = self.cursor.fetchall()
        self.cnx.commit()



    def insert_into_disponiveis(self,unidade_nome,unidade_localizacao,unidade_valor,unidade_quantidade_quartos):
        self.cursor.execute(f"insert into table_disponiveis (unidade_nome,unidade_localizacao,unidade_valor,unidade_quantidade_quartos)VALUES('{unidade_nome}','{unidade_localizacao}','{unidade_valor}','{unidade_quantidade_quartos}')")
        dado = self.cursor.fetchall()
        self.cnx.commit()

    def insert_into_relfinal(self,condominio,unidade,numerocontrato,andar,torre,statusunidade,totalrecebido,saldoatrasado,saldoavencer,parcelasvencidas,parcelasavencer,total,parcelachave,quantidadedisponiveis,nome_cliente,inadimplencia,qtd_quarto,recebivel):
        self.cursor.execute(f"INSERT INTO relfinal(condominio,unidade,numerocontrato,andar,torre,statusunidade,totalrecebido,saldoatrasado,saldoavencer,parcelasvencidas,parcelasavencer,total,parcelachave,quantidadedisponiveis,nome_cliente,inadimplencia,qtd_quarto,recebivel)VALUES({condominio},{unidade},{numerocontrato},{andar},{torre},{statusunidade},{totalrecebido},{saldoatrasado},{saldoavencer},{parcelasvencidas},{parcelasavencer},{total},{parcelachave},{quantidadedisponiveis},{nome_cliente},{inadimplencia},{qtd_quarto},{recebivel})")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def get_cliente_nome_geral_2023(self,nome:str):
        self.cursor.execute(f"select * from table_cvs_relatorio_geral_clientes_2023 where cliente_nome='{nome}'")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def insert_from_where(self,tabela,coluna,dado):
        self.cursor.execute(f"insert in {tabela} values()")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def apagar_dados_no_banco(self,tabela):
        del_querry_list = ['set sql_safe_updates = 0', f'delete from {tabela}']
        self.cursor.execute(del_querry_list[0])
        self.cnx.commit()
        self.cursor.fetchall()
        self.cursor.execute(del_querry_list[1])
        self.cnx.commit()
        self.cursor.fetchall()


    def get_table_csv_bangalo_disponivel_com_valor(self):
        self.cursor.execute("select * from table_csv_bangalo_disponivel_com_valor")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def get_table_csv_estoque_disponivel_com_valores(self):
        self.cursor.execute("select * from table_csv_estoque_disponivel_com_valores")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado


    def get_table_cvs_relatorio_geral_clientes_2023(self):
        self.cursor.execute("select * from table_cvs_relatorio_geral_clientes_2023")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def get_table_cvs_relatorio_geral_clientes_2023_padronizada(self):
        self.cursor.execute("select * from table_cvs_relatorio_geral_clientes_2023")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def get_table_cvs_inadiplencia_geral(self):
        self.cursor.execute("select * from table_csv_inadiplencia_geral")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado


    def get_table_cvs_parcela_chave(self):
        self.cursor.execute("select * from table_csv_cliente_parcela_chave")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def get_table_csv_dados_de_pagamento_padrao(self):
        self.cursor.execute("select * from table_csv_dados_de_pagamento_padrao")
        dado = self.cursor.fetchall()
        self.cnx.commit()
        return dado

    def inserir_dados_no_banco(self, querry_list: list, index) -> list:
        while querry_list.__len__() != 0:
            self.cursor.execute(querry_list.pop())
            self.cnx.commit()
            self.cursor.fetchall()
        return querry_list
