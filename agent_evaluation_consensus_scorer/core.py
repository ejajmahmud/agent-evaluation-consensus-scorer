"""Core Agent Evaluation Consensus Scorer implementation."""
from typing import List, Dict, Any

class ConsensusResult:
    def __init__(self, consensus_score: float, kept_scores: List[float], outlier_scores: List[float], agreement_ratio: float):
        self.consensus_score = consensus_score
        self.kept_scores = kept_scores
        self.outlier_scores = outlier_scores
        self.agreement_ratio = agreement_ratio

class ConsensusScorer:
    @staticmethod
    def aggregate_scores(judge_scores: List[float], outlier_distance_threshold: float = 25.0) -> ConsensusResult:
        if not judge_scores:
            return ConsensusResult(0.0, [], [], 0.0)

        mean_raw = sum(judge_scores) / len(judge_scores)
        kept = []
        outliers = []

        for s in judge_scores:
            if abs(s - mean_raw) > outlier_distance_threshold and len(judge_scores) > 2:
                outliers.append(s)
            else:
                kept.append(s)

        final_score = round(sum(kept) / len(kept), 2) if kept else mean_raw
        agreement = round(len(kept) / len(judge_scores), 4)

        return ConsensusResult(final_score, kept, outliers, agreement)
