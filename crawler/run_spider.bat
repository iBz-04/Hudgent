@echo off
echo Setting up environment for Islamic content crawler...

:: Set the Python path to include the current directory
set PYTHONPATH=%cd%
echo PYTHONPATH set to: %PYTHONPATH%

:: Create data directory if it doesn't exist
if not exist "..\data" mkdir "..\data"
echo Data directory verified

:: List available spiders to verify discovery
echo Checking available spiders:
scrapy list

:: Run the spider with debug logging
echo Running Islamic content crawler...
scrapy crawl website_spider --loglevel DEBUG

echo Crawler finished. Press any key to exit.
pause 