from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None
        self.__solucio = []

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        inicial = Estat(percep.to_dict())
        self.__oberts = []
        self.__tancats = []

        self.__oberts.append(inicial)

        while self.__oberts:
            actual = self.__oberts.pop(0)
            print(actual)
            if Estat.es_meta(actual):
                for actual.pare in self.__oberts:
                    if actual.pare not in self.__tancats:
                        self.solucio.append(actual.pare)
                        actual=actual.pare

                return tuple(reversed(self.__solucio))

            else:
                successors = actual.genera_fill()
                self.__tancats.append(actual)
                self.__oberts.append(successors)

        pass
