from unittest import TestCase, main
from Third_List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, "hello")  # Arrange + Act

    def test_correct_init_ignores_non_int_values(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())  # Assert

    def test_add_non_integer_value_to_the_list_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)  # Arrange + Act

        self.assertEqual("Element is not Integer", str(ve.exception))   # Assert

    def test_add_integer_adds_the_integer_to_the_list(self):
        expected_list = self.i_list.get_data() + [4]   # Arrange

        self.i_list.add(4)   # Act

        self.assertEqual(expected_list, self.i_list.get_data())  # Assert

    def test_remove_index_with_out_of_range_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index()   # Arrange + Act

        self.assertEqual("Index is out of range", str(ie.exception))  # Assert

    def test_remove_index_with_valid_index(self):
        self.i_list.remove_index(1)    # Arrange + Act

        self.assertEqual([1, 3], self.i_list.get_data())  # Assert

    def test_get_with_out_of_range_index(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(1000)   # Arrange + Act

        self.assertEqual("Index is out of range", str(ie.exception))  # Assert

    def test_get_with_valid_index_returns_value_on_index(self):
        result = self.i_list.get(1)  # Act

        self.assertEqual(2, result)   # Assert

    def test_insert_on_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(1000, 5)   # Arrange + Act

        self.assertEqual("Index is out of range", str(ie.exception))  # Assert

    def test_insert_on_valid_index_with_non_integer_type_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1, 6.7)  # Arrange + Act

        self.assertEqual("Element is not Integer", str(ve.exception))  # Assert

    def test_insert_integer_on_valid_index(self):
        expected_list = self.i_list.get_data().copy()  # Arrange
        expected_list.insert(1, 5)   # Arrange

        self.i_list.insert(1, 5)   # Act

        self.assertEqual(expected_list, self.i_list.get_data())  # Assert

    def test_get_biggest_number(self):
        result = self.i_list.get_biggest()  # Arrange + Act
        self.assertEqual(3, result)         # Assert

    def test_get_index(self):
        result = self.i_list.get_index(2)  # Arrange + Act
        self.assertEqual(1, result)        # Assert


if __name__ == "__main__":
    main()
