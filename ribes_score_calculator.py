import sys
import datetime
from ribes_score_script import Corpus, RIBESevaluator  # Make sure to replace 'your_script' with the actual name of your script file
from ribes_score_script import kendall  # Import the kendall function if it's in a separate module

# Function to evaluate RIBES score
def evaluate_ribes(reference_file, hypothesis_file, alpha=0.25, beta=0.10, case=False, emptyref=False):
    # Initialize the RIBESevaluator
    evaluator = RIBESevaluator(sent=False, alpha=alpha, beta=beta, output=sys.stdout)

    # Create Corpus instances for the reference and hypothesis files
    ref_corpus = Corpus(reference_file, case=case)
    hyp_corpus = Corpus(hypothesis_file, case=case)

    # Evaluate the RIBES score
    try:
        # Pass the hypothesis and reference corpora to the evaluator
        best_ribes = evaluator.eval(hyp_corpus, [ref_corpus], emptyref=emptyref)
        print(f"RIBES score: {best_ribes:.6f} (alpha={alpha}, beta={beta})")
    except Exception as e:
        print(f"Error during evaluation: {e}", file=sys.stderr)

# Define file paths
reference_file = 'bleu/cleaned_reference.txt'
hypothesis_file =  'bleu/cleaned_candidate.txt'

# Call the evaluation function
evaluate_ribes(reference_file, hypothesis_file, alpha=0.25, beta=0.10, case=False, emptyref=False)
