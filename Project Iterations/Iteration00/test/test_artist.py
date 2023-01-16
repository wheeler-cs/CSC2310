from unittest import TestCase
from applayer.artist import Artist


class TestArtist(TestCase):

    def setUp(self) -> None:
        self.artist_0 = Artist(2309551, "Frank Stamps", "", "", 0)
        testdata_1 = {
          "_id": {
            "$oid": "630176cbc210d497ecd5db2e"
          },
          "artistID": 2309551,
          "artistName": "Frank Stamps",
          "realname": None,
          "profile": "Hello, Frank",
          "collaborators": [],
          "level": 0
        }
        self.artist_1 = Artist(testdata_1)
        testdata_2 = {
          "_id": {
            "$oid": "63016fde0f877215590c12a3"
          },
          "artistID": 2968305,
          "artistName": "Mr. & Mrs. Ernest Stoneman",
          "realname": None,
          "profile": "",
          "collaborators": [
            {
              "collaboratorID": 938895,
              "collaboratorName": "Ernest Stoneman",
              "releaseID": 10594844,
              "roles": None
            },
            {
              "collaboratorID": 1448909,
              "collaboratorName": "Hattie Stoneman",
              "releaseID": 10594844,
              "roles": [
                "Fiddle [Uncredited]"
              ]
            }
          ],
          "level": 0
        }
        self.artist_2 = Artist(testdata_2)

    def test_collaborators(self):
        self.assertEqual(2, len(self.artist_2.collaborators))

    def test_realname(self):
        self.assertIsNone(self.artist_1.realName)
        self.assertIsNone(self.artist_2.realName)

    def test_profile(self):
        self.assertEqual("Hello, Frank", self.artist_1.profile)
        self.assertEqual("", self.artist_2.profile)

    def test_ids(self):
        self.assertEqual(2968305, self.artist_2.artistID)
        self.assertNotEqual(0, self.artist_2.artistID)

    def test_artistName(self):
        self.assertEqual("Frank Stamps", self.artist_0.artistName)
        self.assertEqual("Mr. & Mrs. Ernest Stoneman", self.artist_2.artistName)

    def test_str(self):
        self.assertEqual("Frank Stamps (2309551)", self.artist_0.__str__())
        self.assertEqual("Frank Stamps (2309551)", self.artist_1.__str__())

    def test_lt(self):
      self.assertTrue(self.artist_1 < self.artist_2)
      self.assertFalse(self.artist_2 < self.artist_1)
      self.assertFalse(self.artist_1 < self.artist_1)
      self.assertFalse(self.artist_1 < 5)
      self.assertFalse(self.artist_1 < "Bob")


    def test_malformed_dict_init(self):
      # Variables to be used in the unittest
      # Malformed data
      empty = {}
      valKey = {"artistID": 55}
      badKey = {"artistid": 100}
      typKey = {"artistID": "asdfae"}
      # Flags for pass-fail status of tests
      nonCaught = False
      valCaught = False
      badCaught = False
      typCaught = False

      # Exception for empty input
      try:
        Artist(empty)
      except KeyError:
        nonCaught = True
      # Exception for data missing after first key
      try:
        Artist(valKey)
      except KeyError:
        valCaught = True
      # Exception for improper key
      try:
        Artist(badKey)
      except KeyError:
        badCaught = True
      # Exception for invalid data type
      try:
        Artist(typKey)
      except:
        typCaught = True

      # Ensure exceptions were caught as tests
      self.assertTrue(nonCaught)
      self.assertTrue(valCaught)
      self.assertTrue(badCaught)
      self.assertTrue(typCaught)


    def test_malformed_params_init(self):
      badParamCaught = False

      # Attempt to pass in an unhandled data
      try:
        Artist(5, None, "", "", 55)
      except NotImplementedError:
        badParamCaught = True

      self.assertTrue(badParamCaught)


    def test_malformed_setters(self):
      # Flags for pass-fail cases
      handleProper = True
      valCaught = False

      # Ensure good data is handled properly
      try:
        self.artist_0.level = 2
      except ValueError:
        handleProper = False
      # Exception for bad data value being used
      try:  
        self.artist_0.level = "a"
      except ValueError:
        valCaught = True

      # Check if all exception cases were handled properly
      self.assertTrue(handleProper)
      self.assertTrue(valCaught)
