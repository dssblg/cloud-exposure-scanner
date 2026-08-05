# cloud-exposure-scanner

## À propos
L'outil créé ici a pour but de vérifier la sécurité de ses propres buckets AWS. En effet, une mauvaise configuration, même minime, peut faire sauter la sécurité existante et c'est exactement ce qu'attendent les attaquants : une petite faille, et des données transmises on ne sait où, on ne sait à qui.

En 2025, un bucket cloud mal configuré a exposé des millions de dossiers de patients chez un prestataire de santé américain, un rappel que ce type d'erreur, en apparence anodine, peut avoir des conséquences massives. J'ai décidé de créer cet outil car le cloud est un élément essentiel pour les entreprises comme pour les particuliers, et ce sujet s'inscrit directement dans mon cursus de Master Cybersécurité du Cloud à l'Edge.

Ce projet illustre une approche "attacker's perspective" : comprendre comment un attaquant détecte une mauvaise configuration permet de mieux la prévenir.

## Cadre légal
L'utilisation de cet outil se fera uniquement sur mes propres buckets. Il est interdit de l'utiliser sur des buckets autres que les siens, même s'ils ne sont pas sécurisés.

Cette règle n'est pas qu'une formalité légale : en sécurité offensive, ce qui différencie un audit légitime d'une intrusion n'est pas l'action technique réalisée, mais l'autorisation préalable du propriétaire du système. Scanner un système sans cette autorisation reste illégal, même si la faille trouvée est réelle et même bien intentionnée.

Pour tester la sécurité de systèmes qui ne m'appartiennent pas, la voie légale existe : elle passe par des programmes de bug bounty, où l'entreprise définit elle-même un périmètre précis de test et autorise explicitement les chercheurs à intervenir dessus. En dehors de ce cadre, même sans intention malveillante, tester un système reste illégal en France.

## Fonctionnalités
- Détection d'accès en lecture publique sur un bucket
- Détection d'accès en écriture publique sur un bucket
- Génération d'un rapport structuré des résultats

## Architecture
- `Bucket_scanner.py` : classe BucketScanner, teste la lecture et l'écriture 
  publique sur un bucket S3 via requêtes HTTP directes
- `ReportWriter.py` : permet de générer le rapport de l'analyse des buckets
- `Severity.py` : Enum permet de savoir si le bucket est safe ou non
- `test_buckets.json` : liste des buckets à scanner (les URLs dans le fichier sont des exemples factices)

## Installation
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

## Utilisation
1. Copier test_buckets.json et adapter les URL des buckets avec les vôtres
2. python3 Bucket_scanner.py
3. Résultats dans rapport.jsonl

## Ce que j'ai appris
Ce projet m'a permis de mettre en pratique la notion de permissions cloud granulaires : j'ai découvert que lecture, écriture et listing sont trois permissions totalement indépendantes sur un bucket S3, ce qui explique en partie pourquoi les mauvaises configurations sont si fréquentes en entreprise. Ce projet m'a clarifié un point légal essentiel en sécurité offensive : l'autorisation doit toujours précéder le test, jamais le suivre — une distinction que je garde en tête pour toute future démarche de recherche de vulnérabilités. Enfin, j'ai appris à nettoyer l'historique Git avec `git filter-repo` lorsqu'une information a été envoyée par erreur sur GitHub. J'ai compris que supprimer une donnée dans un nouveau commit ne suffit pas, car Git conserve les anciennes versions. Il faut donc réécrire l'historique puis forcer la mise à jour du dépôt distant.
