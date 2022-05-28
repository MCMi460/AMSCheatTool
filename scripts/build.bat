cd ..\
python -m pip install -r AMScheat/requirements.txt pyinstaller
python -m PyInstaller --onefile --clean --noconsole app.py
start dist
