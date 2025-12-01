#!/bin/bash

REPO_URL="https://github.com/SkyFetch0/uni-test"
PROJECT_DIR="uni-test"

echo "🚀 GitHub Demo Website Kurulum/Güncelleme"
echo "=========================================="

# Proje dizini var mı kontrol et
if [ -d "$PROJECT_DIR" ]; then
    echo "📁 Proje dizini mevcut, güncelleniyor..."
    cd $PROJECT_DIR
    
    # Docker container'ı durdur
    echo "🛑 Container durduruluyor..."
    docker compose down 2>/dev/null || true
    
    # Git pull
    echo "📥 En son kod çekiliyor..."
    git pull origin main
    
else
    echo "📥 Proje klonlanıyor..."
    git clone $REPO_URL $PROJECT_DIR
    cd $PROJECT_DIR
fi

# Docker build ve start
echo "🔨 Docker image oluşturuluyor..."
docker compose build

echo "▶️ Container başlatılıyor..."
docker compose up -d

echo "✅ Kurulum tamamlandı!"
echo "🌐 Web sitesi: http://localhost:5000"
echo "=========================================="