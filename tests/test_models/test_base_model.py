# tests/test_models/test_base_model.py
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
    
    def test_str_method(self):
        instance = BaseModel()
        expected_output = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_output)
    
    def test_save_method(self):
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)
    
    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['created_at'], instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'], instance.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
