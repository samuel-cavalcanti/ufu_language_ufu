from typing import Optional, Any, Protocol


class GraphvizNode:
    name: str
    children: list
    information = Optional[Any]
