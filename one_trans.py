"""
Created by tz on 2020/11/12 
"""

__author__ = 'tz'

from nltk import word_tokenize
from utils import get_word_dict, subsequent_mask
import torch
import numpy as np
from torch.autograd import Variable
from setting import SAVE_FILE, DEVICE, LAYERS, D_MODEL, D_FF, DROPOUT, H_NUM, TGT_VOCAB, SRC_VOCAB


"""
Single sentence input, single sentence translation output
"""

# from train import model  # You can directly import the initialized model from train, or initialize it as shown below
# Initialize the model
def init_model():
    from setting import LAYERS, D_MODEL, D_FF, DROPOUT, H_NUM, TGT_VOCAB, SRC_VOCAB
    from model import make_model
    # Initialize the model
    model = make_model(
        SRC_VOCAB,  # Source vocabulary size
        TGT_VOCAB,  # Target vocabulary size
        LAYERS,     # Number of layers
        D_MODEL,    # Embedding dimension
        D_FF,       # Feed-forward dimension
        H_NUM,      # Number of attention heads
        DROPOUT     # Dropout rate
    )
    return model

model = init_model()

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
pu_idx2word, pu_word2idx, en_idx2word, en_word2idx = get_word_dict()

# Load the trained model's state
model.load_state_dict(torch.load(SAVE_FILE, map_location=torch.device('cpu')))


def sentence2id(sentence):
    """
    Convert a sentence into a list of word IDs.
    Test example:
    # >>> print(sentence2id('I am a boy'))
    [['2', '5', '90', '9', '192', '3']]
    :param sentence: An English sentence
    :return: A nested list where each word in the sentence is represented by an ID
    """
    en = []
    en.append(['BOS'] + word_tokenize(sentence.lower()) + ['EOS'])

    sentence_id = [[int(en_word2idx.get(w, 0)) for w in e] for e in en]
    return sentence_id

def src_handle(X):
    """
    Convert a list of sentence IDs into a tensor and generate the input mask matrix.
    :param X: List of word IDs
    :return: The tensor of word IDs and the corresponding input mask
    """
    src = torch.from_numpy(np.array(X)).long().to(DEVICE)
    src_mask = (src != 0).unsqueeze(-2)
    return src, src_mask

def greedy_decode(model, src, src_mask, max_len, start_symbol):
    """
    Pass a trained model to predict the output for given data.
    """
    # First, use the encoder to encode the input
    memory = model.encode(src, src_mask)
    # Initialize the prediction with a 1×1 tensor containing the start symbol ('BOS') ID,
    # and set the type to match the input data type (LongTensor)
    ys = torch.ones(1, 1).fill_(start_symbol).type_as(src.data)
    # Iterate over the output length indices
    for i in range(max_len - 1):
        # Decode to get the hidden representation
        out = model.decode(memory,
                           src_mask,
                           Variable(ys),
                           Variable(subsequent_mask(ys.size(1)).type_as(src.data)))
        # Convert the hidden representation into a log_softmax probability distribution over the vocabulary
        prob = model.generator(out[:, -1])
        # Get the ID of the word with the highest probability at the current position
        _, next_word = torch.max(prob, dim=1)
        next_word = next_word.data[0]
        # Append the predicted word ID to the previously predicted content
        ys = torch.cat([ys,
                        torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=1)
    return ys

def output(out):
    translation = []
    # Iterate over the output word indices (note: the start symbol "BOS" at index 0 is not included)
    for j in range(1, out.size(1)):  # Generated maximum sequence length
        # Get the output word at the current index
        sym = pu_idx2word[out[0, j].item()]
        # If the output word is not the end-of-sequence ('EOS') token, add it to the translation list
        if sym != 'EOS':
            translation.append(sym)
        else:
            break
    # Print the translated sentence
    print("translation: %s" % " ".join(translation))
    return ''.join(translation)

def machine_translate(sentence):
    """
    Perform machine translation.
    :param sentence: Input a sentence
    :return: Output the machine-translated result
    """
    src, src_mask = src_handle(sentence2id(sentence))
    out = greedy_decode(model, src, src_mask, max_len=50, start_symbol=int(pu_word2idx.get('BOS')))
    pu_result = output(out)
    return pu_result
