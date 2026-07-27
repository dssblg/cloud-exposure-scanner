# cloud-exposure-scanner

## À propos
L'outil créé ici a pour but de vérifier la sécurité de ses propres buckets AWS. En effet, une mauvaise configuration, même minime, peut faire sauter la sécurité existante et c'est exactement ce qu'attendent les attaquants : une petite faille, et des données transmises on ne sait où, on ne sait à qui.

En 2025, un bucket cloud mal configuré a exposé des millions de dossiers de patients chez un prestataire de santé américain, un rappel que ce type d'erreur, en apparence anodine, peut avoir des conséquences massives. J'ai décidé de créer cet outil car le cloud est un élément essentiel pour les entreprises comme pour les particuliers, et ce sujet s'inscrit directement dans mon cursus de Master Cybersécurité du Cloud à l'Edge.

## Cadre légal
L'utilisation de cet outil se fera uniquement sur mes propres buckets. Il est interdit de l'utiliser sur des buckets autres que les siens, même s'ils ne sont pas sécurisés.

Cette règle n'est pas qu'une formalité légale : en sécurité offensive, ce qui différencie un audit légitime d'une intrusion n'est pas l'action technique réalisée, mais l'autorisation préalable du propriétaire du système. Scanner un système sans cette autorisation reste illégal, même si la faille trouvée est réelle et même bien intentionnée.

Pour tester la sécurité de systèmes qui ne m'appartiennent pas, la voie légale existe : elle passe par des programmes de bug bounty, où l'entreprise définit elle-même un périmètre précis de test et autorise explicitement les chercheurs à intervenir dessus. En dehors de ce cadre, même sans intention malveillante, tester un système reste illégal en France.

## Fonctionnalités
- Détection d'accès en lecture publique sur un bucket
- Détection d'accès en écriture publique sur un bucket
- Génération d'un rapport structuré des résultats

## Architecture
// TODO

## Installation
// TODO

## Utilisation
// TODO

## Ce que j'ai appris
// TODO

## Roadmap
Après avoir testé sur AWS, je continuerai de développer pour tester sur Azure, GCP...
