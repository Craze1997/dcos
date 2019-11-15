$ErrorActionPreference = "stop"
New-Item -ItemType Directory "$env:PKG_PATH/bin/install"
New-Item -ItemType Directory "$env:PKG_PATH/etc"
Add-Type -AssemblyName System.IO.Compression.FileSystem
function Unzip {
    param([string]$zipfile, [string]$outpath)
    [System.IO.Compression.ZipFile]::ExtractToDirectory($zipfile, $outpath)
}
Unzip "c:\pkg\src\nssm\nssm-2.24.zip" "c:\pkg\src\nssm\"

Copy-Item -Recurse -Path "c:/pkg/src/nssm/nssm-2.24/win64/*" "$env:PKG_PATH/bin/install"
Copy-Item "pkg/extra/package.extra" "$env:PKG_PATH/etc/"
Copy-Item "pkg/extra/install.ps1" "$env:PKG_PATH/etc/"
