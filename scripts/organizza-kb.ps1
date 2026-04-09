param(
    [string]$SourcePath = "E:\annalisa\file-redatti",
    [string]$TargetRoot = "E:\annalisa\knowledge-base",
    [switch]$WhatIf
)

function Get-FrontMatter {
    param(
        [string]$FilePath
    )

    $content = Get-Content -LiteralPath $FilePath -Raw -Encoding UTF8

    if ($content -notmatch '(?s)^---\s*(.*?)\s*---') {
        throw "Front matter non trovato nel file: $FilePath"
    }

    $fm = $matches[1]
    $result = @{}

    $currentKey = $null
    $lines = $fm -split "`r?`n"

    foreach ($line in $lines) {
        if ($line -match '^\s*$') {
            continue
        }

        if ($line -match '^([A-Za-z0-9_]+):\s*(.*)$') {
            $currentKey = $matches[1]
            $value = $matches[2].Trim()

            if ($value -eq '') {
                $result[$currentKey] = @()
            }
            else {
                $result[$currentKey] = $value.Trim('"').Trim("'")
            }

            continue
        }

        if ($line -match '^\s*-\s*(.+?)\s*$' -and $null -ne $currentKey) {
            if ($result[$currentKey] -isnot [System.Collections.IList]) {
                $result[$currentKey] = @()
            }
            $result[$currentKey] += $matches[1].Trim().Trim('"').Trim("'")
        }
    }

    return $result
}

function Convert-ToSlug {
    param(
        [string]$Text
    )

    if ([string]::IsNullOrWhiteSpace($Text)) {
        return $null
    }

    $slug = $Text.ToLowerInvariant()

    $map = @{
        'à'='a'; 'á'='a'; 'â'='a'; 'ä'='a'; 'ã'='a'
        'è'='e'; 'é'='e'; 'ê'='e'; 'ë'='e'
        'ì'='i'; 'í'='i'; 'î'='i'; 'ï'='i'
        'ò'='o'; 'ó'='o'; 'ô'='o'; 'ö'='o'; 'õ'='o'
        'ù'='u'; 'ú'='u'; 'û'='u'; 'ü'='u'
        'ç'='c'; 'ñ'='n'
    }

    foreach ($k in $map.Keys) {
        $slug = $slug.Replace($k, $map[$k])
    }

    $slug = $slug -replace '[^a-z0-9]+', '-'
    $slug = $slug -replace '^-+', ''
    $slug = $slug -replace '-+$', ''
    $slug = $slug -replace '-{2,}', '-'

    return $slug
}

function Get-NormalizedFileName {
    param(
        [string]$FileName
    )

    $name = [System.IO.Path]::GetFileNameWithoutExtension($FileName)

    if ($name.ToLowerInvariant().EndsWith('.md')) {
        $name = [System.IO.Path]::GetFileNameWithoutExtension($name)
    }

    return $name
}

$files = Get-ChildItem -LiteralPath $SourcePath -File |
    Where-Object { $_.Name -match '\.md(\.md)?$' }

foreach ($file in $files) {
    try {
        $frontMatter = Get-FrontMatter -FilePath $file.FullName

        $domain   = Convert-ToSlug $frontMatter['domain']
        $feature  = Convert-ToSlug $frontMatter['feature']
        $docKind  = Convert-ToSlug $frontMatter['doc_kind']

        if (-not $domain -or -not $feature -or -not $docKind) {
            throw "domain/feature/doc_kind mancanti o non validi"
        }

        $baseName = Get-NormalizedFileName -FileName $file.Name
        $slug = Convert-ToSlug $baseName

        if (-not $slug) {
            throw "Impossibile generare slug dal file name"
        }

        $destDir = Join-Path $TargetRoot "$domain\$feature\$docKind"
        $destFile = Join-Path $destDir "$slug.md"

        Write-Host "FILE     : $($file.FullName)"
        Write-Host "DEST DIR : $destDir"
        Write-Host "DEST FILE: $destFile"
        Write-Host ""

        if (-not $WhatIf) {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
            Move-Item -LiteralPath $file.FullName -Destination $destFile -Force
        }
    }
    catch {
        Write-Warning "Saltato file '$($file.FullName)': $($_.Exception.Message)"
    }
}