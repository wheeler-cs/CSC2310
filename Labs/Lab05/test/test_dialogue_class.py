from unittest import TestCase
from dialogue_class import Dialogue
from character_class import WizardingCharacter


class TestDialogue(TestCase):

    def setUp(self) -> None:
        data = ["97", "4", "10", "5", "You're a wizard, Harry."]
        self.d_obj = Dialogue(data)
        rhdata = ["5", "Rubeus Hagrid", "Half-Human/Half-Giant", "Male", "Gryffindor", "", "Oak", ""]
        self.hagrid = WizardingCharacter(rhdata)
        hpdata = ["1", "Harry Potter", "Human", "Male", "Gryffindor", "Stag", "Holly", "Phoenix Feather"]
        self.harry = WizardingCharacter(hpdata)

    def test_id(self):
        self.assertEqual(97, self.d_obj.id)
        self.assertNotEqual(1, self.d_obj.id)

    def test_chapter(self):
        self.assertEqual(4, self.d_obj.chapter)
        self.assertNotEqual(5, self.d_obj.chapter)

    def test_place(self):
        self.assertEqual(10, self.d_obj.place)
        self.assertNotEqual(11, self.d_obj.place)

    def test_character(self):
        self.assertEqual(5, self.d_obj.character)
        self.assertNotEqual(1, self.d_obj.character)

    def test_dialogue(self):
        self.assertEqual("You're a wizard, Harry.", self.d_obj.dialogue)
        self.assertNotEqual("You're a wizard, Harry.".lower(), self.d_obj.dialogue)

    def test_spoken_by(self):
        self.assertTrue(self.d_obj.spoken_by(self.hagrid))
        self.assertFalse(self.d_obj.spoken_by(self.harry))

    def test_print(self):
        self.assertEqual("You're a wizard, Harry.",
                         self.d_obj.__str__(), "{} was spoken by {}.".format(self.d_obj, self.hagrid))
