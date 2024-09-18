from nltk.translate.bleu_score import sentence_bleu

def filter_sentences(input_file, output_file, removed_file, threshold=55):
    """
    Filters out lines where the BLEU score between the candidate
    and reference sentences is less than the threshold.
    
    :param input_file: Path to the input file containing the three-part sentences.
    :param output_file: Path to the file where accepted sentences will be saved.
    :param removed_file: Path to the file where removed sentences will be saved.
    :param threshold: BLEU score threshold for filtering (default is 50).
    """
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8') as outfile, \
         open(removed_file, 'w', encoding='utf-8') as removed:
        
        # Iterate through each line in the input file
        for line in infile:
            # Split the line into candidate, reference, and English parts
            parts = line.strip().split('   ')
            if len(parts) != 3:
                # If the line doesn't have exactly three parts, skip it
                continue

            candidate = parts[0].strip().split(' ')  # First part (Urdu candidate)
            reference = [parts[1].strip().split(' ')]  # Second part (Urdu reference)
            english = parts[2].strip()  # Third part (English)

            # Calculate the BLEU score between candidate and reference
            bleu_score = sentence_bleu(reference, candidate) * 100

            if bleu_score >= threshold:
                # If BLEU score is >= threshold, keep the line in the output file
                outfile.write(line)
            else:
                # If BLEU score is < threshold, save the removed line in the removed file
                removed.write(line)

# Example usage
input_file = 'bleu/combined_for_weighted.txt'
output_file = 'bleu/accepted_sentences.txt'
removed_file = 'bleu/removed_sentences.txt'

filter_sentences(input_file, output_file, removed_file)
