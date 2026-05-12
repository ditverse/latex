Set-Location $PSScriptRoot

if (-Not (Test-Path "out")) {
    New-Item -ItemType Directory -Force -Path "out" | Out-Null
}

$mainFile = "proposal_pkm"

function Invoke-PDFLaTeX ([int]$pass) {
    Write-Host "  pdflatex pass $pass..." -NoNewline
    pdflatex -interaction=batchmode -output-directory=out "$mainFile.tex" | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Write-Host " FAILED" -ForegroundColor Red
        Write-Host "`n--- Log (last 40 lines) ---" -ForegroundColor Yellow
        Get-Content "out\$mainFile.log" | Select-Object -Last 40
        exit $LASTEXITCODE
    }
    Write-Host " OK" -ForegroundColor Green
}

Write-Host "Compiling $mainFile.tex ..." -ForegroundColor Cyan

Invoke-PDFLaTeX 1

Write-Host "  bibtex..." -NoNewline
$env:BIBINPUTS = "out;."
bibtex "out\$mainFile" | Out-Null
Remove-Item Env:\BIBINPUTS -ErrorAction SilentlyContinue
Write-Host " OK" -ForegroundColor Green

Invoke-PDFLaTeX 2
Invoke-PDFLaTeX 3

Copy-Item "out\$mainFile.pdf" -Destination "$mainFile.pdf" -Force
Write-Host "Done -> $mainFile.pdf" -ForegroundColor Green
