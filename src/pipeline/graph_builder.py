from collections import defaultdict


def build_graph(mentions):
    """
    Construit un graphe associant chaque médicament à ses mentions.
    Chaque médicament est une clé avec une liste de mentions comme valeur.
    """
    graph = defaultdict(lambda: {"mentions": []})
    for mention in mentions:
        graph[mention["drug"]]["mentions"].append(
            {
                "source": mention["source"],
                "journal": mention["journal"],
                "date": mention["date"],
                "publication_id": mention["publication_id"],
            }
        )
    return graph
