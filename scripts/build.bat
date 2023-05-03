cd ..\
python -m pip install -r AMScheat/requirements.txt pyinstaller
python -m PyInstaller --onefile --clean --noconsole --name=AMSCheatTool --icon=resources/icon.ico app.py
start dist
