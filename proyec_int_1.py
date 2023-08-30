from typing import List
from typing import Tuple

def convert_map(map_str: str) -> List[List[str]]:
    rows = map_str.split("\n")
    map_matrix = [list(row) for row in rows]
    return map_matrix


def clear_screen():
    print("\033[2J\033[H", end="")

    import readchar
    
    print("ingrese la letra: ")
    key = input(readchar.readkey())
    print(key)
