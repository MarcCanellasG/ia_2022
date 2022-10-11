from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None
        self.__solucio=None

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        inicial=Estat[percep.to_dict()]
        OBERT=[inicial]
        TANCAT=[]

        while OBERT:
            actual=OBERT.pop()
            if Estat.es_meta(actual):
                pass
            else:
                successor = actual.genera_fill()
                TANCAT.append(actual)

        pass
