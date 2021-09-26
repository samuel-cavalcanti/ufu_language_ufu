from src.ufu_token.ufu_token import UfuToken
from src.source_program.source_program import SourceProgram
from typing import Protocol, Optional
from abc import abstractmethod




class TokenScan(Protocol):

    @abstractmethod
    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        raise NotImplementedError()
