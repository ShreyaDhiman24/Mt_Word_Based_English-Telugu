def combine_files(en_file, te_file, output_file):
    with open(en_file, 'r', encoding='utf-8') as en_f, \
         open(te_file, 'r', encoding='utf-8') as te_f, \
         open(output_file, 'w', encoding='utf-8') as out_f:
        for en_line, te_line in zip(en_f, te_f):
            en_line = en_line.strip()
            te_line = te_line.strip()
            out_f.write(f"{en_line}\t{te_line}\n")

if __name__ == '__main__':
    en_file = 'bleu/new_candidate.txt'  # English file
    te_file = 'bleu/new_reference.txt'  # Telugu file
    output_file = 'bleu/10_new_CandiReferenceAfterAUG.txt'  # Output file
    combine_files(en_file, te_file, output_file)