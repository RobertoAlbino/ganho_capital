from decimal import ROUND_HALF_UP, Decimal


class ValorMonetario:
    
    def __init__(self, valor_monetario):
        self.valor_monetario = Decimal(valor_monetario).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)