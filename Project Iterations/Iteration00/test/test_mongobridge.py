from unittest import TestCase
from datalayer.mongobridge import MongoBridge
from pymongo import errors


class TestMongoBridge(TestCase):

    def setUp(self) -> None:
        self.mongo_bridge = MongoBridge("mongodb://localhost:27017/", "BristolData", "Artists")

    def test_get_all_artists(self):
        artists = self.mongo_bridge.get_all_artists()
        self.assertEqual(179, len(artists))
        self.assertEqual(1826136, artists[60]["artistID"])
        self.assertEqual(628155, artists[178]["artistID"])

    def test_get_artists_from_list(self):
        ids = [938895, 2634203, 1141486, 908705, 2411933, 2304638, 3895080, 1448909, 1448911, 1141474, 2916175, 353265, 1141476, 938862, 1141491, 1141484, 1141487, 307357, 1141480, 516930, 1001138, 1141475, 269365, 1141488, 1141483, 1141489, 2867358, 2867360, 2189637, 908699, 1420640, 2867359, 1826135]
        artists = self.mongo_bridge.get_artists_from_list(ids)
        self.assertEqual(33, len(artists))
        # tests whether the artistID at artists[2] is 1141486
        self.assertEqual(1141486, artists[2]["artistID"])

    def test_get_artist_by_id(self):
        # Artist exists
        artist = self.mongo_bridge.get_artist_by_id(269365)
        self.assertEqual(269365, artist["artistID"])
        self.assertEqual("Jimmie Rodgers", artist["artistName"])
        self.assertEqual(0, artist["level"])
        self.assertEqual("James Charles Rodgers", artist["realname"])

        # Artist does not exist
        artist2 = self.mongo_bridge.get_artist_by_id(0)
        self.assertIsNone(artist2)

    def test_get_collaborator_by_id(self):
        # Find an artist by using a collaborator of another artist as input
        inputArtist = self.mongo_bridge.get_artist_by_id(269365)

        # Generate a list of collaborators and pull the first index from that list
        collabs = inputArtist["collaborators"]
        collabID = collabs[0]["collaboratorID"]
        # The above code could technically be just one line, but honestly at that point it's asinine
        # and hard to read. Instead, I opted for two variables to increase readability at the cost
        # of an additional variable.

        # Use ID of pulled artist from list as input for new Artist instance.
        collabArtist = self.mongo_bridge.get_artist_by_id(collabID)
        self.assertEqual("Kelly Harrell", collabArtist["artistName"])

    def test_get_artist_by_name(self):
        # Query the database to find an artist with a given name
        artist = self.mongo_bridge.get_artist_by_name("Ernest Stoneman")

        # Test the artist's data against what it is expected to be
        self.assertEqual(artist["artistName"], "Ernest Stoneman")
        self.assertEqual(artist["level"], 0)
        self.assertEqual(artist["artistID"], 938895)

    
    def test_bad_database_connection(self):
        badConCaught = False

        try:
            MongoBridge("badUri", "BristolData", "Artists")
        except errors.ConnectionFailure:
            badConCaught = True

        self.assertTrue(badConCaught)
