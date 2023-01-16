from typing import List
from multipledispatch import dispatch

from applayer.artist import Artist


class Collaboration(object):

    @dispatch()
    def __init__(self) -> None:
        '''
        Default fall-back initializer. In the event that parameters are not provided for some reason,
        the class will still get instantiated with two empty Artist() and an empty list.
        '''
        self.__artist0: str = Artist()
        self.__artist1: str = Artist()
        self.__roles: List[str] = []

    #@dispatch(Artist, Artist)
    # The above dispatch causes issues, requiring the 3rd parameter not be present
    def __init__(self, a0: Artist, a1: Artist, rList: List[str] = None) -> None:
        '''
        Primary initializer that is expected to be used by program. Member variables are initialized
        to some given data.
        :param a0: An Artist() instance to be stored in the __artist0 member variable.
        :param a1: An Artist() instance to be stored in the __artist1 member variable.
        :param rList: A list of strings containing roles taken on by an artist during a collaboration.
        '''
        self.__artist0: str = a0
        self.__artist1: str = a1
        self.__roles: List[str] = rList


    @property
    def artist0(self) -> Artist:
        return self.__artist0

    @property
    def artist1(self) -> Artist:
        return self.__artist1

    @property
    def roles(self) -> List[str]:
        return self.__roles


    def __eq__(self, comp) -> bool:
        '''
        Compares two collaborations and determines if they are equivalent. Since the graph is
        an undirected graph, the order of the two artists are arbitrary. Therefore, there can
        be two possible cases for essentially the same connection.
        '''
        if((self.artist0 == comp.artist0) and (self.artist1 == comp.artist1)): # Same artist order
            return True
        elif((self.artist0 == comp.artist1) and (self.artist1 == comp.artist0)): # Swapped artist order
            return True
        else: # No match
            return False
    