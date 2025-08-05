import pandas as pd

from src.pipeline import loader, parser, graph_builder, config
from src.ad_hoc import journal_analyzer
import json


def run_pipeline():
    """
    Exécute le pipeline complet :
    - Chargement des données (médicaments, publications PubMed CSV/JSON, essais cliniques)
    - Fusion des publications en un seul DataFrame
    - Extraction des mentions de médicaments dans les titres
    - Construction du graphe associant médicaments et mentions
    - Sauvegarde du graphe au format JSON
    - Analyse ad-hoc des journaux les plus mentionnés
    """
    drugs = loader.load_drugs(config.DRUGS_PATH)

    pubmed_csv = loader.load_pubmed_csv(config.PUBMED_CSV_PATH)
    pubmed_csv["source"] = "pubmed.csv"

    pubmed_json = loader.load_pubmed_json(config.PUBMED_JSON_PATH)
    for entry in pubmed_json:
        entry["source"] = "pubmed.json"
    pubmed_json_df = pd.DataFrame(pubmed_json)

    clinical = loader.load_clinical_trials(config.CLINICAL_TRIALS_PATH)
    clinical.rename(columns={"scientific_title": "title"}, inplace=True)
    clinical["source"] = "clinical_trials"

    all_pubs = pd.concat([pubmed_csv, pubmed_json_df, clinical], ignore_index=True)

    mentions = parser.find_mentions(drugs, all_pubs, title_col="title")
    graph = graph_builder.build_graph(mentions)

    with open(config.OUTPUT_PATH, "w") as f:
        json.dump(graph, f, indent=2)

    journal, drugs = journal_analyzer.most_mentions_by_journal(graph)


if __name__ == "__main__":
    run_pipeline()
