from typing import List


class Movies(object):

    def __init__(self, data: List[str]) -> None:
        """
        Given the input data list, instantiate the values of the attributes in the following style
        self.__attributename: type = value

        Sample data: 1, Harry Potter and the Philosopher's Stone, 2001, 152, "$125,000,000", "$1,002,000,000"
        :param data: Array of strings
        """
        self.__movie_id: int = int(data[0])
        self.__movie_title: str = data[1]
        self.__release_year: int = int(data[2])
        self.__runtime: int = int(data[3])
        self.__budget: str = data[4]
        self.__box_office: str = data[5]

    @property
    def movie_id(self) -> int:
        return self.__movie_id

    @property
    def movie_title(self) -> str:
        return self.__movie_title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def runtime(self) -> int:
        return self.__runtime

    @property
    def budget(self) -> str:
        return self.__budget

    @property
    def box_office(self) -> str:
        return self.__box_office

    def __str__(self) -> str:
        return self.__movie_title
