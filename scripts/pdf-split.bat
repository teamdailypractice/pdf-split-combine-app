@echo off

REM python pdf_tools.py --help
REM python pdf_tools.py split --help
REM python pdf_tools.py combine --help


SET INPUT_DATA_DIR=D:\git\pdf-split-combine-app\data-in
set INPUT_FILE=git-python.xlsx

python ../src/pdf/pdf_tools.py split %INPUT_DATA_DIR%\%INPUT_FILE%

