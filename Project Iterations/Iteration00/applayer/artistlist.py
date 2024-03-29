from typing import List, Tuple
from applayer.artist import Artist
from datalayer.mongobridge import MongoBridge
from multipledispatch import dispatch
from pymongo import errors
from sys import exit


class ArtistList(object):
    """
    The ArtistList class consists of two attributes:
        * __artist_objects: List[Artist] (must be Artist objects)
        * __artists: List[Tuple[int, str]] (ex. [(1141480, Alcoa Quartet), (1141491, Alfred G. Karnes)]
          this list must be sorted
    """
    @dispatch(list)
    def __init__(self, ids: List[int]):
        """
        The constructor uses data in mongo to create attributes based on the input ids list;
        Use a Mongobridge object to pull data from the Mongo database; the artists attribute
        must be a sorted list.
        """
        try:
            # Init and get data from Mongo database
            db = MongoBridge()
            self.__artist_objects: List[Artist] = []
            for x in db.get_artists_from_list(ids):
                self.__artist_objects.append(Artist(x))

            # Get ID and name from Artists as a list of tuples
            self.__artists: List[Tuple[int, str]] = []
            for x in self.__artist_objects:
                nameAndId = (x.artistID, x.artistName)
                self.__artists.append(nameAndId)
            self.__artists.sort(key = lambda x: x[1])
        except errors.ConnectionFailure: # Unable to connect to default MongoDB for some reason
            print("[Unable to connect to MongoDB for querying]")
            raise errors.ConnectionFailure("Cannot connect to MongoDB.")
        except BaseException as unhandled: # Something happened that wasn't anticipated
            print("[Unhandled exception raised in ArtistList initializer: {exception}]".format(exception=unhandled))
            exit(5)


    @dispatch()
    def __init__(self):
        """
        Read all of the data from mongo and attributes for all artists; See comment at head of the
        class; the artists attribute must be a sorted list.
        Use a Mongobridge object to pull data from the Mongo database
        """
        try:
            # Init and get data from Mongo database
            db = MongoBridge()
            self.__artist_objects: List[Artist] = []
            for x in db.get_all_artists():
                self.__artist_objects.append(Artist(x))

            # Get ID and name from Artists as a list of tuples
            self.__artists: List[Tuple[int, str]] = []
            temp = sorted(self.__artist_objects)
            for x in self.__artist_objects:
                nameAndId = (x.artistID, x.artistName)
                self.__artists.append(nameAndId)
            self.__artists.sort(key = lambda x: x[1])
        except errors.ConnectionFailure: # Unable to connect to default MongoDB for some reason
            print("[Unable to connect to MongoDB for querying]")
            raise errors.ConnectionFailure("Cannot connect to MongoDB.")
        except BaseException as unhandled: # Something happened that wasn't anticipated
            print("[Unhandled exception raised in ArtistList initializer: {exception}]".format(exception=unhandled))
            exit(5)

    @property
    def artists(self) -> List[Tuple[int, str]]:
        """
        Returns the list of artists as list of tuples of (artistid: int, name: str)
        :return: list of artists
        """
        return self.__artists

    @property
    def artist_objects(self) -> List[Artist]:
        """
        Returns the list of Artist objects
        :return:
        """
        return self.__artist_objects

    def __str__(self) -> str:
        """
        Prints a list of Artist objects separated by a comma ','
        ex: Alcoa Quartet (1141480), Alfred G. Karnes (1141491)
        Note that the formatting of the print of the Artist object is determined by
        the Artist class
        :return: str
        """
        retStr = ""
        for x in self.__artist_objects:
            retStr += x.__str__() + ", "    # Get the printout of the Artist and add a comma
        if len(retStr) > 2:
            return retStr[:-2] # Truncate the final ", " added onto the string
        else: # String isn't long enough to truncate the final ", ", just return an empty string
            return ""
