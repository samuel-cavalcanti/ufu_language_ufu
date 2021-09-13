from typing import Protocol, Optional
from abc import abstractmethod

try:
    from ..source_program import TensorSourceProgram,SourceProgram
    from ..ufu_token import UfuToken, UfuTokenType
except ImportError:
    from src.source_program import SourceProgram, TensorSourceProgram
    from src.ufu_token import UfuToken, UfuTokenType


class TokenScan(Protocol):

    @abstractmethod
    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        raise NotImplementedError()
