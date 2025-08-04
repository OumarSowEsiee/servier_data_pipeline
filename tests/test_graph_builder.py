from src.pipeline.graph_builder import build_graph
import unittest

class testGraphBuilder(unittest.TestCase):
    """Tests pour la fonction build_graph du module graph_builder."""

    def test_single_mention(self):
        """Vérifie la construction correcte du graphe avec une seule mention."""
        mentions = [
            {
                "drug": "Aspirin",
                "journal": "Lancet",
                "date": "2020-01-01",
                "source": "pubmed_csv",
                "publication_id": 1
            }
        ]
        graph = build_graph(mentions)

        self.assertIn("Aspirin", graph)
        self.assertEqual(len(graph["Aspirin"]["mentions"]), 1)
        self.assertEqual(graph["Aspirin"]["mentions"][0]["journal"], "Lancet")

if __name__ == "__main__":
    unittest.main()