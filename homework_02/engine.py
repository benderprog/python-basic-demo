"""
create dataclass `Engine`
"""

from dataclasses import dataclass


@dataclass
class Engine():
    """
    добавьте атрибуты volume и pistons
    """
    volume: float
    pistons: int

