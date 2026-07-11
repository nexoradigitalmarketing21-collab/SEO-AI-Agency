# Production Deployment Script
param(
    [ParameterSet("Local")]
    [ParameterSet("Docker")]
    [ParameterSet("Vercel")]
    [string]$Target = "Docker"
)

Write-Host "🚀 Deploying Nexora AI SEO Agency..." -ForegroundColor Cyan

switch ($Target) {
    "Docker" {
        Write-Host "Building Docker containers..." -ForegroundColor Yellow
        docker-compose build
        docker-compose up -d
        Write-Host "✅ Docker deployment complete!" -ForegroundColor Green
    }
    "Local" {
        Write-Host "Deploying locally..." -ForegroundColor Yellow
        cd ../website
        npm run build
        npm start
    }
    "Vercel" {
        Write-Host "Deploying to Vercel..." -ForegroundColor Yellow
        cd ../website
        vercel --prod
    }
}

Write-Host "📊 Application available at http://localhost:3000" -ForegroundColor Green