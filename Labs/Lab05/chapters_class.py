from typing import List


class Chapters(object):

    def __init__(self, data: List[str]) -> None:
        """
        Given the input data list, instantiate the values of the attributes in the following style
        self.__attributename: type = value

        Sample data: 1, Doorstep Delivery, 1, 1
        :param data: Array of strings
        """
        self.__chapter_id: int = int(data[0])
        self.__chapter_name: str = data[1]
        self.__movie_id: int = int(data[2])
        self.__movie_chapter: int = int(data[3])

    @property
    def chapter_id(self) -> int:
        return self.__chapter_id

    @property
    def chapter_name(self) -> str:
        return self.__chapter_name

    @property
    def movie_id(self) -> int:
        return self.__movie_id

    @property
    def movie_chapter(self) -> int:
        return self.__movie_chapter

    def __str__(self) -> str:
        return self.__chapter_name
