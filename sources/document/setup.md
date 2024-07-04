# Setup IDE


## 1. Setup Extension for vscode
- create profile from ide-vscode-py.code-profile file
  - folder: sources/ide
  - file: ide-vscode-py.code-profile

## 2. Setup Environment for each python project
- refer
  - https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- update pip
  - open terminal/shell; type: python.exe -m pip install --upgrade pip
- create new venv
  - move to where you need to create: cd [folder]
  - open terminal/shell; type: python -m venv [name_ven]
- not create new venv
  - here: root folder
  - command: python -m venv .venv
- activate .venv to use venv
  - open terminal/shell; type:
    - command:
      - mac: source .venv/bin/activate
      - win: .venv\Scripts\activate
- Prepare pip
  - open terminal/shell; type: python -m pip install --upgrade pip
- version pip
  - command: python -m pip --version
- create new requirements.txt file
  - store all libraries that need to be installed
- after install lib for project
  - open terminal/shell; type: pip install -r source/settings/requirements.txt

- run code in jupyter
  - select env have added
  - install:
    - command: pip install -U ipykernel

- check pip list -> shows all installed packages/libs
  - command: pip list
- freezing dependencies
  - pip can export a list of all installed packages and their versions
  - using the freeze command: python -m pip freeze
- use freeze | findstr ... to check lib (changed: grep -> findstr)
  - command: pip freeze | findstr pyarrow
- install pyarrow
  - command: pip install pyarrow


- exit .venv
  - command: deactivate




