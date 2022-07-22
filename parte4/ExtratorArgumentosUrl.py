

from cgitb import lookup


class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError('URL inválida!!!')

    @staticmethod
    def urlEhValida(url):
        if url and url.startswith('https://bytebank.com/'):
            return True
        else:
            return False

    def ExtrairArgumentos(self):

        buscaMoedaOrigem = 'moedaorigem'.lower()
        buscaMoedaDestino = 'moedadestino'.lower()

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find('&')

        moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]

        if moedaOrigem == 'moedadestino':
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find('&')
            moedaOrigem = self.url[indiceInicialMoedaOrigem : indiceFinalMoedaOrigem]
        
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find('&valor')
        moedaDestino = self.url[indiceInicialMoedaDestino : indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) + 1

    def trocaMoedaOrigem(self):
        self.url = self.url.replace('moedadestino','real',1)
        print(self.url)

    def extrairValor(self):
        buscarvalor = 'valor'
        indiceInicialValor = self.encontraIndiceInicial(buscarvalor)
        valor = self.url[indiceInicialValor:]
        return valor