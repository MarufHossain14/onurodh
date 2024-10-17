import unittest
from onurodh import writer  # Updated import


class FakeWriteable:
    def __init__(self):
        self.written_content = None

    def write(self, content):
        self.written_content = content


class TestWriter(unittest.TestCase):
    def setUp(self) -> None:
        self.fake_writeable = FakeWriteable()

    def test_write_response(self):
        content = "Success!"
        writer.write_response(content)
        self.assertEqual(content, "Success!")
