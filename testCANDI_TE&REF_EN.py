import torch
from torch.autograd import Variable
from utils import subsequent_mask
from setting import MAX_LENGTH, DEVICE
import numpy as np

def greedy_decode(model, src, src_mask, max_len, start_symbol):
    """
    Perform prediction on specified data using a trained model
    """
    memory = model.encode(src, src_mask)
    ys = torch.ones(1, 1).fill_(start_symbol).type_as(src.data)
    for i in range(max_len - 1):
        out = model.decode(memory,
                           src_mask,
                           Variable(ys),
                           Variable(subsequent_mask(ys.size(1)).type_as(src.data)))
        prob = model.generator(out[:, -1])
        _, next_word = torch.max(prob, dim=1)
        next_word = next_word.item()
        ys = torch.cat([ys, torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=1)
    return ys

def evaluate(data, model):
    """
    Perform prediction on data using a trained model and print the translation results.
    This version writes generated Telugu to the candidate file and English to the reference file.
    """
    with open('bleu/candidateTE1.txt', 'w', encoding='utf-8') as f_pred, \
         open('bleu/referenceEN1.txt', 'w', encoding='utf-8') as f_ref:
        
        with torch.no_grad():
            for i in range(len(data.train_en)):  # Iterate through training data
                # Original English sentence as the reference
                en_sent = " ".join([data.en_index_dict[w] for w in data.train_en[i]])
                print("\nEnglish: " + en_sent)

                # Actual Telugu reference sentence (used as a candidate after generation)
                te_sent = " ".join([data.te_index_dict[w] for w in data.train_te[i]])  
                print("Telugu Reference: " + te_sent)

                # Convert English sentence to tensor for model input
                src = torch.from_numpy(np.array(data.train_en[i])).long().to(DEVICE)
                src = src.unsqueeze(0)  # Add batch dimension
                src_mask = (src != 0).unsqueeze(-2)  # Create source mask
                
                # Generate Telugu sentence from model
                out = greedy_decode(model, src, src_mask, max_len=MAX_LENGTH, start_symbol=data.te_word_dict["BOS"])

                # Decode the generated sentence
                translation = []
                for j in range(1, out.size(1)):
                    sym = data.te_index_dict[out[0, j].item()]
                    if sym != 'EOS':  # Stop at EOS
                        translation.append(sym)
                    else:
                        break
                translation_sentence = " ".join(translation)
                print("Generated Telugu: %s" % translation_sentence)

                # Write the generated Telugu sentence to the candidate file (Telugu candidate)
                f_pred.write(translation_sentence + '\n')
                # Write the corresponding English sentence to the reference file (English reference)
                f_ref.write(en_sent + '\n')

def evaluate_test(data, model):
    evaluate(data, model)

if __name__ == '__main__':
    from setting import TRAIN_FILE, DEV_FILE, SAVE_FILE
    from train import model
    from data_pre import PrepareData

    model.load_state_dict(torch.load(SAVE_FILE, map_location=torch.device('cpu')))
    data = PrepareData(TRAIN_FILE, DEV_FILE)

    # Run evaluation on the training dataset
    evaluate_test(data, model)
