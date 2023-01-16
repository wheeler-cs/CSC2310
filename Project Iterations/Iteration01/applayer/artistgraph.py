from typing import List
from multipledispatch import dispatch

from applayer.graphbase import GraphBase
from applayer.artist import Artist
from applayer.artistlist import ArtistList
from applayer.collaboration import Collaboration
from datalayer.mongobridge import MongoBridge

from datalayer.artistnotfound import ArtistNotFound


class ArtistGraph(GraphBase):


    @dispatch()
    def __init__(self) -> None:
        '''
        Default initializer. Shouldn't ever really be called, but helps with
        redundancy and preventing errors.
        '''
        super().__init__()
        self.__artists: List[Artist] = []
        self.__collaborations: List[Collaboration] = []


    @dispatch(ArtistList, int)    
    def __init__(self, artist_list: ArtistList, depth:int) -> None:
        '''
        Initializer that should be called when creating a new instance of the
        ArtistGraph class.
        :param artist_list: An ArtistList object instance.
        :param depth: How many nodes are in a sequence. 
        '''
        # Set up member variables for class instance
        super().__init__()
        self.__artists: List[Artist] = []
        self.__collaborations: List[Collaboration] = []
        # Create a temporary connection to the local MongoDB instance
        mDB = MongoBridge()
        masterArtistList = []   # List stores all artists found, ignoring duplicates
        masterCollabList = []   # List stores collaborations, ignoring duplicates
        artistQueue = []
        for a in artist_list.artist_objects:
            artistQueue.append(a)
        lvl = 1
        idx = 0
        while((idx < len(artistQueue)) and (lvl <= depth)): # BUG: Network is not generated properly; some issue needs to be sussed out...
            if(artistQueue[idx].level == lvl):
                lvl += 1
            if(artistQueue[idx].collaborators is not None):
                for c in artistQueue[idx].collaborators:
                    newArtist = None
                    newCollab = None
                    try:
                        # Iterate through all collaborators an Artist has, try to find them in the database, and if
                        # they cannot be found, make a new artist
                        rawArtistInfo = mDB.get_artist_by_id(c["collaboratorID"])
                        rawArtistInfo["level"] = lvl
                        newArtist = Artist(rawArtistInfo)
                    except ArtistNotFound:
                        # Make new artist because the one specified wasn't found
                        newArtist = Artist(c["collaboratorID"], c["collaboratorName"], "", "", lvl)
                    finally:
                        if(c["roles"] is None):
                            newCollab = Collaboration(artistQueue[idx], newArtist, [])
                        else:
                            newCollab = Collaboration(artistQueue[idx], newArtist, c["roles"])
                        masterArtistList.append(newArtist)
                        masterCollabList.append(newCollab)
                        artistQueue.append(newArtist)
            idx += 1
        # Store artists found in the class lists
        for a in masterArtistList:
            self.add_artist(a)
        # Store collaborations found
        for c in masterCollabList:
            self.add_collaboration(c)


    def add_collaboration(self, collab: Collaboration) -> None:
        '''
        Adds a Collaboration instance to the graph as both a member of an internal
        list and as an edge for the graph itself. If an edge already exists, it
        instead has its value incremented by 1.
        :param collab: A Collaboration instance to be added to graph.
        '''
        if super().has_edge(collab.artist0, collab.artist1):  # Collaboration already recorded, increment edge counter
            super().incr_edge(collab.artist0, collab.artist1)
        else: # Collaboration has not been recorded, add to list
            super().add_edge(collab.artist0, collab.artist1)
            self.__collaborations.append(collab)


    def add_artist(self, artist: Artist) -> None:
        '''
        Adds an Artist instance to the graph as both a member of an internal list
        and as a node from the graph itself.
        '''
        inList = (artist in self.artists)
        if inList == False:
            super().add_node(artist)
            self.__artists.append(artist)


    @property
    def artists(self) -> List[Artist]:
        return self.__artists

    @property
    def collaborations(self) -> List[Collaboration]:
        return self.__collaborations


if __name__ == "__main__":
    a_list = ArtistList([5497871])
    #a_list = ArtistList([1141491, 1420640, 2867359])
    a_graph = ArtistGraph(a_list, 3)
    print("Graph Length: {l}".format(l=a_graph.artists))