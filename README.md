# GitHub Demo Website

Basit Python Flask web uygulaması - Docker ile otomatik güncelleme.

## Kurulum

```bash
chmod +x setup.sh
./setup.sh
```

## Kullanım

- Web sitesi: http://localhost:5000
- Kod güncellemek için setup.sh'yi tekrar çalıştırın
- Web arayüzünden "Kodu Güncelle" butonunu kullanabilirsiniz

## Dosyalar

- `app.py` - Flask uygulaması
- `Dockerfile` - Docker image tanımı
- `docker-compose.yml` - Docker Compose konfigürasyonu
- `setup.sh` - Kurulum/güncelleme scripti
- `requirements.txt` - Python bağımlılıkları

## API Endpoints

- `GET /` - Ana sayfa
- `GET /api/status` - Sistem durumu
- `GET /api/update` - Git pull