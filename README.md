## Description
API test suite for CRUD on the JSONPlaceholder
`/posts` endpoint (GET, POST, PUT, DELETE), including a negative scenario.

## Requirements
- Python 3.10+
- `pip`

## Install
```bash
pip install -r requirements.txt
```

## Run
```bash
pytest tests/ -v
```

## Project structure
```
project/
├── tests/
│   ├── __init__.py
│   ├── conftest.py      # shared fixtures
│   └── test_posts.py    # /posts endpoint tests
├── requirements.txt     # dependencies
├── README.md            # project instructions
└── .gitignore           # ignored files
```
