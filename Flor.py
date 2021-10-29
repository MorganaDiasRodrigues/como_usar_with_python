from ConstroiFlor import ConstroiFlor
"""Classe para exemplificar o uso de with."""
class Flor:
    def __init__(self, arquivo):
        with ConstroiFlor(arquivo) as file:
            self.nome, self.cor, self.nro_petalas = file.pega_atri_txt()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True

    def __str__(self):
        return "DESCRIÇÃOn\n" + "FLOR: " + self.nome + " COR: " + self.cor + " TOTAL DE PETALAS: " + self.nro_petalas
