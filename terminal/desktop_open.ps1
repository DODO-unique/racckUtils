Write-Host "Chalo bhai, welcome- let's get to it"

Write-Host "Loading stuff, think about your life till then"

$i = 0
Write-Host "okay, count with me:"
while ($i -lt 3){
    Start-Sleep -Seconds 1
    Write-Host ($i + 1)
    $i++
}
$i = 1

Write-Host "Pick one of the following things you'd like to work on today:"

Write-Host "1. Pyferno"
Write-Host "2. Learning web"
Write-Host "3. Strack"
Write-Host "4. Your own? Opening codes_real for you, then..."
Write-Host "5. You opened it already? Okay, cool, I will shut up then."
Write-Host "6. Chill? We can do that too, Gaurav- remember who you are. A torus of dust, warm against the absolute zero. Who will shine for this world if you give up today? You are allowed to take breaks until they are guiltfree, or you aren't."

$choice = Read-Host ">>"
$locations = "C:\Users\victo\codes_real\making\python", "C:\Users\victo\codes_real\making\web\learning", "C:\Users\victo\codes_real\making\web\Strack", "C:\Users\victo\codes_real", "exit 0", "It's okay, new-born. Go read/write/compose something. Pray, beg to your art before you do to recruiters, come back stronger than ever. You aren't alive until you don't feel cringe about it"

if ($choice -lt 4){
	Write-Host "Starting code..."
	code $locations[$choice-1]	
}

if ($choice -eq 4){
	Write-Host "Open a file"
	explorer.exe $locations[$choice-1]
}

if ($choice -eq 5){
	Write-Host "Bye, bye! Tee-hee~"
	Invoke-Expressions $locations[$choice-1]
}

if ($choice -eq 6){
	Write-Host $locations[$choice-1]
	Start-Sleep -Seconds 120
}

Write-Host "Starting venv..."

nomnomNecromancer\Scripts\Activate.ps1

Write-Host "Starting Chrome..."

Start-Process  chrome.exe "--start-maximized --profile-directory=`"Profile 2`" https://chatgpt.com/"


Write-Host "Starting MechVibes..."

Start-Process "C:\Users\victo\AppData\Local\Programs\Mechvibes\Mechvibes.exe"