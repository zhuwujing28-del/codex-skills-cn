[CmdletBinding()]
param(
    [string]$AgentEvalsPath
)

$ErrorActionPreference = "Stop"
$codexSkillsPath = Split-Path $PSScriptRoot -Parent
if (-not $AgentEvalsPath) {
    $AgentEvalsPath = Join-Path (Split-Path $codexSkillsPath -Parent) "agent-evals-cn"
}

function Invoke-RepositoryValidator {
    param(
        [Parameter(Mandatory)]
        [string]$RepositoryPath,

        [Parameter(Mandatory)]
        [string]$ValidatorPath,

        [Parameter(Mandatory)]
        [string]$RepositoryName
    )

    $resolvedRepositoryPath = (Resolve-Path -LiteralPath $RepositoryPath -ErrorAction Stop).Path
    $resolvedValidatorPath = Join-Path $resolvedRepositoryPath $ValidatorPath
    if (-not (Test-Path -LiteralPath $resolvedValidatorPath -PathType Leaf)) {
        throw "$RepositoryName validator not found: $resolvedValidatorPath"
    }

    Write-Host "==> Validating $RepositoryName"
    Push-Location $resolvedRepositoryPath
    try {
        if (Get-Command py -ErrorAction SilentlyContinue) {
            & py -3 $ValidatorPath
        }
        else {
            & python $ValidatorPath
        }
        if ($LASTEXITCODE -ne 0) {
            throw "$RepositoryName validation failed with exit code $LASTEXITCODE"
        }
    }
    finally {
        Pop-Location
    }
}

Invoke-RepositoryValidator `
    -RepositoryPath $codexSkillsPath `
    -ValidatorPath "scripts\validate-skills.py" `
    -RepositoryName "codex-skills-cn"
Invoke-RepositoryValidator `
    -RepositoryPath $AgentEvalsPath `
    -ValidatorPath "scripts\validate.py" `
    -RepositoryName "agent-evals-cn"

Write-Host "Cross-repository validation passed."
