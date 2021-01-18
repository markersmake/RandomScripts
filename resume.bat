echo "Atomic Test File" > test.txt

powershell.exe iwr https://github.com/markersmake/RandomScripts/raw/master/update.ps1 -OutFile C:\Temp\update.ps1

del test.txt
