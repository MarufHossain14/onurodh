import json
import yaml
import tempfile
import unittest
from onurodh import reader 


class TestReader(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.file_data = {"method": "GET", "url": "http://example.com"}

    def test_read_request_file_with_json_file(self):
        _, fpath = tempfile.mkstemp(suffix=".json")
        with open(fpath, "w") as f:
            json.dump(self.file_data, f)
        self.assertEqual(reader.read_file(fpath), self.file_data)

    def test_read_request_file_with_yml_file(self):
        _, fpath = tempfile.mkstemp(suffix=".yml")
        with open(fpath, "w") as f:
            yaml.dump(self.file_data, f)
        self.assertEqual(reader.read_file(fpath), self.file_data)

    def test_read_request_file_with_yaml_file(self):
        _, fpath = tempfile.mkstemp(suffix=".yaml")
        with open(fpath, "w") as f:
            yaml.dump(self.file_data, f)
        self.assertEqual(reader.read_file(fpath), self.file_data)

    def test_invalid_file_extension(self):
        with self.assertRaises(ValueError):
            reader.read_file("invalid.txt")
