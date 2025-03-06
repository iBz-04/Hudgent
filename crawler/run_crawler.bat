@echo off
echo Running Islamic content crawler using Python API...

:: Set the Python path to include the current directory
set PYTHONPATH=%cd%
echo PYTHONPATH set to: %PYTHONPATH%

:: Run the Python script
python run_crawler.py

echo Crawler finished. Press any key to exit.
pause 