@echo off

REM python pdf_tools.py --help
REM python pdf_tools.py split --help
REM python pdf_tools.py combine --help


SET INPUT_DATA_DIR=D:\git\pdf-split-combine-app\data-in
set INPUT_FILE=git-python.xlsx

SET OUTPUT_DATA_DIR=D:\git\pdf-split-combine-app\data-out
SET OUTPUT_FILENAME=git-and-python-cheatsheet.pdf

python ../src/pdf/pdf_tools.py combine %INPUT_DATA_DIR%\%INPUT_FILE% %OUTPUT_DATA_DIR%\%OUTPUT_FILENAME%

