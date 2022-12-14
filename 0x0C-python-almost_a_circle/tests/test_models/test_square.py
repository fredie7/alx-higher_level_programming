i#!/usr/bin/python3
"""Unittests for Square class"""
import csv
import io
import json
import sys
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    def test_init_empty(self):
        """Initialize with no arguments"""
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_init_size(self):
        """Initialize wtih one argument"""
        s1 = Square(1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_init_size_xy(self):
        """Initialize with size, x, y"""
        s1 = Square(7, 8, 9)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)

    def test_init_all(self):
        """Initialize with size, x, y, id"""
        s1 = Square(7, 8, 9, 21)
        self.assertEqual(s1.width, 7)
        self.assertEqual(s1.height, 7)
        self.assertEqual(s1.x, 8)
        self.assertEqual(s1.y, 9)
        self.assertEqual(s1.id, 21)

    def test_init_size0(self):
        """Initialize with size 0"""
        with self.assertRaises(ValueError) as ve:
            Square(0)
            self.assertEqual(str(ve.exception), "width must be >= 0")

    def test_init_toomany(self):
        """Initialize with too many arguments"""
        with self.assertRaises(TypeError):
            s1 = Square(7, 8, 9, 21, 22)

    def test_init_type(self):
        """Initialize with string value"""
        with self.assertRaises(TypeError):
            Square("1")

    def test_init_type_sizex(self):
        """Initialize with string value"""
        with self.assertRaises(TypeError):
            Square(2, "1")

    def test_init_type_sizexy(self):
        """Initialize with string value"""
        with self.assertRaises(TypeError):
            Square(3, 2, "1")

    def test_init_negative(self):
        """Initialize with a negative value"""
        with self.assertRaises(ValueError) as ve:
            Square(-1)
            self.assertEqual(str(ve.exception), "width must be >= 0")

    def test_init_negative_sizex(self):
        """Initialize with a negative value"""
        with self.assertRaises(ValueError) as ve:
            Square(2, -1)
            self.assertEqual(str(ve.exception), "width must be >= 0")

    def test_init_negative_sizexy(self):
        """Initialize with a negative value"""
        with self.assertRaises(ValueError) as ve:
            Square(3, 2, -1)
            self.assertEqual(str(ve.exception), "width must be >= 0")

    def test_str_size(self):
        """Test __str__() function, intialize with size only"""
        s1 = Square(1)
        s1.id = 3
        self.assertEqual(s1.__str__(), "[Square] (3) 0/0 - 1")

    def test_str_xy(self):
        """Test __str__() function, initialize x, y"""
        s1 = Square(7, 8, 9)
        s1.id = 4
        self.assertEqual(s1.__str__(), "[Square] (4) 8/9 - 7")

    def test_str_all(self):
        """Test __str__() function, initialize all attributes"""
        s1 = Square(7, 8, 9, 21)
        self.assertEqual(s1.__str__(), "[Square] (21) 8/9 - 7")

    def test_display(self):
        """Test inherited display"""
        captured = io.StringIO()
        sys.stdout = captured
        s1 = Square(4)
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "####\n####\n####\n####\n")

    def test_displayxy(self):
        """Test inherited display with x, y values"""
        captured = io.StringIO()
        sys.stdout = captured
        s1 = Square(3, 2, 1)
        s1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n  ###\n  ###\n  ###\n")

    def test_area(self):
        """Test inherited area()"""
        s1 = Square(3)
        self.assertEqual(s1.area(), 9)

    def test_size_property(self):
        """Test setter and getter for size"""
        s1 = Square(3)
        self.assertEqual(s1.size, 3)
        s1.size = 9
        self.assertEqual(s1.size, 9)

    def test_size_property_invalid_value(self):
        """Test if size setter raises ValueException('width must be > 0')"""
        s1 = Square(3)
        with self.assertRaisesRegex(ValueError, "width"):
            s1.size = -3

    def test_size_property_invalid_type(self):
        """Test if size setter raises
        TypeException('width must be an integer')
        """
        s1 = Square(3)
        with self.assertRaisesRegex(TypeError, "width"):
            s1.size = "3"

    def test_update_args(self):
        """Test if update args correctly with too many parameters"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(89, 2, 3, 4, 5)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")

    def test_update_all_args(self):
        """Test if update args correctly"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        """Test if update kw args correctly"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(y=1, size=21, id=99, x=7)
        self.assertEqual(s1.__str__(), "[Square] (99) 7/1 - 21")

    def test_update_args_kwargs(self):
        """Test update args and kwargs (kwargs should not update)"""
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(10, id=7, size=3)
        self.assertEqual(s1.__str__(), "[Square] (10) 10/10 - 10")

    def test_to_dictionary(self):
        """Test to dictionary()"""
        attrs = {"id": 5, "size": 2, "x": 3, "y": 4}
        s1 = Square(2, 3, 4, 5)
        s_dict = s1.to_dictionary()
        self.assertEqual(len(attrs), len(s_dict))
        for k, v in attrs.items():
            self.assertEqual(s_dict[k], v)

    def test_save_to_file_sq(self):
        """Test inhertied save_to_file()"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            sqs = json.load(f)
            self.assertEqual(len(sqs), 2)
            self.assertEqual(s1.to_dictionary(), sqs[0])
            self.assertEqual(s2.to_dictionary(), sqs[1])

    def test_save_to_file_1sq(self):
        """Test inhertied save_to_file()"""
        sq = Square(1)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            sqs = json.load(f)
            self.assertEqual(len(sqs), 1)
            self.assertEqual(sq.to_dictionary(), sqs[0])

    def test_save_to_file_nonesq(self):
        """Test save_to_file() with None"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            sqs = json.load(f)
            self.assertEqual(len(sqs), 0)
            self.assertEqual(sqs, [])

    def test_save_to_file_emptysq(self):
        """Test save_to_file() with empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            sqs = json.load(f)
            self.assertEqual(len(sqs), 0)
            self.assertEqual(sqs, [])

    def test_create_sq(self):
        """Test create()"""
        s1 = Square(10, 7, 3, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s1.__str__(), s2.__str__())
        self.assertNotEqual(s1, s2)

    def test_load_from_file_sq(self):
        """Test inherited load_from_file()"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(len(list_squares_output), len(list_squares_input))
        self.assertEqual(s1.__str__(), list_squares_output[0].__str__())
        self.assertEqual(s2.__str__(), list_squares_output[1].__str__())

    def test_save_to_file_csv_sq(self):
        """Test save_to_file_csv()"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2)
        sqs = [s1, s2]
        Square.save_to_file_csv(sqs)
        with open("Square.csv", "r") as f:
            reader = csv.DictReader(f)
            for row, sq in zip(reader, sqs):
                for k, v in row.items():
                    row[k] = int(v)
                self.assertEqual(row, sq.to_dictionary())

    def test_load_from_file_csv_sq(self):
        """Test inherited load_from_file_csv()"""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(len(list_squares_output), len(list_squares_input))
        for si, so in zip(list_squares_input, list_squares_output):
            self.assertEqual(si.__str__(), so.__str__())

    def test_save_file_csv_none_sq(self):
        """Test save None object to csv file"""
        Square.save_to_file_csv(None)
        with open("Square.csv", "r", newline='') as f:
            sqs = Square.load_from_file_csv()
            self.assertEqual(len(sqs), 0)
            self.assertEqual(sqs, [])

    def test_save_file_csv_empty_sq(self):
        """Test save empty list to csv file"""
        Square.save_to_file_csv([])
        with open("Square.csv", "r", newline='') as f:
            sqs = Square.load_from_file_csv()
            self.assertEqual(len(sqs), 0)
            self.assertEqual(sqs, [])
