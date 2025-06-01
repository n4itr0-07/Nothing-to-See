# ================================================
# PowerShell Profile - Equivalent to .bashrc
# Author: Virus_xx
# Location: $PROFILE
# ================================================

# ------------- Terminal Aesthetics ---------------
# Enable terminal color support
Import-Module -Name PSReadLine
Set-PSReadLineOption -EditMode Emacs
Set-PSReadLineOption -PredictionSource History
Set-PSReadLineOption -PredictionViewStyle InlineView
Set-PSReadLineOption -Colors @{
    "Command" = [ConsoleColor]::Cyan
    "Parameter" = [ConsoleColor]::Yellow
    "String" = [ConsoleColor]::Green
}

# ------------- Prompt Customization --------------
function global:prompt {
    $user = [System.Security.Principal.WindowsIdentity]::GetCurrent().Name
    $path = Get-Location
    $git = Get-GitBranch

    $promptSymbol = "❯"
    $colorUser = "`e[38;5;81m"
    $colorPath = "`e[38;5;75m"
    $colorGit = "`e[38;5;214m"
    $colorReset = "`e[0m"

    "$colorUser$user $colorPath$path $colorGit$git$colorReset`n$promptSymbol "
}

# Show current Git branch (if inside a repo)
function global:Get-GitBranch {
    if (Test-Path .git -or (Get-Command git -ErrorAction SilentlyContinue)) {
        $branch = git rev-parse --abbrev-ref HEAD 2>$null
        if ($LASTEXITCODE -eq 0) {
            return " $branch"
        }
    }
    return ""
}

# ------------- Aliases ---------------------------
Set-Alias ll Get-ChildItem
Set-Alias la "Get-ChildItem -Force"
Set-Alias grep Select-String
Set-Alias .. Set-Location ..
Set-Alias cls Clear-Host
Set-Alias ports "Get-NetTCPConnection | Where-Object { \$_.State -eq 'Listen' }"

# ------------- Custom Functions ------------------
function reload-profile {
    . $PROFILE
    Write-Host "Profile reloaded!" -ForegroundColor Green
}

function extract {
    param([string]$file)
    switch -Wildcard ($file) {
        "*.zip" { Expand-Archive $file -Force }
        "*.tar.gz" { tar -xvzf $file }
        "*.tar" { tar -xvf $file }
        "*.7z" { & 'C:\Program Files\7-Zip\7z.exe' x $file }
        default { Write-Host "Unknown archive format." }
    }
}

function find-port {
    param($port)
    netstat -aon | Select-String ":$port"
}

# ------------- History Settings ------------------
Set-PSReadLineOption -HistorySavePath "$env:APPDATA\PowerShell\PSReadLine\ConsoleHost_history.txt"
Set-PSReadLineOption -HistoryNoDuplicates:$true
Set-PSReadLineOption -MaximumHistoryCount 5000

# ------------- Error Handling --------------------
$ErrorActionPreference = "Stop"

function global:Show-Error {
    param ($err)
    Write-Host "❌ ERROR: $err" -ForegroundColor Red
}
Trap { Show-Error $_; continue }

# ------------- Startup Banner --------------------
Write-Host "`n⚡ Welcome, Virus_xx! PowerShell is ready.`n" -ForegroundColor Cyan

# ------------- Auto-load Modules -----------------
# Example: if you're using Posh-Git or PSFzf
if (Get-Module -ListAvailable -Name posh-git) {
    Import-Module posh-git
}
if (Get-Module -ListAvailable -Name PSFzf) {
    Import-Module PSFzf
}