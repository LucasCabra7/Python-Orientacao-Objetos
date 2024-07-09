from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #A classe prato está herdando metodos e atributos da classe ItemCardapio.
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) # O 'super' serve para acessarmos informações de outras Classes no caso ItemCardapio.
        self.descricao = descricao
        
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)