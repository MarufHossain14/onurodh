def format_output(response):
    # Assuming the response object from the requests module
    output = f"Status: {response.status_code}\n"
    output += f"Headers: {response.headers}\n"
    output += f"Body: {response.text}\n"
    return output
