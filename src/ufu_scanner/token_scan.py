from src.ufu_token.ufu_token import UfuToken
from src.source_program.source_program import SourceProgram
from typing import Protocol, Optional


class TokenScan(Protocol):

    def scan(self, source: SourceProgram) -> Optional[UfuToken]:
        ...
