from typing import List


class Places(object):

    def __init__(self, data: List[str]) -> None:
        """
        Given the input data list, instantiate the values of the attributes in the following style
        self.__attributename: type = value

        Sample data: 1, Flourish & Blotts, Diagon Alley
        :param data: Array of strings
        """
        self.__place_id: int = int(data[0])
        self.__place_name: str = data[1]
        self.__place_category: str = data[2]

    @property
    def place_id(self) -> int:
        return self.__place_id

    @property
    def place_name(self) -> str:
        return self.__place_name

    @property
    def place_category(self) -> str:
        return self.__place_category

    def __str__(self) -> str:
        return self.__place_name
