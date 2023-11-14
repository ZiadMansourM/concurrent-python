from typing import Final
from pathlib import Path

BASE_DIR: Final[Path] = Path(__file__).resolve().parent.parent.parent
DATA_DIR: Final[Path] = BASE_DIR.joinpath("data")
LOGS_DIR: Final[Path] = BASE_DIR.joinpath("logs")


LETTERS: Final[list[tuple[str, int]]] = [
    ("A", 4), 
    ("B", 5), 
    ("C", 3), 
    ("D", 2), 
    ("E", 3)
]

NUMBERS: list[int] = [38, 39, 40, 41]


__DB_NAME: Final[str] = "tune.db"