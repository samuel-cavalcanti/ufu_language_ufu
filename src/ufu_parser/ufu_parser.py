from typing import Callable

from src.ufu_scanner.scanner import Scanner
from src.ufu_parser.syntactic_graphs.componets import *
from src.ufu_parser.scanner_consumer import ScannerConsumer
from src.ufu_parser.syntax_tree import SyntaxNode, SyntaxTree
from src.ufu_parser.parser_observer import Subject, ParserSubject, Observer


class UfuParser:
    __consumer: ScannerConsumer
    __scanner: Scanner
    __subject: Subject

    def __init__(self, scanner: Scanner):
        self.__scanner = scanner
        self.__init_graphs()
        self.__connect_graphs()
        self.__subject = ParserSubject()

    def run(self) -> SyntaxTree:
        self.__consumer = ScannerConsumer(self.__scanner, self.__subject)
        root = self.__sofware.parse(self.__consumer)

        return SyntaxTree(root)

    def register_observer(self, graph: type, observer: Observer):
        self.__subject.attach(graph, observer)

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
        self.__cmd_repeticao_while = CmdRepeticaoWhile()
        self.__cmd_repeticao_do_until = CmdRepeticaoDoUntil()
        self.__cmd_atribuicao = CmdAtribuicao()

        self.__id_ou_constante = IdOuConstante()

        self.__condicao = Condicao()

        self.__expressao_aritmetica_ou_const_ascii = ExpressaoAritmeticaOuConstAscii()

        self.__expressao_aritmetica = ExpressaoAritmetica()
        self.__expressao_aritmetica_linha = ExpressaoAritmeticaLinha()

        self.__termo = Termo()
        self.__termo_linha = TermoLinha()

        self.__fator = Fator()
        self.__add_ou_sub = AddOuSUb()
        self.__mult_ou_div = MultOuDiv()

    def __connect_graphs(self):
        self.__sofware.bloco = self.__bloco

        self.__bloco.conteudo_bloco = self.__conteudo_bloco

        self.__conteudo_bloco.lista_variaveis = self.__lista_variaveis
        self.__conteudo_bloco.lista_comandos = self.__lista_comandos

        self.__lista_variaveis.declaracao_de_variavel = self.__declaracao_de_variavel

        self.__lista_comandos.comando = self.__comando

        self.__declaracao_de_variavel.lista_ids = self.__lista_ids

        self.__comando.cmd_selecao = self.__cmd_selecao

        self.__comando.cmd_repeticao_while = self.__cmd_repeticao_while
        self.__comando.cmd_repeticao_do_until = self.__cmd_repeticao_do_until
        self.__comando.cmd_atribuicao = self.__cmd_atribuicao

        self.__lista_ids.mais_de_um_id = self.__mais_de_um_id

        self.__mais_de_um_id.lista_ids = self.__lista_ids

        self.__cmd_selecao.condicao = self.__condicao
        self.__cmd_selecao.bloco = self.__bloco
        self.__cmd_selecao.com_else = self.__com_else

        self.__com_else.bloco = self.__bloco

        self.__cmd_repeticao_while.condicao = self.__condicao
        self.__cmd_repeticao_while.bloco = self.__bloco

        self.__cmd_repeticao_do_until.bloco = self.__bloco
        self.__cmd_repeticao_do_until.condicao = self.__condicao

        self.__condicao.id_ou_constante = self.__id_ou_constante

        self.__cmd_atribuicao.expressao_aritmetica_ou_const_ascii = self.__expressao_aritmetica_ou_const_ascii

        self.__expressao_aritmetica_ou_const_ascii.expressao_aritmetica = self.__expressao_aritmetica

        self.__expressao_aritmetica.termo = self.__termo
        self.__expressao_aritmetica.expressao_aritmetica_linha = self.__expressao_aritmetica_linha

        self.__expressao_aritmetica_linha.add_ou_sub = self.__add_ou_sub
        self.__expressao_aritmetica_linha.termo = self.__termo

        self.__termo.fator = self.__fator
        self.__termo.termo_linha = self.__termo_linha

        self.__termo_linha.mult_ou_div = self.__mult_ou_div
        self.__termo_linha.fator = self.__fator

        self.__fator.expressao_aritmetica = self.__expressao_aritmetica
