from multipledispatch import dispatch
from typing import List
from sys import exit


class Artist(object):

    @dispatch(dict)
    def __init__(self, raw_in: dict):
        """
        Takes a mongodb dictionary from the Artist collection and creates an Artist object
        :param raw_in: dictionary based on schema from mongo database
        """
        # Import basic artist information
        try:
            self.__artistID:   int = int(raw_in["artistID"])
            self.__artistName: str = raw_in["artistName"] if not None else ""
            self.__realName:   str = raw_in["realname"] if not None else ""
            self.__profile:    str = raw_in["profile"] if not None else ""
            self.__level:      int = int(raw_in["level"])
            self.__collaborators: List[dict] = raw_in["collaborators"]
        except KeyError: # A dictionary with a bad key was used
            print("[Invalid dict key]")
            raise KeyError("Unexpected key in dict.")
        except ValueError: # Bad values are found in the dictionary
            print("[Invalid dict data value]")
            raise ValueError("Unexpcted data value in dict.")
        except TypeError: # Invalid data types for operations are used
            print("[Invalid dict data type]")
            raise TypeError("Unexpected data type in dict.")
        except BaseException as unhandled: # Unhandled exception raise, terminate execution
            print("[Unhandled exception raised in the Artist dict initializer: {exception}]".format(exception=unhandled))
            exit(5)



    @dispatch(int, str, str, str, int)
    def __init__(self, aid: int, name: str, real_name: str, profile: str, level: int):
        """
        Creates an Artist object using the input parameters; collaborators is set to None
        :param aid: artist id
        :param name: artist name
        :param real_name: artist real name, if known
        :param profile: artist profile
        :param level: artist level
        """
        # Store data passed in as method parameters
        try:
            self.__artistID:   int = int(aid)
            self.__artistName: str = name if not None else ""
            self.__realName:   str = real_name if not None else ""
            self.__profile:    str = profile if not None else ""
            self.__level:      int = int(level)
            self.__collaborators: List[dict] = []
        except ValueError: # Bad values detected as input
            print("[Invalid parameter value]")
            raise ValueError("Unexpcted data value as parameter.")
        except TypeError: # Invalid data types for operations are used
            print("[Invalid parameter type]")
            raise TypeError("Unexpected data type as parameter.")
        except BaseException as unhandled: # Unhandled exception raised, terminate execution
            print("[Unhandled exception raised in Artist parameter initializer: {exception}]".format(exception=unhandled))
            exit(5)


    def __lt__(self, other) -> bool:
        '''
        Compares the __artistName of two Artist classes and returns True if the left-hand Artist is
        lexographically smaller than the right-hand artist.

        This defines the sorting criteria for the Artist class as the name of the artist.

        Parameters:
            other (Artist): The right-hand operand of the comparison operator.

        Returns:
            bool:
                 True: If the left-hand operand of the < operator is less than the right-hand operand.
                False: If the right-hand operand of the < operator is less than the left-hand operand.
        '''
        try:
            if self.__artistName < other.__artistName:
                return True
            else:
                return False
        except AttributeError: # Attempt to rectify other not being of type Artist
            if type(other) is str: # other is of type str, try to salvage by using it as the right-hand name
                if self.__artistName < other:
                    return True
                else:
                    return False
            else: # Couldn't resolve type of other parameter in the context of Artist class
                print("[Invalid right-hand data type for Artist lt operator: Type is {typ} when Artist or str is expected]".format(typ=type(other)))
                return False
        except BaseException as unhandled: # Unhandled exception encountered, just assume left-hand operand is larger
            print("[Unhandled comparison exception raised for Artist lt operator: {exception}]".format(exception=unhandled))
            return False

    @property
    def artistID(self) -> int:
        return self.__artistID

    @property
    def artistName(self) -> str:
        return self.__artistName

    @property
    def realName(self) -> str:
        return self.__realName

    @property
    def profile(self) -> str:
        return self.__profile

    @property
    def level(self) -> int:
        return self.__level

    @property
    def collaborators(self) -> List[dict]:
        return self.__collaborators

    @level.setter
    def level(self, lev: int) -> None:
        try:
            self.__level = int(lev)
        except ValueError: # Parameter passed in wasn't an int
            print("[Invalid value for level]")
            raise ValueError
        except BaseException as unhandled: # Unhandled error encountered; print message and do nothing
            print("[Unhandled exception raised in Artist.level mutator: {exception}]".format(exception=unhandled))
            print("No action has been taken...")

    def __str__(self) -> str:
        """
        Prints an artist name and artist ID
        ex. Alcoa Quartet (1141480)
        :return: string formatted as in example
        """
        return "{name} ({id})".format(name = self.__artistName, id = self.__artistID)
