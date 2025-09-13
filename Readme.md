## CMPE300 Project 3

This project is designed to generate and process data files based on user input, supporting multiple configurations and automated batch output generation. It is intended for coursework in CMPE300 and produces output files for further analysis or reporting.

---

### Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Input & Output](#input--output)
- [Batch Generation](#batch-generation)
- [File Structure](#file-structure)
- [Troubleshooting](#troubleshooting)
- [Contact](#contact)

---

## Overview

The project consists of two main scripts:

- `main.py`: Interactive script for generating output files based on user-specified parameters.
- `run.py`: Automates the process to generate all possible output files for different parameter combinations.

## Requirements

- Python 3.x (recommended)
- No external libraries required (uses only standard Python modules)

## Usage

### Running Interactively

To run the program interactively, use one of the following commands in your terminal or command prompt:

```
py main.py
python main.py
python3 main.py
```

You will be prompted to enter:

- **Data size** (e.g., 100, 1000, 10000)
- **k value** (an integer parameter)
- **Input type** (e.g., random, sorted, reversed)

Type `exit` at any prompt to terminate the program.

### Batch Generation

To automatically generate all 27 possible output files (for all combinations of data size, input type, and k value), run:

```
py run.py
python run.py
python3 run.py
```

## Input & Output

- **Input:**

  - The program prompts for data size, k value, and input type.
  - Acceptable values for each parameter are defined in the code (see `main.py`).

- **Output:**
  - For each run, a file named `output-{datasize}-{inputtype}-{kvalue}.txt` is created in the project directory.
  - Each output file contains the results of the computation for the given parameters.

## File Structure

- `main.py` — Main interactive script
- `run.py` — Batch output generator
- `Readme.md` — Project documentation

## Troubleshooting

- Ensure you are using Python 3.x.
- If you encounter issues, check that your terminal is in the project directory.
- Output files will be overwritten if they already exist for the same parameters.