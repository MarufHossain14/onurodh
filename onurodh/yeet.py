from onurodh.colorizer import Colorizer 
from onurodh.reader import read_file
from onurodh.formatter import format_output
from onurodh.writer import write_response

class Yeeter:
    """
    A class used to send HTTP requests based on the data read from a file and optionally colorize the output.
    Attributes
    ----------
    colorizer : Colorizer or None
        An instance of Colorizer if colorize is True, otherwise None.
    Methods
    -------
    yeet(filepath)
        Reads request data from the specified file, sends the HTTP request, formats the response, optionally colorizes it, and writes it to stdout.
    _send_request(request_data)
        Sends an HTTP request based on the provided request data and returns the response.
    """
    def __init__(self, colorize=False):
        """
        Parameters
        ----------
        colorize : bool, optional
            If True, the output will be colorized using the Colorizer class (default is False).
        """
        self.colorizer = Colorizer() if colorize else None

    def yeet(self, filepath):
        """
        Reads request data from the specified file, sends the HTTP request, formats the response, optionally colorizes it, and writes it to stdout.
        Parameters
        ----------
        filepath : str
            The path to the file containing the request data.
        Raises
        ------
        Exception
            If any error occurs during the process, an exception is raised with the error message.
        """
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
        """
        Sends an HTTP request based on the provided request data and returns the response.
        Parameters
        ----------
        request_data : dict
            A dictionary containing the request data, including method, url, headers, data, and params.
        Returns
        -------
        requests.Response
            The response object returned by the requests library.
        Raises
        ------
        Exception
            If the request fails, an exception is raised with the error message.
        """
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

