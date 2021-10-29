class ConstroiFlor:

    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.arquivo_aberto = None

    def __enter__(self):
        self.arquivo_aberto = open(self.arquivo, "r", encoding="utf-8")
        return self

    def pega_atri_txt(self):
        lista_atrr = []
        for linha in self.arquivo_aberto: #txt
            lista_atrr.append(str(linha).replace("\n", "").strip())
        nome = lista_atrr[0]
        cor = lista_atrr[1]
        nro_petalas = lista_atrr[2]
        return nome, cor, nro_petalas

    def __exit__(self, *args):
        return False


"""with ConstroiFlor("frases.txt") as file:
    print(file.pega_atri_txt())
    print("ASSIM ESTÁ O ARQUIVO: ", file)"""
