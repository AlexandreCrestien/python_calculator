def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("impossible de diviser par zéro")
    return a / b