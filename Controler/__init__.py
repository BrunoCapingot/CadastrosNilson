from Factory import Factory
from Motor import Motor
from Model import Model
from View import View

if __name__ == '__main__':
    md = Model()
    vw = View()
    factory = Factory()
    motor = Motor()
    motor.adicionar_lista_de_execucao(execution_list=factory.(datalist=dict(
        csv_table=md.get_csv_table_geral_clientes_2025()
    ), Model=md, View=vw))
    motor.executar_motor()
    #md.apagar_dados_no_banco()
    #vw.mostrar_execucao(nome_processo='Inadiplencia_geral')
    #operador = Inadiplencia_geral(Model=md)
    #operador.extrair_dados_necessarios()
    #operador.cadastrar_dados_necessarios()
    #vw.mostrar_execucao(nome_processo='Cadastro_inad_estoque_bangalos_inadiplentes')
    #operador = Cadastro_inad_estoque_bangalos_inadiplentes(Model=md, View=vw)
    #operador.extrair_dados_necessarios()
    #operador.cadastrar_dados_necessarios()
    #vw.mostrar_execucao(nome_processo='EstoqueCotasDisponiveis')
    #operador = EstoqueCotasDisponiveis(Model=md, View=vw)
    #operador.extrair_dados_necessarios()
    #operador.cadastrar_dados_necessarios()
    #vw.mostrar_execucao(nome_processo='CadastroGerais2023')
    #operador = CadastroGerais2023(Model=md, View=vw)
    #operador = CadastroGerais2023(Model=md, View=vw)
    #operador = CadastroGerais2023NoBanco(Model=md, View=vw)
