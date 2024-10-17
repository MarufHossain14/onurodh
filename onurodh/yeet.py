import json
import yaml
from onurodh.colorizer import Colorizer  # Adjusted import to "onurodh"
from onurodh.reader import read_file
from onurodh.formatter import format_output
from onurodh.writer import write_response

class Yeeter:
    def __init__(self, colorize=False):
        self.colorizer = Colorizer() if colorize else None

    def yeet(self, filepath):
        try:
            # Reading request data from file
            request_data = read_file(filepath)
            response = self._send_request(request_data)

            # Formatting the response
            formatted_response = format_output(response)

            # Colorizing output if needed
            if self.colorizer:
                formatted_response = self.colorizer.colorize(formatted_response)
            
            # Writing response to stdout
            write_response(formatted_response)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def _send_request(self, request_data):
        # Simplified request sending logic for Onurodh
        import requests
        method = request_data.get('method', 'GET').upper()
        url = request_data.get('url')
        headers = request_data.get('headers', {})
        data = request_data.get('data', {})
        params = request_data.get('params', {})
        
        try:
            if method == 'GET':
                return requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                return requests.post(url, headers=headers, json=data)
            elif method == 'PUT':
                return requests.put(url, headers=headers, json=data)
            elif method == 'DELETE':
                return requests.delete(url, headers=headers)
            else:
                raise ValueError(f"Unsupported method: {method}")
        except requests.RequestException as e:
            raise Exception(f"Request failed: {e}")

