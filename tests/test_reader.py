import json
import yaml
import tempfile
import os
import unittest
from onurodh import reader


class TestReader(unittest.TestCase):

    def setUp(self):
        """Set up sample data for testing."""
        self.file_data = {"method": "GET", "url": "http://example.com"}
        self.temp_files = []

    def _create_temp_file(self, suffix, data, dump_func):
        """Helper function to create temporary files."""
        temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
        self.temp_files.append(temp_file.name)
        with open(temp_file.name, "w") as f:
            dump_func(data, f)
        return temp_file.name

    def test_read_json_file(self):
        """Test reading JSON file."""
        fpath = self._create_temp_file(".json", self.file_data, json.dump)
        self.assertEqual(reader.read_file(fpath), self.file_data)

    def test_read_yml_file(self):
        """Test reading .yml file."""
        fpath = self._create_temp_file(".yml", self.file_data, yaml.dump)
        self.assertEqual(reader.read_file(fpath), self.file_data)

    def test_read_yaml_file(self):
        """Test reading .yaml file."""
        fpath = self._create_temp_file(".yaml", self.file_data, yaml.dump)
        self.assertEqual(reader.read_file(fpath), self.file_data)

    def test_invalid_file_extension(self):
        """Test that an invalid file extension raises ValueError."""
        with self.assertRaises(ValueError):
            reader.read_file("invalid.txt")

    def tearDown(self):
        """Clean up temporary files after each test."""
        for fpath in self.temp_files:
            if os.path.exists(fpath):
                os.remove(fpath)


if __name__ == "__main__":
    unittest.main()
