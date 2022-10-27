from unittest import TestCase
from movies_class import Movies


class MyTestCase(TestCase):

    def setUp(self):
        success_data = [4, "Harry Potter and the Goblet of Fire", 2005, 157, "$150,000,000", "$896,400,000"]
        self.m0 = Movies(success_data)

    def test_id(self):
        self.assertEqual(4, self.m0.movie_id)
        self.assertNotEqual(1, self.m0.movie_id)

    def test_title(self):
        self.assertEqual("Harry Potter and the Goblet of Fire", self.m0.movie_title)
        self.assertNotEqual("HARRY POTTER AND THE GOBLET OF FIRE", self.m0.movie_title)

    def test_release_year(self):
        self.assertEqual(2005, self.m0.release_year)
        self.assertNotEqual("2005", self.m0.release_year)

    def test_runtime(self):
        self.assertEqual(157, self.m0.runtime)
        self.assertNotEqual("157", self.m0.runtime)

    def test_budget(self):
        self.assertEqual("$150,000,000", self.m0.budget)
        self.assertNotEqual(150_000_000, self.m0.budget)

    def test_box_office(self):
        self.assertEqual("$896,400,000", self.m0.box_office)
        self.assertNotEqual(896_400_000, self.m0.box_office)

    def test_print(self):
        self.assertEqual("Harry Potter and the Goblet of Fire", self.m0.__str__(),
                         "{} is the correct movie.".format(self.m0.movie_title))

