@echo off
set /p loc=Enter the location of your reposiotry folder to setup the things: 
cd %loc%

echo Downlaoding python 3.9.7 ...
powershell -Command "invoke-WebRequest https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -Outfile python_installer.exe"
echo Python Downloaded
pause

mkdir dep
echo Installing python...
mkdir Python
python_installer.exe/passive TargetDir="%loc%\dep\Python" PrependPath=1
echo Python installed

cd chords
pip install -r requirements.txt

pause
