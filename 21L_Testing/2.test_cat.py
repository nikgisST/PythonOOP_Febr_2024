from unittest import TestCase, main
from Second_Test_Cat.cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Pancho")  # Arrange + Act

    def test_correct_init(self):
        self.assertEqual("Pancho", self.cat.name)   # Assert
        self.assertFalse(self.cat.fed)             # Assert
        self.assertFalse(self.cat.sleepy)         # Assert
        self.assertEqual(0, self.cat.size)        # Assert

    def test_feed_cat_makes_cat_sleepy_and_not_hungry_expect_size_increase_by_1(self):
        expected_size = self.cat.size + 1  # Arrange

        self.cat.eat()   # Act

        self.assertTrue(self.cat.fed)     # Assert
        self.assertTrue(self.cat.sleepy)   # Assert
        self.assertEqual(expected_size, self.cat.size)  # Assert

    def test_feed_cat_when_cat_is_already_fed_raise_exception(self):
        self.cat.fed = True  # Arrange

        with self.assertRaises(Exception) as ex:
            self.cat.eat()  # Act

        self.assertEqual('Already fed.', str(ex.exception))  # Assert

    def test_sleepy_cat_sleeps_and_its_not_sleepy_after_that(self):
        self.cat.sleepy = True  # Arrange
        self.cat.fed = True   # Arrange

        self.cat.sleep()  # Act

        self.assertFalse(self.cat.sleepy)   # Assert

    def test_make_hungry_cat_sleep_raises_exception(self):
        self.cat.fed = False  # Arrange

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()  # Act

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))  # Assert


if __name__ == "__main__":
    main()
