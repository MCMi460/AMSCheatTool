cd ../
python3 -m pip install -r AMScheat/requirements.txt py2app
py2applet --make-setup app.py
python3 setup.py py2app
open dist
