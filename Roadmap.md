# Roadmap — cloud-exposure-scanner

## Multi-cloud
- [ ] Support Azure Blob Storage
- [ ] Support GCP Cloud Storage
- [ ] Support d'autres services compatibles S3 (Wasabi, DigitalOcean Spaces, etc.)

## Améliorations techniques
- [ ] Ajout de tests unitaires
- [ ] Scan parallélisé (threading ou asyncio pour accélérer sur beaucoup de buckets)
- [ ] Détection du listing public (en plus de lecture/écriture)
- [ ] Export du rapport en CSV (en plus du JSON Lines)

## Intégration
- [ ] Intégration au dashboard Nexus (flux de données vers Prometheus/Grafana)
- [ ] Exécution schedulée (cron / GitHub Actions)