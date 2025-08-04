# Servier Data Pipeline

Ce projet construit un graphe JSON associant des médicaments à leurs mentions dans les publications scientifiques issues de PubMed (CSV/JSON) et des essais cliniques.

---

## Structure du projet

```text
servier_data_pipeline/
├── data/                     # Données d'entrée (CSV/JSON) - non versionnées
├── output/                   # Résultats générés par le pipeline (JSON, CSV…)
├── src/
│   ├── pipeline/             # Code principal de traitement de données
│   │   ├── main.py           # Point d'entrée de l'exécution du pipeline
│   │   ├── config.py         # Chemins et constantes de configuration
│   │   ├── graph_builder.py  # Construction du graphe à partir des mentions
│   │   ├── loader.py         # Chargement des fichiers (CSV/JSON)
│   │   └── parser.py         # Détection des mentions de médicaments
│   └── ad_hoc/
│       └── journal_analyzer.py  # Analyses spécifiques (ex : journal le plus cité)
├── tests/                    # Tests unitaires
│   └── test_graph_builder.py # Test du module graph_builder (avec unittest ou pytest)
├── README.md                 # Documentation du projet
├── pyproject.toml            # Définition du projet et des dépendances (géré par Poetry)
└── requirements.txt          # (Optionnel) pour compatibilité pip

```

---

## Prérequis

- Python ≥ 3.10
- [Poetry](https://python-poetry.org/) (si utilisé)
- Accès à des fichiers de données dans le dossier `data/`

---

## Installation

### Option 1 - Avec [Poetry](https://python-poetry.org/) (recommandé)

Poetry permet de gérer les dépendances, les environnements virtuels et les scripts.

```bash
# 1. Installer Poetry si besoin
curl -sSL https://install.python-poetry.org | python3 -

# 2. Cloner le dépôt et entrer dans le dossier
git clone <url>
cd servier_data_pipeline

# 3. Installer les dépendances
poetry install
```

Pour activer l’environnement virtuel Poetry :

```bash
poetry shell
```

---

### Option 2 - Avec `pip` et `requirements.txt`

```bash
# Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows

# Installer les dépendances
pip install -r requirements.txt
```

---

## Exécution

Dans la racine du projet :

Avec Poetry :

```bash
poetry run python -m src.pipeline.main
```

Sans Poetry :

```bash
python -m src.pipeline.main
```

---

## Lancer les tests

Avec `unittest` :
```bash
poetry run python -m unittest discover tests/
```

Ou:
```bash
python -m unittest discover -s tests
```

Avec `pytest` :

```bash
poetry run pytest
```

Ou:
```bash
pytest
```
---

Fichier de sortie : drug_mentions.json :
```json
{
  "DIPHENHYDRAMINE": {
    "mentions": [
      {
        "source": "pubmed.csv",
        "journal": "Journal of emergency nursing",
        "date": "01/01/2019",
        "publication_id": 1
      },
      {
        "source": "pubmed.csv",
        "journal": "Journal of emergency nursing",
        "date": "01/01/2019",
        "publication_id": 2
      },
      {
        "source": "pubmed.csv",
        "journal": "The Journal of pediatrics",
        "date": "02/01/2019",
        "publication_id": 3
      },
      {
        "source": "clinical_trials",
        "journal": "Journal of emergency nursing",
        "date": "1 January 2020",
        "publication_id": "NCT01967433"
      },
      {
        "source": "clinical_trials",
        "journal": "Journal of emergency nursing",
        "date": "1 January 2020",
        "publication_id": "NCT04189588"
      },
      {
        "source": "clinical_trials",
        "journal": "Journal of emergency nursing",
        "date": "1 January 2020",
        "publication_id": "NCT04237091"
      }
    ]
  },
  "TETRACYCLINE": {
    "mentions": [
      {
        "source": "pubmed.csv",
        "journal": "Journal of food protection",
        "date": "01/01/2020",
        "publication_id": 4
      },
      {
        "source": "pubmed.csv",
        "journal": "American journal of veterinary research",
        "date": "02/01/2020",
        "publication_id": 5
      },
      {
        "source": "pubmed.csv",
        "journal": "Psychopharmacology",
        "date": "2020-01-01",
        "publication_id": 6
      }
    ]
  },
  "ETHANOL": {
    "mentions": [
      {
        "source": "pubmed.csv",
        "journal": "Psychopharmacology",
        "date": "2020-01-01",
        "publication_id": 6
      }
    ]
  },
  "EPINEPHRINE": {
    "mentions": [
      {
        "source": "pubmed.csv",
        "journal": "The journal of allergy and clinical immunology. In practice",
        "date": "01/02/2020",
        "publication_id": 7
      },
      {
        "source": "pubmed.csv",
        "journal": "The journal of allergy and clinical immunology. In practice",
        "date": "01/03/2020",
        "publication_id": 8
      },
      {
        "source": "clinical_trials",
        "journal": "Journal of emergency nursing\\xc3\\x28",
        "date": "27 April 2020",
        "publication_id": "NCT04188184"
      }
    ]
  },
  "ISOPRENALINE": {
    "mentions": [
      {
        "source": "pubmed.json",
        "journal": "Journal of photochemistry and photobiology. B, Biology",
        "date": "01/01/2020",
        "publication_id": 9
      }
    ]
  },
  "BETAMETHASONE": {
    "mentions": [
      {
        "source": "pubmed.json",
        "journal": "The journal of maternal-fetal & neonatal medicine",
        "date": "01/01/2020",
        "publication_id": 10
      },
      {
        "source": "pubmed.json",
        "journal": "Journal of back and musculoskeletal rehabilitation",
        "date": "01/01/2020",
        "publication_id": 11
      },
      {
        "source": "pubmed.json",
        "journal": "The journal of maternal-fetal & neonatal medicine",
        "date": "01/03/2020",
        "publication_id": ""
      },
      {
        "source": "clinical_trials",
        "journal": "H\u00f4pitaux Universitaires de Gen\u00e8ve",
        "date": "1 January 2020",
        "publication_id": "NCT04153396"
      }
    ]
  },
  "ATROPINE": {
    "mentions": [
      {
        "source": "pubmed.json",
        "journal": "The journal of maternal-fetal & neonatal medicine",
        "date": "01/03/2020",
        "publication_id": ""
      }
    ]
  }
}
```

## Bonnes pratiques et choix de conception

- **Séparation claire du code** :
  - Le code source est placé dans le dossier `src/` pour éviter les conflits avec les tests ou scripts.
  - `src/pipeline/` contient la logique principale de transformation des données.
  - `src/ad_hoc/` regroupe des analyses spécifiques, ponctuelles ou exploratoires.

- **Tests unitaires** :
  - Tous les modules critiques sont couverts par des tests dans le dossier `tests/`.
  - Utilisation possible de `pytest` ou `unittest` pour plus de flexibilité.

- **Utilisation de Poetry** :
  - Pour la gestion des dépendances, l’isolation de l’environnement, et la portabilité du projet.
  - Tous les scripts peuvent être lancés via `poetry run`.

- **Respect du principe KISS (Keep It Simple)** :
  - Le projet est conçu pour rester simple à comprendre et à modifier.
  - Peu de dépendances externes pour faciliter la prise en main.

- **Structuration des données en sortie** :
  - Résultats produits stockés dans `output/`, de préférence en formats standard (CSV, JSON).

- **Nomination explicite des fonctions et variables** :
  - Le code est commenté de façon concise mais claire.
  - Les noms sont choisis pour refléter la logique métier plutôt que les détails techniques.

- **Configuration centralisée** *(si applicable)* :
  - Paramètres configurables centralisés dans un fichier ou module dédié (ex: `config.py` ou `.env`).