# Onurodh - Python CLI Program for Sending Requests

## Project Overview

"Onurodh" is a Python-based CLI program designed for making HTTP requests by reading request data from JSON or YAML files. It's made with ease of use in mind, perfect for human-friendly interactions.

---

## Installation

```bas
pip install onurodh
```

(or)

```bash
pip3 install onurodh
```

## Usage Example

### Help with Command-line Arguments

```bash
onurodh --help
```

### Sending a Request via File

```bash
onurodh -f "path/to/request.yml"
```

### Enabling Colorized Output

```bash
onurodh -f "path/to/request.yml" -c
```

### Disclaimer

On some Windows setups, using `onurodh` globally might cause issues. To prevent this, install it in a virtual environment.

```bash
python3 -m venv onurodh_env
```

Activate the environment:

```bash
# Windows
.\onurodh_env\Scripts\activate

# macOS/Linux
source onurodh_env/bin/activate
```

Then, install Onurodh within the virtual environment.

---

## Redirection

You can redirect output and headers:

```bash
onurodh -f "path/to/request.yml" > response.json 2> headers.txt
```

Or redirect both output and headers to one file:

```bash
onurodh -f "path/to/request.yml" > output.txt 2>&1
```

---

## Example Request Files

### GET Example

```yaml
url: https://api.example.com/data
method: get
params:
  limit: 50
  offset: 0
headers:
  accept: application/json
timeout: 5000
```

### POST Example

```yaml
url: https://api.example.com/create
method: post
headers:
  Authorization: Bearer your_token
  Content-Type: application/json
data:
  title: Task Title
  completed: false
timeout: 5000
```

### PUT Example

```yaml
url: https://api.example.com/update/1
method: put
headers:
  Content-Type: application/json
data:
  title: Updated Task Title
  completed: true
timeout: 5000
```

### DELETE Example

```yaml
url: https://api.example.com/delete/1
method: delete
```

---

## Full YAML Request Format

```yaml
method: XXX # (REQUIRED) GET, POST, PUT, DELETE, etc.
url: XXX # (REQUIRED) must start with http:// or https://

params: 
  key1: value1
  key2: value2

data: # For POST/PUT requests
  field1: value1
  field2: value2

headers: 
  Content-Type: application/json
  Authorization: Bearer token_string

timeout: 3.0 # in seconds

verify: true # TLS certificate verification (true/false or path to cert)
```

---

## Development

1. Clone the repo and install the dependencies:

```bash
git clone https://github.com/yourusername/onurodh.git
cd onurodh
pip install -r requirements.txt
```

2. Commit and push your changes.

---

## Contributing

Fork the repo and make a pull request following the same steps:

```bash
git checkout -b feature/new-feature
git commit -am 'Add new feature'
git push origin feature/new-feature
```

---
