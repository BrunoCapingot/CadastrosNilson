from Factory.CadastroCsvBanco.CadastroBancoInadiplentesGeral import CadastroBancoInadiplentesGeral
from Factory.CadastroCsvBanco.CadastroBancoBangalosInadiplentes import CadastroBancoBangalosInadiplentes
from Factory.CadastroCsvBanco.CadastroBancoCotasDisponiveisComValores import CadastroBancoCotasDisponiveisComValores
from Factory.CadastroCsvBanco.CadastroBancoBangalosDisponiveisComValor import CadastroBancoBangalosDisponiveisComValor
from Factory.CadastroCsvBanco.CadastroBancoEstoqueIntegralComValores import CadastroBancoEstoqueIntegralComValores
from Factory.CadastroCsvBanco.CadastroBancoClientesParcelaChave import CadastroBancoClientesParcelaChave
from Factory.CadastroCsvBanco.CadastroBancoRelatorioGeralClientes2023 import CadastroBancoRelatorioGeralClientes2023
from Factory.CadastroCsvBanco.CadastroDadosBancoGerais2023Padronizada import CadastroDadosBancoGerais2023Padronizada
from Factory.CadastroCsvBanco.CadastroBancoDadosPagamentoPadrao import CadastroBancoDadosPagamentoPadrao
from Factory.CadastroCsvBanco.CadastroBancoGeralClientes2025 import CadastroBancoGeralClientes2025
from Factory.CadastroCsvBanco.CadastroBancoDisponiveis import CadastroBancoDisponiveis
from Factory.CadastroCsvBanco.CadastroBancoClientesCadastrados import CadastroBancoClientesCadastrados

from Factory.TestesComBanco import TestesComBanco

from Factory.CadastroCsvSite.CadastroSiteCotasDisponiveisComValores import CadastroSiteCotasDisponiveisComValores
from Factory.CadastroCsvSite.CadastroDadosSiteGerais2023 import CadastroDadosSiteGerais2023
from Factory.CadastroCsvSite.CadastroDadosSiteGerais2023Padrao import CadastroDadosSiteGerais2023Padrao


class Factory:
    def __init__(self):
        pass

    def cadastro_site_disponivels(self,datalist,Model,View):
        return [CadastroBancoDisponiveis(nome='CadastroBancoDisponiveis', prioridade=9,datalist=datalist, Model=Model, View=View)]

    def cadastro_clientes_cadastrados(self,datalist,Model,View):
        return [CadastroBancoClientesCadastrados(nome='CadastroBancoClientesCadastrados', prioridade=9,datalist=datalist, Model=Model, View=View)]

    def cadastro_banco_csv_table_geral_2025(self, datalist, Model, View):
        return [CadastroBancoGeralClientes2025(nome='CadastroBancoGeralClientes2025', prioridade=9, datalist=datalist['csv_table'], Model=Model, View=View)]

    def executar_subida_dados_from_relfinal(self,data_dict):
        return [CadastroSiteCotasDisponiveisComValores(nome='CadastroSiteCotasDisponiveisComValores',prioridade=9, data_list=data_dict['CadastroSiteCotasDisponiveisComValores'])]

    def executar_cruzamento_de_dados(self):
        return [CadastroDadosSiteGerais2023(nome='CadastroDadosSiteGerais2023',prioridade=9)]

    def executar_cadastro_tabela_padrao(self):
        return [CadastroDadosSiteGerais2023Padrao(nome='CadastroDadosSiteGerais2023Padrao',prioridade=9)]

    def executar_conversa_com_banco(self):
        return [TestesComBanco(nome='TestesComBanco',prioridade=9)]

    def executar_padronizacao_de_dados(self):
        return [CadastroDadosBancoGerais2023Padronizada(nome='CadastroDadosBancoGerais2023Padronizada', prioridade=9)]


    def cadastro_csv_geral_no_banco(self,datalist,Model,View)->list:
        return [
            #CadastroBancoRelatorioGeralClientes2023(nome='CadastroBancoRelatorioGeralClientes2023', prioridade=2),
            #CadastroBancoInadiplentesGeral(nome='CadastroBancoInadiplentesGeral',prioridade=9),
            #CadastroBancoDadosPagamentoPadrao(nome='CadastroBancoDadosPagamentoPadrao',prioridade=8),
            #CadastroBancoClientesParcelaChave(nome='CadastroBancoClientesParcelaChave', prioridade=3),
            #CadastroBancoBangalosInadiplentes(nome='CadastroBancoBangalosInadiplentes',prioridade=8),
            #CadastroBancoEstoqueIntegralComValores(nome='CadastroBancoEstoqueIntegralComValores',prioridade=7),
            CadastroBancoCotasDisponiveisComValores(nome='CadastroBancoCotasDisponiveisComValores',prioridade=6,datalist=datalist, Model=Model, View=View),
            #CadastroBancoBangalosDisponiveisComValor(nome='CadastroBancoBangalosDisponiveisComValor',prioridade=4),
            #CadastroBancoInadiplentesGeral(nome='CadastroBancoInadiplentesGeral',prioridade=1),


                ]