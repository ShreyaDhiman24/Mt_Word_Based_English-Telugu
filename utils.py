import numpy as np
import torch

def seq_padding(X, padding=0):
    """
    Pads a batch of sequences (represented by word IDs) to align their lengths.
    :param X: List of sequences, where each sequence is a list of word IDs.
    :param padding: The ID used for padding (default is 0).
    :return: A numpy array with all sequences padded to the same length.
    """
    # Calculate the length of each sequence in the batch
    L = [len(x) for x in X]
    # Find the maximum sequence length in the batch
    ML = max(L)
    # For each sequence in X, pad with the padding ID if its length is less than the maximum length
    # (By default, padding ID is 0, which is equivalent to using <UNK> for padding)
    return np.array([
        np.concatenate([x, [padding] * (ML - len(x))]) if len(x) < ML else x for x in X
    ])


def subsequent_mask(size):
    """
    Creates a mask matrix for self-attention in the decoder layer.
    :param size: The dimension of the sequence.
    :return: A mask matrix where the upper right (excluding the diagonal) is all False, and the lower left is all True.
    """
    # Define the shape of the subsequent_mask matrix
    attn_shape = (1, size, size)
    # Generate a subsequent_mask matrix where the upper right (excluding the main diagonal) is all 1,
    # and the lower left (including the main diagonal) is all 0
    subsequent_mask = np.triu(np.ones(attn_shape), k=1).astype('uint8')

    # Return a subsequent_mask matrix where the upper right (excluding the main diagonal) is all False,
    # and the lower left (including the main diagonal) is all True
    return torch.from_numpy(subsequent_mask) == 0


def get_word_dict():
    """
    Retrieves the Chinese-English word2idx and idx2word dictionaries.
    :return: The dictionaries.
    """
    import csv
    pu_idx2word = {}  # Dictionary mapping from index to word (Chinese)
    pu_word2idx = {}  # Dictionary mapping from word to index (Chinese)
    en_idx2word = {}  # Dictionary mapping from index to word (English)
    en_word2idx = {}  # Dictionary mapping from word to index (English)
    
    # Load the Chinese word index dictionary
    with open("data/word_name_dict/pu_index_dict.csv", 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        for l in data:
            pu_idx2word[int(l[0])] = l[1]
            pu_word2idx[l[1]] = int(l[0])

    # Load the English word index dictionary
    with open("data/word_name_dict/en_index_dict.csv", 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        for l in data:
            en_idx2word[int(l[0])] = l[1]
            en_word2idx[l[1]] = int(l[0])

    return pu_idx2word, pu_word2idx, en_idx2word, en_word2idx


def bleu_candidate(sentence):
    """
    Saves the predicted translation results to a file.
    :param sentence: The candidate translation sentence to save.
    """
    from setting import BLEU_CANDIDATE
    with open(BLEU_CANDIDATE, 'a+', encoding='utf-8') as f:
        f.write(sentence + '\n')


def bleu_references(read_filename, save_filename):
    """
    Saves reference translations to a file (in Chinese, without space segmentation in the file).
    :param read_filename: The input file containing reference translations.
    :param save_filename: The output file to save the formatted reference translations.
    """
    writer = open(save_filename, 'a+', encoding='utf-8')
    with open(read_filename, 'r', encoding="utf-8") as f_read:
        for line in f_read:
            line = line.strip().split('\t')
            sentence_tap = " ".join([w for w in line[1]])
            writer.write(sentence_tap + '\n')
    writer.close()
    print('Writing successful')


if __name__ == '__main__':
    read_filename = 'data/dev.txt'
    save_filename = 'data/bleu/references.txt'

    bleu_references(read_filename, save_filename)
