def most_mentions_by_journal(graph):
    """
    Retourne le journal qui mentionne le plus de médicaments distincts dans le graphe.

    Args:
        graph (dict): dictionnaire des médicaments avec leurs mentions.

    Returns:
        tuple: (nom du journal, set des médicaments mentionnés)
    """

    journal_drugs = {}

    for drug, data in graph.items():
        for mention in data["mentions"]:
            journal = mention["journal"]
            journal_drugs.setdefault(journal, set()).add(drug)

    return max(journal_drugs.items(), key=lambda x: len(x[1]))