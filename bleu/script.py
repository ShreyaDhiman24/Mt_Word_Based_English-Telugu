def remove_empty_lines(candidate_file, reference_file, cleaned_candidate_file, cleaned_reference_file):
    """
    Remove lines where either candidate or reference file has an empty line.
    The corresponding lines from both files are removed.
    """
    # Read all lines from candidate and reference files
    with open(candidate_file, 'r', encoding='utf-8') as f_candidate, open(reference_file, 'r', encoding='utf-8') as f_reference:
        candidate_lines = f_candidate.readlines()
        reference_lines = f_reference.readlines()

    # Ensure both files have the same number of lines
    if len(candidate_lines) != len(reference_lines):
        print("The number of lines in candidate and reference files don't match.")
        return

    cleaned_candidate_lines = []
    cleaned_reference_lines = []

    # Loop through both files and keep only lines that are non-empty in both
    for cand_line, ref_line in zip(candidate_lines, reference_lines):
        if cand_line.strip() and ref_line.strip():  # Only keep lines that are non-empty in both files
            cleaned_candidate_lines.append(cand_line)
            cleaned_reference_lines.append(ref_line)

    # Write cleaned lines back to new files
    with open(cleaned_candidate_file, 'w', encoding='utf-8') as f_cleaned_candidate, open(cleaned_reference_file, 'w', encoding='utf-8') as f_cleaned_reference:
        f_cleaned_candidate.writelines(cleaned_candidate_lines)
        f_cleaned_reference.writelines(cleaned_reference_lines)

    print(f"Cleaned files written to {cleaned_candidate_file} and {cleaned_reference_file}")

# Example usage:
candidate_file = 'bleu/candidate.txt'
reference_file = 'bleu/reference.txt'
cleaned_candidate_file = 'bleu/cleaned_candidate.txt'
cleaned_reference_file = 'bleu/cleaned_reference.txt'

remove_empty_lines(candidate_file, reference_file, cleaned_candidate_file, cleaned_reference_file)
