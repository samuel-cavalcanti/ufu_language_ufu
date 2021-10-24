from typing import Any, Optional
from src.ufu_token import UfuToken


class SyntaxNode:
    name: str
    children: list
    information = Optional[dict]

    def __init__(self, name: str, information=None):
        self.name = name
        self.children = list()
        self.information = information

    @staticmethod
    def from_ufu_token(token: UfuToken):
        return SyntaxNode(token.type.name, token.content)

    def __str__(self):
        return f"name: {self.name} children: {self.children}"
