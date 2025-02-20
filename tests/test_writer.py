import unittest
from onurodh import writer


class FakeWriteable:
    """Fake file-like object for testing write operations."""
    def __init__(self):
        self.written_content = None

    def write(self, content):
        self.written_content = content


class TestWriter(unittest.TestCase):
    def setUp(self):
        """Initialize a fake writable object before each test."""
        self.fake_writeable = FakeWriteable()

    def test_write_response(self):
        """Test if `writer.write_response` correctly writes content."""
        content = "Success!"
        writer.write_response(content, self.fake_writeable)  # Assuming writer.write_response takes a file-like object
        self.assertEqual(self.fake_writeable.written_content, content)


if __name__ == "__main__":
    unittest.main()
