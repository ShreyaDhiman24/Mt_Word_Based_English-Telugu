from rouge import Rouge
import codecs
from statistics import mean

def read_sentences(file_path):
    with codecs.open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def calculate_rouge_scores(hypothesis, reference):
    rouge = Rouge()
    scores = rouge.get_scores(hypothesis, reference)
    return scores[0]

def main():
    from setting import BLEU_REFERENCES, BLEU_CANDIDATE
    hypotheses = read_sentences(BLEU_CANDIDATE)
    references = read_sentences(BLEU_REFERENCES)

    if len(hypotheses) != len(references):
        print("Error: The number of sentences in the files do not match.")
        return

    all_scores = []

    for i, (hyp, ref) in enumerate(zip(hypotheses, references)):
        hyp = hyp.strip()
        ref = ref.strip()
        
        if not hyp or not ref:
            print(f"Skipping sentence pair {i+1} due to empty hypothesis or reference.")
            continue
        
        scores = calculate_rouge_scores(hyp, ref)
        all_scores.append(scores)
        
        print(f"Sentence pair {i+1}:")
        print(f"Hypothesis: {hyp}")
        print(f"Reference: {ref}")
        print(f"ROUGE-1 F1: {scores['rouge-1']['f']:.4f}")
        print(f"ROUGE-2 F1: {scores['rouge-2']['f']:.4f}")
        print(f"ROUGE-L F1: {scores['rouge-l']['f']:.4f}")
        print()

    # Calculate average ROUGE scores
    if all_scores:
        avg_rouge_1 = mean(score['rouge-1']['f'] for score in all_scores)
        avg_rouge_2 = mean(score['rouge-2']['f'] for score in all_scores)
        avg_rouge_l = mean(score['rouge-l']['f'] for score in all_scores)

        print("Average ROUGE Scores:")
        print(f"ROUGE-1 F1: {avg_rouge_1:.4f}")
        print(f"ROUGE-2 F1: {avg_rouge_2:.4f}")
        print(f"ROUGE-L F1: {avg_rouge_l:.4f}")
    else:
        print("No valid sentence pairs to calculate ROUGE scores.")

if __name__ == "__main__":
    main()


# from rouge import Rouge
# import codecs
# from statistics import mean

# def read_sentences(file_path):
#     with codecs.open(file_path, 'r', encoding='utf-8') as file:
#         return file.readlines()

# def calculate_rouge_scores(hypothesis, reference):
#     rouge = Rouge()
#     scores = rouge.get_scores(hypothesis, reference)
#     return scores[0]

# def main():
#     hypotheses = read_sentences('bleu/candidate.txt')
#     references = read_sentences('bleu/reference.txt')

#     if len(hypotheses) != len(references):
#         print("Error: The number of sentences in the files do not match.")
#         return

#     all_scores = []

#     for i, (hyp, ref) in enumerate(zip(hypotheses, references)):
#         hyp = hyp.strip()
#         ref = ref.strip()
        
#         scores = calculate_rouge_scores(hyp, ref)
#         all_scores.append(scores)
        
#         print(f"Sentence pair {i+1}:")
#         print(f"Hypothesis: {hyp}")
#         print(f"Reference: {ref}")
#         print(f"ROUGE-1 F1: {scores['rouge-1']['f']:.4f}")
#         print(f"ROUGE-2 F1: {scores['rouge-2']['f']:.4f}")
#         print(f"ROUGE-L F1: {scores['rouge-l']['f']:.4f}")
#         print()

#     # Calculate average ROUGE scores
#     avg_rouge_1 = mean(score['rouge-1']['f'] for score in all_scores)
#     avg_rouge_2 = mean(score['rouge-2']['f'] for score in all_scores)
#     avg_rouge_l = mean(score['rouge-l']['f'] for score in all_scores)

#     print("Average ROUGE Scores:")
#     print(f"ROUGE-1 F1: {avg_rouge_1:.4f}")
#     print(f"ROUGE-2 F1: {avg_rouge_2:.4f}")
#     print(f"ROUGE-L F1: {avg_rouge_l:.4f}")

# if __name__ == "__main__":
#     main()
    


# Average ROUGE Scores:
# ROUGE-1 F1: 0.6654
# ROUGE-2 F1: 0.5405
# ROUGE-L F1: 0.6538


# BLEU Score for 1,0.2,0,0 weitage is
# 44.19202628256681
# BLEU Score for 1,0.5,0.2,0.1 weitage is
# 24.24187796037474
# BLEU Score for 1,0.2,0.2,0.2 weitage is
# 28.051858664166602
# BLEU Score for 0.8,0.5,0.3,0 weitage is
# 27.967394668124136
# BLEU Score for 1:1:0:0 weitage is
# 21.6702187993598
# BLEU Score for 1:1:1:0 weitage is
# 7.5084524747394905
# BLEU Score for 1:1:1:1 weitage is
# 2.23332501728021
# BLEU Score for 1:0:0:0 weitage is
# 52.809744935729185
# BLEU Score for 0,1,0,0 weitage is
# 41.03450760031698
# BLEU Score for 0,0,1,0 weitage is
# 34.64871556793562
# BLEU Score for 0,0,0,1 weitage is
# 29.744145345445457



# after backtranslation

# BLEU Score for 1,0.2,0,0 weitage is
# 45.85537823378769
# BLEU Score for 1,0.5,0.2,0.1 weitage is
# 25.879148514173504
# BLEU Score for 1,0.2,0.2,0.2 weitage is
# 29.762817845689206
# BLEU Score for 0.8,0.5,0.3,0 weitage is
# 29.6679453345616
# BLEU Score for 1:1:0:0 weitage is
# 23.216017750794972
# BLEU Score for 1:1:1:0 weitage is
# 8.48155528699247
# BLEU Score for 1:1:1:1 weitage is
# 2.67427804517377
# BLEU Score for 1:0:0:0 weitage is
# 54.36143572621035
# BLEU Score for 0,1,0,0 weitage is
# 42.70677814272917
# BLEU Score for 0,0,1,0 weitage is
# 36.53320469528863
# BLEU Score for 0,0,0,1 weitage is
# 31.530514801632087


# Average ROUGE Scores:
# ROUGE-1 F1: 0.6654
# ROUGE-2 F1: 0.5405
# ROUGE-L F1: 0.6538