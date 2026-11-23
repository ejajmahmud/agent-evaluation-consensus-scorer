"""Tests for ConsensusScorer."""
import unittest
from agent_evaluation_consensus_scorer.core import ConsensusScorer

class TestConsensusScorer(unittest.TestCase):
    def test_consensus_aggregation(self):
        res = ConsensusScorer.aggregate_scores([80.0, 82.0, 81.0, 10.0])
        self.assertIn(10.0, res.outlier_scores)
        self.assertEqual(len(res.kept_scores), 3)
        self.assertAlmostEqual(res.consensus_score, 81.0, delta=0.5)
