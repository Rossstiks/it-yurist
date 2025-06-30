# it-yurist

A simple command-line tool for generating basic legal documents. Currently it can create a minimal Non-Disclosure Agreement (NDA).

## Installation

No external dependencies are required. The scripts are written for Python 3.12 or later.

## Usage

Run the CLI with Python:

```bash
python -m it_yurist.cli nda --company "ACME Corp" --partner "John Doe" --output nda.txt
```

If `--output` is omitted, the document will be printed to the console.
