# veille-IA-CR-auto

## description

Veille sur l’intelligence artificielle appliquée aux comptes rendus automatiques.

### Sites visités

- [Aixploria - Catégories AI](https://www.aixploria.com/categories-ai/)

### Installation

1. Créez un environnement virtuel (venv).
2. Installez les dépendances à partir du fichier `requirements.txt`.
3. Exécutez le script pour générer la base de données :
```bash
python ./src/create_db.py
```

## lignes de commande

### Commandes occasionnelles

Pour collecter des catégories depuis Aixploria et les sauvegarder dans un fichier JSON :
```bash
scrapy crawl info_aixplora -O output/categories.json --set LOG_LEVEL=WARNING --logfile=output/scrapy.log
```

### Exécution principale

Pour collecter des outils IA tout en réduisant la verbosité des logs et en enregistrant les logs dans un fichier :
```bash
scrapy crawl ai_tools --set LOG_LEVEL=WARNING --logfile=scrapy.log
```

Nettoyage - suppression des doublons avec concaténation des données informatives :
```bash
python ./src/ai_tools_concat.py
```

Pour récupérer les URL finales :
```bash
python ./src/get_final_url.py
```