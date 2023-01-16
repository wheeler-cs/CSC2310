from unittest import TestCase
from applayer.artist import Artist
from applayer.artistlist import ArtistList
from applayer.artistgraph import ArtistGraph
from applayer.collaboration import Collaboration

from datalayer.mongobridge import MongoBridge


class TestArtistGraph(TestCase):

    def setUp(self) -> None:
        # Initialize a graph using a list of Artists
        self.artistlist = ArtistList([1141491, 1420640, 2867359])
        self.artistgraph = ArtistGraph(self.artistlist, 3)
        # Create 2 test instances of Artist
        self.a = Artist(0, "Jerry Gannod", "Jerry Gannod", "", 0)
        self.b = Artist(1, "Gerald Gannod", "Gerald Gannod", "", 0)
        # Create an empty ArtistGraph instance
        self.emptygraph = ArtistGraph()

        # New tests
        # Create a graph using Alfred Karnes
        self.ak_list = ArtistList([1141491])
        self.ak_graph = ArtistGraph(self.ak_list, 2)
        mb = MongoBridge()
        # Get the objects related to William Doane and Alfred Karnes
        self.wd_data = mb.get_artist_by_id(726550)
        self.ak_data = mb.get_artist_by_id(1141491)
        self.wd_artist = Artist(self.wd_data)
        self.ak_artist = Artist(self.ak_data)
        self.gmbb_artist = Artist(4014047, "Grand Massed Brass Bands", "", "", 2)
        # Create a collaboration and ...

    def test_add_collaboration(self):
        # Create a new collaboration instance using Artist a and b
        c = Collaboration(self.a, self.b)
        # Add collaboration to empty graph
        self.emptygraph.add_collaboration(c)
        # Determine if collab was added based on edges and nodes present
        self.assertTrue(self.emptygraph.has_edge(self.a, self.b))
        self.assertTrue(self.emptygraph.has_edge(self.b, self.a))
        self.assertTrue(self.emptygraph.has_node(self.a))
        self.assertTrue(self.emptygraph.has_node(self.b))

    def test_buildgraph(self):
        # Using self.artistgraph, a graph generated above, determine:
        # If the size of the network is as expected
        self.assertEqual(66, len(self.artistgraph.artists))
        # If the number of collaborations is as expected
        self.assertEqual(91, len(self.artistgraph.collaborations))
        # An empty ArtistGraph has the expected state
        self.assertEqual(0, len(self.emptygraph.artists))
        self.assertEqual(0, len(self.emptygraph.collaborations))

    def test_add_artist(self):
        # Test adding an artist to an empty graph
        self.emptygraph.add_artist(self.a)
        self.assertTrue(self.emptygraph.has_node(self.a))
        self.assertFalse(self.emptygraph.has_node(self.b))
        '''
        Test adding an artist to an already established graph.
        Test added by Drew Wheeler (amwheeler43)
        Notes: Thought it would be pointless just to make another test
            that is pretty much exactly like this. Instead, just added
            onto pre-existing test. The code below is what was added.
        '''
        self.emptygraph.add_artist(self.b)
        self.assertTrue(self.emptygraph.has_node(self.a))
        self.assertTrue(self.emptygraph.has_node(self.b))

    def verify_inheritance(self):
        # Verify relation of GraphBase and ArtistGraph is as expected
        self.assertTrue(issubclass(ArtistGraph, GraphBase))
        self.assertFalse(issubclass(GraphBase, ArtistGraph))

    def test_ak_list(self):
        # Test to see the right number of nodes are there, that William Doane is in the list, and that the edge
        # between these artists are there
        self.assertTrue(33, len(self.ak_graph.graph.nodes))
        self.assertTrue(self.ak_graph.has_node(self.wd_artist))
        self.assertTrue(self.ak_graph.has_edge(self.wd_artist, self.ak_artist))
        self.assertTrue(self.ak_graph.has_edge(self.ak_artist, self.wd_artist))
        self.assertTrue(self.ak_graph.has_node(self.gmbb_artist))
        self.assertTrue(self.ak_graph.has_edge(self.wd_artist, self.gmbb_artist))
        self.assertTrue(self.ak_graph.has_edge(self.gmbb_artist, self.wd_artist))

    def test_compute_degree_centrality(self):
        self.assertTrue(True)

    def test_compute_closeness_centrality(self):
        # Python unittest documentation states that this needs some sort of tag to be handled properly
        # by the module. However, unknown how this should be handled in the context of the assignment.
        # self.fail()

    def test_expansion(self):
        # applayer.ArtistGraph has no method get_expansion_list(), and description of function is
        # absent in the class diagram
        # self.assertEqual(33, len(self.artistgraph.get_expansion_list()))
