from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebida
from modelos.cardapio.prato import Prato

restaurante_galletus = Restaurante('Galletus', 'Assados')
bebida_galletus = Bebida('Coca - cola', 7, '2L')
bebida_galletus.aplicar_desconto()
prato_galletus = Prato('Filé com fritas', 39, 'Porção de bife assado, cebola cristalizada e batata frita')
prato_galletus.aplicar_desconto()

restaurante_galletus.adicionar_no_cardapio(bebida_galletus)
restaurante_galletus.adicionar_no_cardapio(prato_galletus)

def main():
    restaurante_galletus.exibir_cardapio

if __name__ == '__main__':
    main()