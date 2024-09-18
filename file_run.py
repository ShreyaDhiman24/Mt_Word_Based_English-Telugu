from ribes import RIBES

# Load your candidate and reference files
candidate_file = 'bleu/candidate.txt'
reference_file = 'bleu/reference.txt'

# Read the files
with open(candidate_file, 'r') as f:
    candidate = f.read().splitlines()

with open(reference_file, 'r') as f:
    reference = f.read().splitlines()

# Initialize RIBES scorer
ribes_scorer = RIBES()

# Calculate RIBES score
ribes_score = ribes_scorer.score(candidate, reference)

print(f'RIBES score: {ribes_score:.4f}')
