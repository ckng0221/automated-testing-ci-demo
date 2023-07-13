Before merge into the `main` branch, should create a feature branch, and then perform a `pull request`.

GitHub Actions will be triggered to run `pytest`, to check if all tests passed.

Merge to the `main` branch will be done after approval.

---
To run test cases locally:

Install `pytest`, id don't have
Create virtual environment and install pytest
```cmd
python -m venv venv

.\venv\Scripts\pip.exe install -r requirements.txt
```

After activated virtual environment, on cmd
```cmd
# eg.
.\venv\Scripts\activate.exe
$(venv) pytest

# alternative
.\venv\Scripts\python.exe -m pytest
```

