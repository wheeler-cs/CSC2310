from typing import List
from multipledispatch import dispatch
import discogs_client
from datalayer.artistnotfound import ArtistNotFound
from discogs_client.exceptions import HTTPError

from time import sleep


class DiscogsBridge(object):
    @dispatch(str, str)
    def __init__(self, key: str, secret: str):
        self.__temp_collaborators: list[dict] = []
        self.__dc: discogs_client.Client = discogs_client.Client(
            'CSC2310_Lecture/1.0',
            consumer_key=key,
            consumer_secret=secret
        )

    @dispatch()
    def __init__(self):
        key = "VofqGvBSvTLjmZaIxVln"
        secret = "lCSpDHQyuoinilgyFNpUqibZeaoBGCgB"
        self.__temp_collaborators: list[dict] = []

        self.__dc: discogs_client.Client = discogs_client.Client(
            'CSC2310_Lecture/1.0',
            consumer_key=key,
            consumer_secret=secret
        )

    def get_artist_by_id(self, aid: int, year: int = 1935) -> dict:
        """
        Get a dictionary of information about an artist from Discogs
        :param aid: artist id
        :param year: optional year
        :return: dictionary with artist info
        :raises: ArtistNotFound if the artist is not found in Discogs
        """
        artistInfo = dict()
        try:
            apiRequest = self.__dc.artist(aid)
            apiArtist  = self.__dc._get(apiRequest.data["resource_url"])
            artistInfo["artistID"] = apiArtist["id"]
            artistInfo["artistName"] = apiArtist["name"]
            if("realname" in apiArtist):
                artistInfo["realname"] = apiArtist["realname"]
            else: # Default to whatever name is given as realname if one doesn't exist
                artistInfo["realname"] = apiArtist["name"]
            artistInfo["profile"] = apiArtist["profile"]
            releaseList = self.__dc._get(apiArtist["releases_url"])
            releaseList = releaseList["releases"]
            artistInfo["collaborators"] = self.get_collaborator_dicts(releaseList, year)
            artistInfo["level"] = 0
        except HTTPError:
            raise ArtistNotFound("Unresolved Artist: ", str(aid))
        return artistInfo

    def get_collaborator_dicts(self, releaseList: list[dict], year: int = 1935) -> list[dict]:
        cList = []
        for release in releaseList:
            # Only add a release's artists if its year is before 'year' param (ignore releases w/ no year)
            if("year" in release) and (release["year"] < year):
                    cList.append(release["artist"])
        cList = list(dict.fromkeys(cList)) # Remove duplicate artists from list
        return cList

    def get_artists_from_list(self, a_list: list[int], year: int = 1935) -> list[dict]:
        """
        Get all the artists from Discogs based on the input list of int ids
        :param a_list: list of integer ids
        :param year: year filter
        """
        result: List[dict] = []
        for i in a_list:
            a = self.get_artist_by_id(i, year)
            if a is not None:
                result.append(a)
        if not result:
            raise ArtistNotFound("No artists found", 404)
        else:
            return result



