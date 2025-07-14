#to create a repo on git remote


function tryFileAdd($value) {
    try {
        New-Item -Name $value -ItemType File -ErrorAction Stop | Out-Null
        Write-Host "Added $value in the repo." -ForegroundColor LightGreen
    }
    catch {
        Write-Host "Some error occurred while adding $value. Either it exists or something else (Debug time). Overwrite? [y/n]" -ForegroundColor Yellow
        $answer = Read-Host
        if ($answer -eq 'y') {
            New-Item -Name $value -ItemType File -Force | Out-Null
            Write-Host "File overwritten." -ForegroundColor Green
        }
        else {
            Write-Host "$value was left untouched." -ForegroundColor Cyan
        }
    }
}

#take the path
$repoPath = (Read-Host "Enter the repo " ).Trim('"').Trim(" ")

#take the URL
$remoURL = Read-Host "Enter the git URL (or go and make it on remote if you forgot) "

#check if the path exists, if it does not we don't add it to avoid duplicates and unintentional creations
if (!(Test-Path "$repoPath")) {
    Write-Host "No path found; fix your life and retry." -ForegroundColor Red
    exit
}

if ("$repoPath" -notmatch '^[a-zA-Z]:\\([^<>:"|?*]+\\)*[^<>:"|?*]+$'){
    Write-Host "Enter valid path."
    exit
}

if ($remoURL -notmatch '^[https:\/\/github.com].+\.git$') {
    Write-Host "That's not a valid Git URL. Try again." -ForegroundColor Red
    exit
}

#warn the mfs because why not- seriously though, highly optional
Write-Host "`nAbout to initialize Git repository at "$repoPath"." -ForegroundColor Cyan
Write-Host "Press Ctrl+C to cancel..." -ForegroundColor DarkCyan
Start-Sleep -Seconds 3
Write-Host "Too late." -ForegroundColor Gray

#move to the listed directory
Set-Location "$repoPath"

#initialise git 
git init
#make a README.md and .gitignore, good habit
# New-Item -Name README.md -ItemType File -Force | Out-Null
# New-Item -Name .gitignore -ItemType File -Force | Out-Null

#add basics to the repo, good habit

tryFileAdd "README.md"
tryFileAdd ".gitignore"

#stage it
git add README.md
git add .gitignore

#ask if there is more to add:
$commits = Read-Host "Do you want to push all the files in the given repo [y/n]?"
if ($commits -eq 'y'){
    git add .
}
else {
    $ignore = Read-Host "Do you want add files to .gitignore [y/n]?"
    if ($ignore -eq 'y'){
        Start-Process notepad ""$repoPath"\.gitignore" -Wait
        Write-Host "Notepad closed, resuming..." -ForegroundColor Yellow
        Write-Host "Processing uploads..."
        git add .
    }
}

#first a inital commit- commits is basically saving changes locally
git commit -m "initial commit"

#add the remote repo which is relevant
git remote add origin $remoURL

#push the local repo to the remote
$branch = (git branch --show-current).Trim()
Write-Host "Pushing changes to $branch branch"
git push -u origin $branch

Write-Host "Done!" -ForegroundColor Green