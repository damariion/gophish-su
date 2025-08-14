# install requirements
python3 -m venv ../.venv
../.venv/Scripts/pip3 install -r requirements.txt
../.venv/Scripts/activate.ps1

[System.Console]::WriteLine("`n:: CONFIGURATION ::")

# - GoPhish API
[System.Console]::Write("- Gophish API key: ")
[System.IO.File]::WriteAllText("shared/.key", [System.Console]::ReadLine())