cd ../
python3 -m pip install -r AMScheat/requirements.txt py2app
py2applet --make-setup app.py resources/icon.icns
sed -i '' -e "s/)/    name='AMSCheatTool')/" setup.py
python3 setup.py py2app
open dist
