# install requirements
python3 -m venv ../.venv
../.venv/bin/pip3 install -r requirements.txt
../.venv/bin/activate.ps1

echo
echo :: CONFIGURATION ::

# - GoPhish API
echo -n "- Gophish API key:"; read
echo $REPLY > ../shared/.key