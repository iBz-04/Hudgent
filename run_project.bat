@echo off
echo Islamic Knowledge Base System
echo ===========================
echo.

:: Create necessary directories
echo Creating directories...
if not exist "data" mkdir data
if not exist "indexer\index" mkdir indexer\index
echo.

:: Step 0: Create sample data first
echo Step 0: Creating sample data...
python create_sample_data.py
if %ERRORLEVEL% NEQ 0 (
    echo Error creating sample data. Stopping.
    pause
    exit /b 1
)
echo.

:: Step 1: Run the crawler (optional since we have sample data)
echo Step 1: Running the crawler...
echo Note: This step is optional since we already have sample data.
set /p run_crawler="Do you want to run the crawler? (y/n): "
if /i "%run_crawler%"=="y" (
    cd crawler
    python run_crawler.py
    cd ..
)
echo.

:: Step 2: Build the index
echo Step 2: Building the search index...
cd indexer
python build_index.py
if %ERRORLEVEL% NEQ 0 (
    echo Error building index. Stopping.
    cd ..
    pause
    exit /b 1
)
cd ..
echo.

:: Step 3: Run the main Q&A interface
echo Step 3: Starting the Islamic Q^&A interface...
python main.py
echo.

echo Process completed.
pause 