# Production Final Check Script
Write-Host "🔍 Running Production Final Check..." -ForegroundColor Cyan

# Check Node.js version
$nodeVersion = node --version
Write-Host "Node.js Version: $nodeVersion" -ForegroundColor Green

# Check if .env exists
if (Test-Path "../.env") {
    Write-Host "✅ .env file exists" -ForegroundColor Green
} else {
    Write-Host "❌ .env file missing" -ForegroundColor Red
}

# Check if .next exists
if (Test-Path "../website/.next") {
    Write-Host "✅ Build artifacts exist" -ForegroundColor Green
} else {
    Write-Host "⚠️ Build artifacts not found - run npm run build" -ForegroundColor Yellow
}

# Check if node_modules exists
if (Test-Path "../website/node_modules") {
    Write-Host "✅ Dependencies installed" -ForegroundColor Green
} else {
    Write-Host "⚠️ Dependencies not installed - run npm ci" -ForegroundColor Yellow
}

Write-Host "`n✅ Final check complete!" -ForegroundColor Green