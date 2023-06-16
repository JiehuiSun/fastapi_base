# FastApi Base

*fastapi + mongodb*

### Structure
```shell
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   ├── http_error.py
│   │   │   └── validation_error.py
│   │   └── routes
│   │       ├── __init__.py
│   │       ├── api.py
│   │       └── example.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── events.py
│   │   └── logging.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── common.py
│   │   ├── domain
│   │   │   ├── __init__.py
│   │   │   ├── base_model.py
│   │   │   └── example.py
│   │   ├── events.py
│   │   └── schemas
│   │       ├── __init__.py
│   │       └── example.py
│   └── utils
│       └── __init__.py
├── poetry.lock
├── pyproject.toml
├── requirements.txt
└── tests
    └── __init__.py
```
...
