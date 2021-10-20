class SyntaxNode:
    name: str
    childs: list

    def __init__(self, name: str):
        self.name = name
        self.childs = list()
