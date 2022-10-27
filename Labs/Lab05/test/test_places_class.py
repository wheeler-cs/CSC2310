from unittest import TestCase
from places_class import Places


class TestPlaces(TestCase):

    def setUp(self) -> None:
        data = [4, "Ollivanders", "Diagon Alley"]
        self.loc0 = Places(data)

    def test_id(self):
        self.assertEqual(4, self.loc0.place_id)
        self.assertNotEqual(100, self.loc0.place_id)

    def test_name(self):
        self.assertEqual("Ollivanders", self.loc0.place_name)
        self.assertNotEqual("Flourish & Blotts", self.loc0.place_name)

    def test_category(self):
        self.assertEqual("Diagon Alley", self.loc0.place_category)
        self.assertNotEqual("Hogwarts", self.loc0.place_category)

    def test_print(self):
        self.assertEqual("Ollivanders", self.loc0.__str__(),
                         "{} is located in {}".format(self.loc0.__str__(), self.loc0.place_category))
        self.assertNotEqual("Honeydukes", self.loc0.__str__())
