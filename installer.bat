@echo off
set /p loc=Enter the full location to setup the things: 
cd %loc%
git clone https://github.com/amanjha8100/chords.git

echo Downlaoding python 3.9.7 ...
powershell -Command "invoke-WebRequest https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -Outfile python_installer.exe"
echo Python Downloaded

mkdir dep
cd dep
mkdir Pyhton
cd..

::7Zip download and installtion
mkdir setups
cd setups

powershell -Command "invoke-WebRequest https://www.7-zip.org/a/7z1900-x64.exe -Outfile 7zip.exe"
7zip.exe/S 
set path=%path%;C:\Program Files\7-Zip

echo Dowloading ffmpeg...
powershell -Command "invoke-WebRequest https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z -Outfile ffmpeg_installer.7z"
7z x -o"%loc%\dep\" "ffmpeg_installer.7z"
set path=%path%;%loc%\dep\ffmpeg-2021-10-11-git-90a0da9f14-full_build\bin

echo Installing python...

python_installer.exe/passive TargetDir="%loc%\dep\Python" PrependPath=1
echo Python installed

cd..
cd chords
pip install -r requirements.txt

pause
