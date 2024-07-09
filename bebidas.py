from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco) # Obs: ele está utilizando os atributos da class ItemCardapio - se chama 'Herança'.
        self.tamanho = tamanho

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)