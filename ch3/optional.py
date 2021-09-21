from typing import Optional

class Bun:
    def __init__(self, name: str):
        self.name = name

def are_buns_available():
    return True

# Optionalを使ってstrとNoneの双方を使える変数を定義
string_or_none1: Optional[str] = "string"
string_or_none2: Optional[str] = None

def dispense_bun() -> Optional[Bun]:
    if not are_buns_available():
        return None
    return Bun('Wheat')