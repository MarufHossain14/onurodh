def format_output(response: requests.Response) -> str:
    return (
        f"Status: {response.status_code}\n"
        f"Headers: {json.dumps(dict(response.headers), indent=2)}\n"
        f"Body: {response.text[:500]}...\n"
    )