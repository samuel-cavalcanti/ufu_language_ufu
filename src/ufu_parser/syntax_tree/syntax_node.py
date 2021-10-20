from typing import Any, Optional


class SyntaxNode:
    name: str
    children: list

    def __init__(self, name: str):
        self.name = name
        self.children = list()

    def __str__(self):
        return f"name: {self.name} children: {self.children}"
