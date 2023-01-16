from unittest import TestCase

import datalayer.artistnotfound
from applayer.artistlist import ArtistList


class TestArtistList(TestCase):

    def setUp(self):
        # Create a list of ids to be pulled from MongoDB
        ids = [938895, 2634203, 1141486, 908705, 2411933, 2304638, 3895080, 1448909, 1448911, 1141474, 2916175, 353265, 1141476, 938862, 1141491, 1141484, 1141487, 307357, 1141480, 516930, 1001138, 1141475, 269365, 1141488, 1141483, 1141489, 2867358, 2867360, 2189637, 908699, 1420640, 2867359, 1826135]
        # Initialize an instance of ArtistList using the above ids
        self.artists = ArtistList(ids)
        # Initialize an instance of ArtistList containing all artists in a database
        self.allartists = ArtistList()
        # Create an empty list
        empty_ids = []
        self.empty_list = ArtistList(empty_ids)

    def test_bristol_artists(self):
        # There should be 33 artists in the list
        self.assertEqual(33, len(self.artists.artists))
        # Returned list must be sorted
        self.assertTrue(TestArtistList.isSorted(self.artists.artists, key=lambda x: x[1]))
        # Assuming the list is sorted, the following will be true
        self.assertEqual("B.F. Shelton", self.artists.artists[2][1])
        self.assertEqual("Jimmie Rodgers", self.artists.artists[16][1])
        self.assertEqual((269365, "Jimmie Rodgers"), self.artists.artists[16])
        self.assertEqual((938862, "B.F. Shelton"), self.artists.artists[2])

    def test_bristol_artists_no_db(self):
        # Verify ArtistNotFound is raised for bad URI
        with self.assertRaises(datalayer.artistnotfound.ArtistNotFound):
            self.noartists = ArtistList("mongodb://localhost:27017", "BristolData", "NoArtists")
            #self.assertEqual(33, len(self.artists.noartists))
            # Above line causes a syntax error; believe it should be self.noartists.artists (see below)
            self.assertEqual(0, len(self.noartists.artists))
            # I'm a bit confused on this one, shouldn't the size be 0 instead of 33 because the
            # collection has no artists in it?

    def test_artists(self):
        # There should be 179 artists in the list
        self.assertEqual(179, len(self.allartists.artists))
        # Returned list must be sorted
        self.assertTrue(TestArtistList.isSorted(self.allartists.artists, key=lambda x: x[1]))
        # Assuming the list is sorted, the following will be true
        self.assertEqual("A. P. Carter", self.allartists.artists[0][1])
        self.assertEqual("Alice Palmer", self.allartists.artists[3][1])

    def test_artists_objects(self):
        # Obtain a List[Artist]
        objs = self.artists.artist_objects
        # Verify data in specific index is as expected
        self.assertEqual(1141486, objs[2].artistID)
        self.assertEqual("Irma Frost", objs[2].artistName)
        self.assertEqual(1, len(objs[2].collaborators))

    def test_allartists_artists(self):
        # Verify that loading all artists upon instantiation is done correctly
        self.assertEqual("Sam J. McCollum", self.allartists.artists[139][1])
        self.assertEqual("Jimmie Rodgers", self.allartists.artists[99][1])

    def test_allartists_objects(self):
        # Test for sequential Artists
        a0 = next(item for item in self.allartists.artist_objects if item.artistID == 1826136)
        self.assertEqual("Stephen Tarter", a0.artistName)
        a0 = next(item for item in self.allartists.artist_objects if item.artistID == 5766040)
        self.assertEqual("Jim Seany", a0.artistName)


    def test_print(self):
        # Get an ArtistList using a list of 3 ids
        ids = [938895, 2634203, 1141486]
        artists = ArtistList(ids)
        # Set the expected output of the function
        outstring = "Ernest Stoneman (938895), Kahle Brewer (2634203), Irma Frost (1141486)"
        # Verify __str__() method of ArtistList is correct
        self.assertEqual(outstring, artists.__str__())
        # Verify ArtistList sorts correctly
        self.assertTrue(TestArtistList.isSorted(self.artists.artists, key=lambda x: x[1]))
        # Verify artists are positioned where expected
        self.assertEqual("Ernest Stoneman", artists.artists[0][1])
        self.assertEqual("Kahle Brewer", artists.artist_objects[1].artistName)

    @staticmethod
    def isSorted(x, key=lambda x: x):
        return all([key(x[i]) <= key(x[i + 1]) for i in range(len(x) - 1)])

    def test_exception_handle(self):
        # Tests should crash here is exception wasn't properly handled
        test_passed = False
        ArtistList("BadDB", "BadItem", "BadItem")
        test_passed = True
        self.assertTrue(test_passed)

    def test_empty_list(self):
        # Test that artists and artist_objects lists are initialized to empty
        self.assertEqual([], self.empty_list.artists)
        self.assertEqual([], self.empty_list.artist_objects)

    def test_print_empty(self):
        # Test to make sure no extra characters are printed for an empty list
        self.assertEqual("", self.empty_list.__str__())
        self.assertNotEqual(", ", self.empty_list.__str__())
