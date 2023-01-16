import pymongo
from typing import List, Any
from multipledispatch import dispatch
from sys import exit


class MongoBridge(object):
    """
    MongoBridge reads raw data from the mongo database for the BristolData database.
    """
    @dispatch(str, str, str)
    def __init__(self, uri: str, db: str, col: str):
        """
        Connects to the uri server, db database, and the col collection

        Parameters:
            uri (str): Address where running instance of Mongo can be found.
             db (str): Database within the Mongo server that houses data needed.
            col (str): Collection within the specified database that has needed data.
        """
        try:
            self.__server:     pymongo.MongoClient = pymongo.MongoClient(uri, timeoutMS="5000")
            self.__server.admin.command("ping") # Needed to trigger a connection failure exception
            self.__database:   pymongo.Database    = self.__server[db]
            self.__collection: pymongo.Collection  = self.__database[col]
        except pymongo.errors.ConnectionFailure: # Catch bad server connection
            print("[Unable to connect to MongoDB {dbUri}]".format(dbUri=uri))
            raise pymongo.errors.ConnectionFailure
        # Couldn't get the InvalidName exception to trigger, even when using clearly wrong input; it's here just in case
        except pymongo.errors.InvalidName: # Catch bad database name being used
            print("[Unable to find database {dbName}]".format(dbName=db))
            raise pymongo.errors.InvalidName
        except BaseException as unhandled: # Catchall for unhandled exceptions; terminates execution
            print("[Unhandled exception raised in parameter initializer of MongoBridge: {exception}]".format(exception=unhandled))
            exit(5)


    @dispatch()
    def __init__(self):
        """
        Connects to the mongo server, BristolData database, and the Artists collection
        """
        try:
            self.__server:     MongoClient = pymongo.MongoClient("mongodb://localhost:27017/", timeoutMS="5000")
            self.__server.admin.command("ping") # Needed to trigger a connection failure exception
            self.__database:   Database    = self.__server["BristolData"]
            self.__collection: Collection  = self.__database["Artists"]
        except pymongo.errors.ConnectionFailure: # Unable to connect to server specified
            print("[Unable to connect to default MongoDB]")
            raise pymongo.errors.ConnectionFailure
        except BaseException as unhandled: # Catchall for unhandled exceptions; terminates execution
            print("[Unhandled exception raised in default MongoBridge initializer: {exception}]".format(exception=unhandled))
            exit(5)


    def get_all_artists(self) -> List[dict]:
        """
        Get all artists in the database/collection. The returned list is a dictionary
        formatted with the following fields:
        * _id: str
        * artistID: int
        * artistName: str
        * realname: str
        * profile: str
        * collaborators: List of dictionaries
        * level: int
        See the test_artist.py for an example
        :return: list of the dictionaries returned from mongo
        """
        retList = []
        for x in self.__collection.find():
            retList.append(x)
        return retList


    def get_artists_from_list(self, a_list: list[int]) -> List[dict]:
        """
        Get artists using the id list from the database/collection
        The returned list is a dictionary formatted with the following fields:
        * _id: str
        * artistID: int
        * artistName: str
        * realname: str
        * profile: str
        * collaborators: List of dictionaries
        * level: int
        See the test_artist.py for an example
        :return: list of the dictionaries returned from mongo
        """
        retList = []
        for x in a_list:
            temp_a = self.__collection.find_one({"artistID": x})
            retList.append(temp_a)
        return retList

    def get_artist_by_id(self, aid: int) -> dict:
        """
        Get the dictionary for a single artist from the database/collection.
        The returned dictionary is formatted with the following fields:
        * _id: str
        * artistID: int
        * artistName: str
        * realname: str
        * profile: str
        * collaborators: List of dictionaries
        * level: int
        See the test_artist.py for an example
        :param aid: artist id
        :return: dictionary with artist info
        """
        return self.__collection.find_one({"artistID": aid})

    
    def get_artist_by_name(self, aName: str) -> dict:
        '''
        Get the dictionary for a single artist from the database/collection.
        The returned dictionary is formatted with the following fields:
        * _id: str
        * artistID: int
        * artistName: str
        * realname: str
        * profile: str
        * collaborators: List of dictionaries
        * level: int
        See the test_artist.py for an example
        :param aName: artist name
        :return: dictionary with artist info
        '''
        return self.__collection.find_one({"artistName": aName})
