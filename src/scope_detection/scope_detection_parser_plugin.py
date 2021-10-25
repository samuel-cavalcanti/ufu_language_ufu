from src.ufu_parser import UfuParser
from src.ufu_parser.parser_observer import Observer, ObserverBuilder
from src.ufu_parser.syntax_tree import SyntaxNode
from src.ufu_parser.syntactic_graphs.componets import *
from .scope_detection import ScopeDetection
from src.ufu_token import UfuTokenType
from typing import Optional
from src.symbol_tables import Symbol


class ScopeDetectionPlugin:
    scope_detection: ScopeDetection

    def __init__(self):
        self.scope_detection = ScopeDetection()

    def __on_create_block(self, node: SyntaxNode):
        self.scope_detection.new_scope(name=f"block:{id(node)}")

    def __on_complete_block(self, _: SyntaxNode):
        self.scope_detection.back_scope()
        """
            ao final de um símbolo não terminal bloco
            o escopo atual volta para o seu antecessor se
            não houver antecessor ,então o escopo é o Global e não há o que voltar.
        """

    def __on_complete_variable_declaration(self, node: SyntaxNode):
        information: dict = node.information
        variable_type = information.get(UfuTokenType.TYPE_VARIABLE.value)
        ids = information.get(UfuTokenType.ID.value)
        """
                   um símbolo não terminal DeclaracaoDeVariavel deriva em:
                   DeclaracaoDeVariavel → TipoDeVariavel : listaIds ;
                   logo o seu nó deve conter o tipo da ou das variáveis e uma lista de ids
                   informações essas que viram símbolos da tabela do escopo atual
                  
        """

        for variable_id in ids:
            self.scope_detection.insert_symbol_on_current_scope(Symbol(variable_type, variable_id, ''))

    def __verify_id(self, node: SyntaxNode):
        information: dict = node.information

        variable_id: Optional[str] = information.get(UfuTokenType.ID.value)
        """
            um node pode ou não conter um uma variável ID
            como no caso do símbolo não terminal Fator,
            Fator ->  id | ConstInt | ConstReal
            ou seja, possa ser que esse nó derive em um ID 
        """
        if not variable_id:
            return

        self.scope_detection.verify_variable_declaration(variable_id)

    def build(self, parser: UfuParser):
        block_observer = ObserverBuilder() \
            .set_on_create(self.__on_create_block) \
            .set_on_complete(self.__on_complete_block) \
            .build()

        parser.register_observer(Bloco, block_observer)

        variable_declaration_observer = ObserverBuilder() \
            .set_on_complete(self.__on_complete_variable_declaration) \
            .build()

        parser.register_observer(DeclaracaoDeVariavel, variable_declaration_observer)

        verify_id_observer = ObserverBuilder() \
            .set_on_complete(self.__verify_id) \
            .build()

        """cmdAtribuicao → id:=hexpressaoAritmeticaOuConstAsciii;"""
        parser.register_observer(CmdAtribuicao, verify_id_observer)

        """fator → id | ConstInt | ConstReal |(expressaoAritmetica)"""
        parser.register_observer(Fator, verify_id_observer)

        "idOUConstante → id | ConstInt | ConstReal | ConstAscii"
        parser.register_observer(IdOuConstante, verify_id_observer)
