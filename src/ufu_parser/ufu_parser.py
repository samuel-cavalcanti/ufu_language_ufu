from src.ufu_scanner.scanner import Scanner
from src.ufu_parser.syntactic_graphs.componets import *
from src.ufu_parser.scanner_consumer import ScannerConsumer


class UfuParser:
    __consumer: ScannerConsumer

    def __init__(self, scanner: Scanner):
        self.__consumer = ScannerConsumer(scanner)
        self.__init_graphs()
        self.__connect_graphs()

    def __init_graphs(self):
        self.__sofware = Software()

        self.__bloco = Bloco()
        self.__conteudo_bloco = ConteudoBloco()

        self.__lista_variaveis = ListaVariaveis()
        self.__lista_comandos = ListaComandos()

        self.__declaracao_de_variavel = DeclaracaoDeVariavel()

        self.__comando = Comando()
        self.__lista_ids = ListaIDs()
        self.__mais_de_um_id = MaisDeUmID()

        self.__cmd_selecao = CmdSelecao()
        self.__com_else = ComElse()
        self.__cmd_repeticao = CmdRepeticao()
        self.__cmd_repeticao_while = CmdRepeticaoWhile()
        self.__cmd_repeticao_do_until = CmdRepeticaoDoUntil()
        self.__cmd_atribuicao = CmdAtribuicao()

        self.__condicao = Condicao()
        self.__condicao_linha = CondicaoLinha()

        self.__expressao = Expressao()
        self.__expressao_linha = ExpressaoLinha()
        self.__id_ou_constante = IdOuConstante()

    def __connect_graphs(self):
        self.__sofware.bloco = self.__bloco

        self.__bloco.conteudo_bloco = self.__conteudo_bloco

        self.__conteudo_bloco.lista_variaveis = self.__lista_variaveis
        self.__conteudo_bloco.lista_comandos = self.__lista_comandos

        self.__lista_variaveis.declaracao_de_variavel = self.__declaracao_de_variavel

        self.__lista_comandos.comando = self.__comando

        self.__declaracao_de_variavel.lista_ids = self.__lista_ids

        self.__comando.cmd_selecao = self.__cmd_selecao
        self.__comando.cmd_repeticao = self.__cmd_repeticao
        self.__comando.cmd_atribuicao = self.__cmd_atribuicao

        self.__lista_ids.mais_de_um_id = self.__mais_de_um_id

        self.__mais_de_um_id.lista_ids = self.__lista_ids

        self.__cmd_selecao.condicao = self.__condicao
        self.__cmd_selecao.bloco = self.__bloco
        self.__cmd_selecao.com_else = self.__com_else

        self.__com_else.bloco = self.__bloco

        self.__cmd_repeticao.cmd_repeticao_while = self.__cmd_repeticao_while
        self.__cmd_repeticao.cmd_repeticao_do_until = self.__cmd_repeticao_do_until

        self.__cmd_repeticao_while.condicao = self.__condicao
        self.__cmd_repeticao_while.bloco = self.__bloco

        self.__cmd_repeticao_do_until.bloco = self.__bloco
        self.__cmd_repeticao_do_until.condicao = self.__condicao

        self.__cmd_atribuicao.expressao = self.__expressao

        self.__condicao.id_ou_constante = self.__id_ou_constante
        self.__condicao.condicao_linha = self.__condicao_linha

        self.__condicao_linha.condicao = self.__condicao

        self.__expressao.id_ou_constante = self.__id_ou_constante
        self.__expressao.expressao_linha = self.__expressao_linha

    def run(self):
        self.__sofware.parse(self.__consumer)
