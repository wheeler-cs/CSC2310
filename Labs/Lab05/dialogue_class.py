from typing import List
from character_class import WizardingCharacter


class Dialogue(object):

    def __init__(self, data: List[str]) -> None:
        """
        Given the input data list, instantiate the values of the attributes in the following style
        self.__attributename: type = value

        Sample data: 97,4,10,5,"You're a wizard, Harry."
        :param data: Array of strings
        """
        self.__dialogueId: int = int(data[0])
        self.__chapter: int = int(data[1])
        self.__place: int = int(data[2])
        self.__character: int = int(data[3])
        self.__text: str = data[4]

    @property
    def id(self) -> int:
        return self.__dialogueId

    @property
    def chapter(self) -> int:
        return self.__chapter

    @property
    def place(self) -> int:
        return self.__place

    @property
    def character(self) -> int:
        return self.__character

    @property
    def dialogue(self) -> str:
        return self.__text

    def spoken_by(self, character: WizardingCharacter) -> bool:
        """
        Used to verify whether a given character spoke the line
        :param character:
        :return: True if character spoke the line
        """
        if character.character_id == self.__character:
            return True
        else:
            return False

    def __str__(self):
        return self.__text
