Write-Host "Chalo bhai, welcome- let's get to it"

Write-Host "Loading stuff, think about your life till then"

$i = 0
Write-Host "okay, count with me:"
while ($i -lt 3){
    Start-Sleep -Seconds 1
    Write-Host ($i + 1)
    $i++
}

Write-Host "Starting Chrome..."

Start-Process  chrome.exe "--start-maximized --profile-directory=`"Profile 2`" https://chatgpt.com/"

Write-Host "Starting code..."

code "C:\Users\victo\codes_real\making\web"

Write-Host "Starting MechVibes..."

Start-Process "C:\Users\victo\AppData\Local\Programs\Mechvibes\Mechvibes.exe"


