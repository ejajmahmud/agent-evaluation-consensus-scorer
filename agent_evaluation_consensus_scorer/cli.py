"""CLI for Agent Evaluation Consensus Scorer."""
import argparse
from .core import ConsensusScorer

def main():
    parser = argparse.ArgumentParser(description="Agent Evaluation Consensus Scorer CLI")
    parser.add_argument("--demo", action="store_true", help="Run consensus scoring demo")
    args = parser.parse_args()

    scores = [85.0, 88.0, 86.0, 20.0] # 20.0 is an outlier
    res = ConsensusScorer.aggregate_scores(scores)
    print("Judge Scores:", scores)
    print(f"Consensus Score: {res.consensus_score}")
    print(f"Outliers Discarded: {res.outlier_scores}")
    print(f"Agreement Ratio: {res.agreement_ratio * 100:.1f}%")

if __name__ == "__main__":
    main()
