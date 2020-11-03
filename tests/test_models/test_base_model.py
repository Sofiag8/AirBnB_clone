#!/usr/bin/python3
"""
unittest for base model
"""
import unittest
from models.base_model import BaseModel
import datetime
from models.engine.file_storage import FileStorage
import os
import json


class BaseModelTest(unittest.TestCase):
    """
    test for base model
    """
    obj_dict = "[BaseModel] (1234-5678-9012) {'id': '1234-5678-9012', " \
               "'created_at': datetime.datetime(2019, 11, 12, 8, 31, 23, " \
               "541848), 'updated_at': datetime.datetime(2019, 11, 12, 8, " \
               "31, 23, 541852)}"
    b = BaseModel()

    b.created_at = datetime.datetime(2019, 11, 12, 8, 31, 23, 541848)
    b.updated_at = datetime.datetime(2019, 11, 12, 8, 31, 23, 541852)
    b.id = "1234-5678-9012"

    def test_ids_maker(self):
        """
        test to generate the id
        """
        obj = BaseModel()
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertTrue(obj.id != obj1.id)
        self.assertTrue(obj.id != obj2.id)
        self.assertTrue(obj1.id != obj2.id)

    def test_setUp(self):
        """
        test the set up
        """
        pass

    def test_basemodel_str(self):
        """
        test base model print
        """
        b = BaseModel()
        s = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(s, str(b))

    def test_file(self):
        """
        test file storage
        """
        FileStorage._FileStorage__objects = {}
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except IOError:
            pass

    def test_basemodel_save_more_args(self):
        """
        tests to save with more arguments
        """
        with self.assertRaises(TypeError):
            BaseModel.save(self, 1, "Hello")



if __name__ == "__main__":
    unittest.main()