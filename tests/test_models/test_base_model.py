import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(instance.created_at, instance.updated_at)

    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        new_updated_at = instance.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['created_at'], instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'], instance.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()
