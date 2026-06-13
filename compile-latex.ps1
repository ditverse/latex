param(
    [switch]$CleanAux
)

# Script PowerShell untuk kompilasi dokumen LaTeX.
# Sumber utama tetap bukped.tex, output PDF menggunakan nama laporan_litma.pdf.

$TexFile = "bukped"
$JobName = "laporan_litma"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Kompilasi LaTeX Document" -ForegroundColor Cyan
Write-Host "  Source : $TexFile.tex" -ForegroundColor Cyan
Write-Host "  Output : $JobName.pdf" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

function Invoke-LatexStep {
    param(
        [string]$Label,
        [scriptblock]$Command
    )

    Write-Host $Label -ForegroundColor Yellow
    & $Command | Out-Null

    if ($LASTEXITCODE -eq 0) {
        Write-Host "      OK Berhasil" -ForegroundColor Green
    }
    else {
        Write-Host "      ! Selesai dengan warning/error, cek $JobName.log bila PDF tidak sesuai" -ForegroundColor Yellow
    }
}

Invoke-LatexStep "[1/4] Menjalankan pdflatex (kompilasi pertama)..." {
    pdflatex "-jobname=$JobName" -interaction=nonstopmode "$TexFile.tex"
}

Invoke-LatexStep "[2/4] Menjalankan bibtex..." {
    bibtex "$JobName"
}

Invoke-LatexStep "[3/4] Menjalankan pdflatex (kompilasi kedua)..." {
    pdflatex "-jobname=$JobName" -interaction=nonstopmode "$TexFile.tex"
}

Invoke-LatexStep "[4/4] Menjalankan pdflatex (kompilasi ketiga)..." {
    pdflatex "-jobname=$JobName" -interaction=nonstopmode "$TexFile.tex"
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan

if (Test-Path "$JobName.pdf") {
    $pdfInfo = Get-Item "$JobName.pdf"
    Write-Host "OK Kompilasi selesai!" -ForegroundColor Green
    Write-Host "  File: $($pdfInfo.Name)" -ForegroundColor White
    Write-Host "  Ukuran: $([math]::Round($pdfInfo.Length/1KB, 2)) KB" -ForegroundColor White
    Write-Host "  Terakhir diupdate: $($pdfInfo.LastWriteTime)" -ForegroundColor White

    if ($CleanAux) {
        $auxFiles = @(
            "$JobName.aux",
            "$JobName.log",
            "$JobName.out",
            "$JobName.toc",
            "$JobName.lot",
            "$JobName.lof",
            "$JobName.equ",
            "$JobName.bbl",
            "$JobName.blg",
            "$JobName.bcf",
            "$JobName.run.xml",
            "$JobName-blx.bib"
        )

        foreach ($file in $auxFiles) {
            Remove-Item -LiteralPath $file -ErrorAction SilentlyContinue
        }

        Write-Host "OK File auxiliary telah dihapus" -ForegroundColor Green
    }
    else {
        Write-Host "  File auxiliary dipertahankan. Gunakan -CleanAux untuk menghapusnya." -ForegroundColor White
    }
}
else {
    Write-Host "X Kompilasi gagal! PDF tidak ditemukan." -ForegroundColor Red
    Write-Host "  Cek file $JobName.log untuk detail error." -ForegroundColor Yellow
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
