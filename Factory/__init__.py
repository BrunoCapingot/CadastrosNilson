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

from Factory.CadastroCsvSite.CadastroSiteInadiplentes import CadastroSiteInadiplentes
from Factory.CadastroCsvSite.CadastroSiteCotasDisponiveisComValores import CadastroSiteCotasDisponiveisComValores
from Factory.CadastroCsvSite.CadastroDadosSiteGerais2023 import CadastroDadosSiteGerais2023
from Factory.CadastroCsvSite.CadastroDadosSiteGerais2023Padrao import CadastroDadosSiteGerais2023Padrao


class Factory:
    def __init__(self):
        pass

    def cadastro_site_inadiplentes(self, datalist, Model, View) -> list:
        return [
            CadastroSiteInadiplentes(nome='CadastroSiteInadiplentes', prioridade=9, datalist=datalist, Model=Model, View=View)
        ]

    def cadastro_site_disponivels(self, datalist, Model, View) -> list:
        return [CadastroBancoDisponiveis(nome='CadastroBancoDisponiveis', prioridade=9,datalist=datalist, Model=Model, View=View)]

    def cadastro_clientes_cadastrados(self, datalist, Model, View) -> list:
        return [CadastroBancoClientesCadastrados(nome='CadastroBancoClientesCadastrados', prioridade=9,datalist=datalist, Model=Model, View=View)]

    def cadastro_csv_geral_no_banco(self, datalist, Model, View) -> list:
        return [
            #CadastroBancoRelatorioGeralClientes2023(nome='CadastroBancoRelatorioGeralClientes2023', prioridade=2),
            #CadastroBancoInadiplentesGeral(nome='CadastroBancoInadiplentesGeral',prioridade=9),
            #CadastroBancoDadosPagamentoPadrao(nome='CadastroBancoDadosPagamentoPadrao',prioridade=8),
            #CadastroBancoClientesParcelaChave(nome='CadastroBancoClientesParcelaChave', prioridade=3),
            #CadastroBancoBangalosInadiplentes(nome='CadastroBancoBangalosInadiplentes',prioridade=8),
            #CadastroBancoEstoqueIntegralComValores(nome='CadastroBancoEstoqueIntegralComValores',prioridade=7, datalist=datalist['csv_table'], Model=Model, View=View),
            #CadastroBancoCotasDisponiveisComValores(nome='CadastroBancoCotasDisponiveisComValores',prioridade=6,datalist=datalist, Model=Model, View=View),
            #CadastroBancoBangalosDisponiveisComValor(nome='CadastroBancoBangalosDisponiveisComValor',prioridade=4),
            #CadastroBancoInadiplentesGeral(nome='CadastroBancoInadiplentesGeral',prioridade=1),


                ]