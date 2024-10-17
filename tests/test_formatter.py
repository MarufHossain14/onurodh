import unittest
from onurodh import formatter  # Updated import


class TestFormatter(unittest.TestCase):
    def test_format_output(self):
        response = {
            'status_code': 200,
            'headers': {'Content-Type': 'application/json'},
            'text': '{"message": "success"}'
        }
        formatted = formatter.format_output(response)
        expected_output = (
            "Status: 200\n"
            "Headers: {'Content-Type': 'application/json'}\n"
            "Body: {\"message\": \"success\"}\n"
        )
        self.assertEqual(formatted, expected_output)
