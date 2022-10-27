from unittest import TestCase
from chapters_class import Chapters


class TestChapter(TestCase):
    def setUp(self) -> None:
        success_data = [4, "Keeper of the Keys", 1, 4]
        self.c0 = Chapters(success_data)

    def test_chapters_id(self):
        self.assertEqual(4, self.c0.chapter_id)
        self.assertNotEqual(0, self.c0.chapter_id)

    def test_chapters_name(self):
        self.assertEqual("Keeper of the Keys", self.c0.chapter_name)
        self.assertNotEqual("The House of Many Ways", self.c0.chapter_name)

    def test_movie_id(self):
        self.assertEqual(1, self.c0.movie_id)
        self.assertNotEqual(8, self.c0.movie_id)

    def test_movie_chapters(self):
        self.assertEqual(4, self.c0.movie_chapter)
        self.assertNotEqual(10, self.c0.movie_chapter)

    def test_print(self):
        self.assertEqual("Keeper of the Keys", self.c0.__str__(), "{} was the book chapter.".format(self.c0))
