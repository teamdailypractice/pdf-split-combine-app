# PDF Tools

This tool is used to:

* Split Pdf
* Combine Pdf
* Create bookmarks
* Assumptions
  * currently works only with **unprotected/without password** pdf

## Language, tools

* Python
* VS Code

## Is python installed - windows?

* Run the command: `python --version`
* What's the output?
* If python is installed, where: `where python`

## Setup Steps

* Be in the project directory: `cd pdf-split-combine-app`
* Create python virtual environment - `python -m venv venv`
* Activate the virtual environment:
  * Windows - `venv\Scripts\activate.bat`
  * Linux/Unix/MacOS - `venv\Scripts\activate`
* Install all the required libraries - `pip install -r requirements.txt`
* After finishing work, if any new libraries installed update - `pip freeze > requirements.txt`

## Running the project

* Open and Update the `data-in/git-python.xlsx` to reflect the correct path as your machine
  * source_filepath
  * target_filepath
* Be in the script directory inside the project: `cd scripts`
* Windows - Update `pdf-split.bat` - to have correct path as per your machine
* Windows - run: `pdf-split.bat`

## VS Code setup

* VS Code extension - **View -> Extensions** search and install
  * Python from Microsoft
  * Python Debugger from Microsoft
* Setup the **Python Profile**. How?
  * What is profile? <https://code.visualstudio.com/docs/editor/profiles>
* C + S + P -> Select Interpreter
* Select python interpreter
