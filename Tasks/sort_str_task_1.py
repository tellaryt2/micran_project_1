import re

def sort_str() -> None:
    n = ["C_12_F", "C_01_F", "C_75_F", "C_98_F", "C_02_F", "C_31_F", "C_53_F", "C_22_F", "C_11_F", "C_44_F"]

    n = sorted(n, key=lambda element: re.findall(r'\d+', element))

    print(n)