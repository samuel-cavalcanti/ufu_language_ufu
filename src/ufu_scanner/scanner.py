from typing import Protocol

from src.ufu_token import UfuToken


class Scanner(Protocol):

    def get_token(self) -> UfuToken:
        """Retorna o próximo token um erro caso o token não seja reconhecido"""
