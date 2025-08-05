import pandas as pd
import json


def load_drugs(path):
    """Charge le fichier CSV des médicaments en DataFrame pandas."""
    return pd.read_csv(path)


def load_pubmed_csv(path):
    """Charge le fichier CSV PubMed en DataFrame pandas."""
    return pd.read_csv(path)


def load_pubmed_json(path):
    """
    Charge un fichier JSON PubMed.
    Convertit le champ 'id' en int quand c'est possible, sinon laisse tel quel.
    Si 'id' est vide ou None, le remplace par None.
    """
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for entry in data:
        id_value = entry.get("id")
        if id_value == "" or id_value is None:
            entry["id"] = None
        else:
            try:
                entry["id"] = int(id_value)
            except (ValueError, TypeError):
                pass
    return data


def load_clinical_trials(path):
    """Charge le fichier CSV des essais cliniques en DataFrame pandas."""
    return pd.read_csv(path)
