from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class GraphvizNode:
    name: str
    children: list
    information: Optional[Any]
    uuid: int
