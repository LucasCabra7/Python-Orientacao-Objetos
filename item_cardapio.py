from abc import ABC, abstractmethod #Metodo abstrato

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod #todas as classes derivadas de ItemCardapio precisam ter (Polimorfismo)
    def aplicar_desconto(self):
        pass
