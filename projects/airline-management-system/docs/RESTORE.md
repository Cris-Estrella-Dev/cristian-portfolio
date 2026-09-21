# Restore the development project

Backup prepared on 2026-09-21. The application lives inside the
`Cris-Estrella-Dev/cristian-portfolio` repository, on branch `main`.

## Restore on a replacement Mac

Install Git and a compatible Python interpreter. The verified local environment
uses Python 3.9.6. Its installed package versions are recorded in
`requirements-backup-2026-09-21.txt`; the original `requirements.txt` also remains.
A fresh dependency installation on a replacement machine has not been tested.

```sh
git clone https://github.com/Cris-Estrella-Dev/cristian-portfolio.git
cd cristian-portfolio/projects/airline-management-system
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-backup-2026-09-21.txt
python -m pip check
python -m pytest
python -m uvicorn api.main:app --app-dir src --reload
```

Run these commands from the application directory. The API exposes `/health`
and interactive API documentation at `/docs` on localhost port 8000.
The snapshot includes macOS-specific packages such as uvloop; another OS or
Python version may require compatible dependency adjustments.

## Persistence and source assets

The current storage is JSON in `data/bookings.json`, not an SQL database.
The owner confirmed that the three stored bookings and the contact information
in source/tests are fictitious test data. This JSON is already tracked by Git
and is included in the backup. Its existing .gitignore entry does NOT prevent
changes to this tracked file from being committed. Never put real customer data
in it for publication.

`src/services/booking_storage_service.py`, domain `to_dict`/`from_dict` methods,
and `src/api/schemas/booking_schema.py` define serialization and API schemas.
No SQL migrations are required. With no JSON file, the loader returns an empty
list; the tracked `data/.gitkeep` preserves the parent directory for later saves.
Do not run `src/main.py` against valuable data: the demo saves sample bookings.

Source, tests, requirements, pytest configuration, README, editable draw.io UML,
and the architecture PNG are tracked. No separate frontend, package.json,
templates, SQL database, .env or application credentials were found.

## Excluded local files

- `.venv/`: installed dependencies, scripts and interpreter links; recreate it.
- `.pytest_cache/`: generated test cache; recreate it.
- `.DS_Store`, `docs/.DS_Store`, `docs/architecture/.DS_Store`,
  `docs/screenshots/.DS_Store`: macOS folder metadata.
- `__pycache__/` is ignored if generated.

The environment version snapshot preserves the useful information from .venv.
No unique application source was found among ignored files. Secret-file patterns
are now ignored as a precaution; no actual application secrets were identified.
A bundled public CA certificate file in pip is not a private key.

## Validation before backup

55 tests passed under Python 3.9.6; pip check reported no broken requirements.
All Python source/tests parsed. The API imported, health returned OK, OpenAPI
was generated, and all three stored bookings validated against response schemas.
Tests use temporary storage; the existing JSON was not overwritten.

## Independent backup before repair

GitHub is not a full computer backup. Keep a second copy on an external disk or
another trusted destination, ideally encrypted, before handing over the Mac.
Include the repository and any files outside it needed for development, plus
securely stored GitHub access/recovery methods. No external backup destination
was supplied during this audit, so a second off-device backup was not created.
