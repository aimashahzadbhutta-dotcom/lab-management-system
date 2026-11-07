# Mini Lab Management System

A command-line lab management tool built in Python for tracking patients, experiments, and drug records. Built as part of my Python learning journey for AI drug research (Biotechnology, Semester 2).

## Features

- **Login system** — username/password verification with a 3-attempt limit
- **Add Patient** — records patient name, age, and report, saved to `patients.csv`
- **Add Experiment** — logs experiment name and result (Passed/Failed) to `experiments.txt`
- **View All Drugs** — lists all drugs from `drugs.json`
- **Search Drug** — look up a specific drug by generic name
- **View saved records** — option to display all patients or experiments after adding new ones

## File Structure
Lab_Management_System/
```
├── Lab_Management_System.py   # main program
├── drugs.json                  # drug database (generic_name field required)
├── patients.csv                 # generated: patient records
├── experiments.txt               # generated: experiment logs
└── README.md
```

## Requirements

- Python 3.9+
- No external dependencies — uses built-in `json` and `csv` modules
- A `drugs.json` file in the same directory, formatted as a list of objects with at least a `generic_name` key, e.g.:
```json
[
  {"generic_name": "Aspirin"},
  {"generic_name": "Ibuprofen"}
]
```

## How to Run
```
python Lab_Management_System.py
```
You'll be prompted to set a username and password, then re-enter them to verify (3 attempts allowed). On success, you'll reach the main menu:
```
1. Add patient
2. Add experiment
3. View all drugs
4. Search Drug
5. Quit
```
## Known Limitations
Login logic has an edge case where both incorrect username and password can incorrectly report success (fix in progress)
No password hashing — credentials are compared in plain text (fine for local practice, not for real use)
patients.csv header is rewritten on every new patient entry (may cause duplicate headers over multiple runs)
## Notes
This project is part of my learning portfolio — built to practice file I/O, dictionaries, JSON handling, and CSV read/write in the context of a lab-data domain.