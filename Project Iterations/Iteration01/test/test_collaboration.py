from unittest import TestCase
from applayer.artist import Artist
from applayer.artistlist import ArtistList
from applayer.artistgraph import ArtistGraph
from applayer.collaboration import Collaboration

from datalayer.mongobridge import MongoBridge

class TestCollaboration(TestCase):
    def setUp(self) -> None:
        self.artist_0 = Artist(123456, "Mr. Mustard the Fiddler", "", "", 0)
        self.artist_1 = Artist(654321, "Senor Salisbury", "Juan Carlos III", "", 1)
        self.artist_2 = Artist(1001, "Johnny Nine Fingers", "Johnathan Zaxby", "", 1)
        self.role_list_0 = ["Fiddler", "Banjo"]
        self.role_list_1 = ["Electric Bass", "Banjo"]
        self.t_colab_0 = Collaboration(self.artist_0, self.artist_1, self.role_list_0)
        self.t_colab_1 = Collaboration(self.artist_0, self.artist_2, self.role_list_1)
        self.t_colab_2 = Collaboration(self.artist_1, self.artist_2, [])
        # Things for new tests added
        mb = MongoBridge()
        self.a0 = Artist(mb.get_artist_by_id(1141491))
        self.a1 = Artist(mb.get_artist_by_id(938895))
        self.roles = ["Guitar", "Banjo"]
        self.collab = Collaboration(self.a0, self.a1, self.roles)

        self.a2 = Artist(mb.get_artist_by_id(2411933))
        self.a3 = Artist(mb.get_artist_by_id(2304638))
        self.collab2 = Collaboration(self.a2, self.a3)

    def test_artist_get(self):
        # Verify artists are properly initialized
        self.assertEqual   (self.t_colab_0.artist0, self.artist_0)
        self.assertEqual   (self.t_colab_0.artist1, self.artist_1)
        self.assertNotEqual(self.t_colab_0.artist0, self.artist_2)

    def test_role_get(self):
        # Verify role list is properly initialized
        self.assertEqual(["Fiddler", "Banjo"], self.t_colab_0.roles)
        self.assertEqual(["Electric Bass","Banjo"], self.t_colab_1.roles)
        self.assertEqual([], self.t_colab_2.roles)

    def test_list_len(self):
        # Ensure the length of the role list is as expected
        self.assertEqual(2, len(self.t_colab_0.roles))
        self.assertEqual(0, len(self.t_colab_2.roles))

    def test_artist0(self):
        self.assertEqual(self.a0, self.collab.artist0)

    def test_not_artist0(self):
        self.assertNotEqual(self.a1, self.collab.artist0)

    def test_artist1(self):
        self.assertEqual(self.a1, self.collab.artist1)

    def test_not_artist1(self):
        self.assertNotEqual(self.a0, self.collab.artist1)

    def test_roles(self):
        self.assertEqual(self.roles, self.collab.roles)
        self.assertIn("Guitar", self.collab.roles)
        self.assertIn("Banjo", self.collab.roles)
        self.assertNotIn("Fiddle", self.collab.roles)

    def test_none_roles(self):
        self.assertIsNone(self.collab2.roles)
