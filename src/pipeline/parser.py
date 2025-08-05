def normalize_title(title):
    """
    Convertit un titre en chaîne de caractères en minuscules
    pour faciliter la recherche insensible à la casse.
    """
    return str(title).lower()


def find_mentions(drugs_df, publications_df, title_col):
    """
    Recherche les mentions des médicaments dans les titres des publications.

    Args:
        drugs_df (DataFrame): Liste des médicaments avec colonnes 'drug' et 'atccode'.
        publications_df (DataFrame): Publications avec titres et métadonnées.
        title_col (str): Nom de la colonne contenant les titres dans publications_df.

    Returns:
        list: Liste de dictionnaires avec les mentions détectées.
    """
    mentions = []
    for _, pub in publications_df.iterrows():
        title = normalize_title(pub[title_col])
        for _, drug in drugs_df.iterrows():
            if drug["drug"].lower() in title:
                mentions.append(
                    {
                        "drug": drug["drug"],
                        "atccode": drug["atccode"],
                        "source": pub.get("source", "unknown"),
                        "journal": pub["journal"],
                        "date": pub["date"],
                        "publication_id": pub["id"],
                    }
                )
    return mentions
