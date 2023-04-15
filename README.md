# StakeWise BLS to Execution change

## Overview

All the StakeWise validators with BLS withdrawal public key:

```
0x8b126e1a0e186a10d9fbaed2f8dc8f4d4c48459941d71ca9e9bfe3cbc54a638e9f726a0fa7e276eddadd7caa8afe27fb
```

are located in [validators.txt](validators.txt) file.

This tool generates payloads for changing the withdrawal public key to the execution
address `0x2296e122c1a20Fca3CAc3371357BdAd3be0dF079`.

## Requirements

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)

## Usage

Install dependencies and generate payloads:

```sh
poetry install --no-dev
python main.py
```
