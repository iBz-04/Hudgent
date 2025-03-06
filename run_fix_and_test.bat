@echo off
echo Islamic Knowledge Base System - Fix and Test
echo ==========================================
echo.

:: Step 1: Fix the data.json file
echo Step 1: Fixing data.json file...
python fix_data_json.py
if %ERRORLEVEL% NEQ 0 (
    echo Error fixing data.json. Stopping.
    pause
    exit /b 1
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

:: Step 3: Test the search functionality
echo Step 3: Testing search functionality...
python test_search.py
if %ERRORLEVEL% NEQ 0 (
    echo Search test failed. Stopping.
    pause
    exit /b 1
)
echo.

:: Step 4: Run the main Q&A interface
echo Step 4: Starting the Islamic Q^&A interface...
python main.py
echo.

echo Process completed.
pause 