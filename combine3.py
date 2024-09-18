def combine_sentences(file1, file2, file3, output_file):
    """
    Combine lines from three text files with three tab spaces in between and write to an output file.
    """
    with open(file1, 'r', encoding='utf-8') as f1, \
         open(file2, 'r', encoding='utf-8') as f2, \
         open(file3, 'r', encoding='utf-8') as f3, \
         open(output_file, 'w', encoding='utf-8') as out:

        # Iterate over lines from the three files simultaneously
        for line1, line2, line3 in zip(f1, f2, f3):
            # Remove any leading/trailing whitespace and combine with three tab spaces
            combined_line = f"{line1.strip()}   {line2.strip()}   {line3.strip()}\n"
            # Write the combined line to the output file
            out.write(combined_line)

# Example usage
combine_sentences('bleu/candidate.txt', 'bleu/reference.txt', 'bleu/referenceEN1.txt', 'bleu/combined_for_weighted.txt')
