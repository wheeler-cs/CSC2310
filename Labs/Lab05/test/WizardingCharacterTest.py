from unittest import TestCase

from character_class import WizardingCharacter


class WizardingCharacterTest(TestCase):

    def setUp(self) -> None:
        data = ["1", "Harry Potter", "Human", "Male", "Gryffindor", "Stag", "Holly", "Phoenix Feather"]
        self.hp = WizardingCharacter(data)

    def test_name(self):
        self.assertEqual("Harry Potter", self.hp.character_name)

    def test_id(self):
        self.assertEqual(1, self.hp.character_id)

    def test_species(self):
        self.assertEqual("Human", self.hp.species)

    def test_print(self):
        self.assertEqual("Harry Potter, House: Gryffindor", self.hp.__str__())

    def test_patronus(self):
        self.fail()
