from typing import List


class WizardingCharacter(object):

    def __init__(self, data: List[str]) -> None:
        self.__character_id: int = int(data[0])
        self.__character_name: str = data[1]
        self.__species: str = data[2]
        self.__gender: str = data[3]
        self.__house: str = data[4]
        self.__patronus: str = data[5]
        self.__wood: str = data[6]
        self.__core: str = data[7]

    @property
    def character_name(self):
        return self.__character_name

    @property
    def character_id(self):
        return self.__character_id

    @property
    def species(self):
        return self.__species

    @property
    def gender(self):
        return self.__gender

    @property
    def patronus(self):
        return self.__patronus

    @property
    def house(self):
        return self.__house

    @property
    def wood(self):
        return self.__wood

    @property
    def core(self):
        return self.__core

    def __str__(self):
        return "{}, House: {}".format(self.__character_name, self.__house)
