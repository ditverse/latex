# Script PowerShell untuk kompilasi Laporan Praktikum PSA
# File: compile-psa.ps1

# Set nama file (tanpa ekstensi)
$TexFile = "laporan_praktikum_psa"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Kompilasi Laporan Praktikum PSA" -ForegroundColor Cyan
Write-Host "  File: $TexFile.tex" -ForegroundColor Cyan
Write-Host "  Output: Root directory" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Kompilasi pertama
Write-Host "[1/4] Menjalankan pdflatex (kompilasi pertama)..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode "$TexFile.tex" | Out-Null
if ($LASTEXITCODE -eq 0) { Write-Host "      OK Berhasil" -ForegroundColor Green }
else { Write-Host "      ! Selesai dengan warning" -ForegroundColor Yellow }

# Menjalankan Biber
Write-Host "[2/4] Menjalankan biber..." -ForegroundColor Yellow
biber $TexFile | Out-Null
if ($LASTEXITCODE -eq 0) { Write-Host "      OK Berhasil" -ForegroundColor Green }
else { Write-Host "      ! Selesai dengan warning" -ForegroundColor Yellow }

# Kompilasi kedua
Write-Host "[3/4] Menjalankan pdflatex (kompilasi kedua)..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode "$TexFile.tex" | Out-Null
if ($LASTEXITCODE -eq 0) { Write-Host "      OK Berhasil" -ForegroundColor Green }
else { Write-Host "      ! Selesai dengan warning" -ForegroundColor Yellow }

# Kompilasi ketiga (final)
Write-Host "[4/4] Menjalankan pdflatex (kompilasi ketiga)..." -ForegroundColor Yellow
pdflatex -interaction=nonstopmode "$TexFile.tex" | Out-Null
if ($LASTEXITCODE -eq 0) { Write-Host "      OK Berhasil" -ForegroundColor Green }
else { Write-Host "      ! Selesai dengan warning" -ForegroundColor Yellow }

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan

# Cek apakah PDF berhasil dibuat
if (Test-Path "$TexFile.pdf") {
    $pdfInfo = Get-Item "$TexFile.pdf"
    Write-Host "OK Kompilasi selesai!" -ForegroundColor Green
    Write-Host "  File: $($pdfInfo.Name)" -ForegroundColor White
    Write-Host "  Ukuran: $([math]::Round($pdfInfo.Length/1KB, 2)) KB" -ForegroundColor White
    
    Write-Host ""
    $cleanup = Read-Host "Hapus file auxiliary? y/n"
    if ($cleanup -eq 'y' -or $cleanup -eq 'Y') {
        Remove-Item "$TexFile.aux", "$TexFile.bbl", "$TexFile.bcf", "$TexFile.blg", "$TexFile.lof", "$TexFile.log", "$TexFile.lot", "$TexFile.out", "$TexFile.run.xml", "$TexFile.toc" -ErrorAction SilentlyContinue
        Write-Host "OK File auxiliary untuk $TexFile telah dihapus" -ForegroundColor Green
    }
}
else {
    Write-Host "X Kompilasi gagal! PDF tidak ditemukan." -ForegroundColor Red
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
