#test.py

import torch
from torch.autograd import Variable
from utils import subsequent_mask
from setting import MAX_LENGTH, DEVICE
import numpy as np
from utils import bleu_candidate

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
        next_word = next_word.data[0]
        ys = torch.cat([ys, torch.ones(1, 1).type_as(src.data).fill_(next_word)], dim=1)
    return ys

def evaluate(data, model):
    """
    Perform prediction on data using a trained model and print the translation results
    """
    with open('bleu/candidate.txt', 'w', encoding='utf-8') as f_pred, open('bleu/reference.txt', 'w', encoding='utf-8') as f_ref:
        with torch.no_grad():
            for i in range(len(data.dev_en)):
                en_sent = " ".join([data.en_index_dict[w] for w in data.dev_en[i]])
                print("\n" + en_sent)

                te_sent = " ".join([data.te_index_dict[w] for w in data.dev_te[i]])
                print("".join(te_sent))

                src = torch.from_numpy(np.array(data.dev_en[i])).long().to(DEVICE)
                src = src.unsqueeze(0)
                src_mask = (src != 0).unsqueeze(-2)
                out = greedy_decode(model, src, src_mask, max_len=MAX_LENGTH, start_symbol=data.te_word_dict["BOS"])

                translation = []
                for j in range(1, out.size(1)):
                    sym = data.te_index_dict[out[0, j].item()]
                    if sym != 'EOS':
                        translation.append(sym)
                    else:
                        break
                translation_sentence = " ".join(translation)
                print("translation: %s" % translation_sentence)

                # Write the translated sentence to the candidate file
                f_pred.write(translation_sentence + '\n')
                # Write the reference sentence to the reference file
                f_ref.write(te_sent + '\n')

                # bleu_candidate(translation_sentence)

def evaluate_test(data, model):
    evaluate(data, model)

if __name__ == '__main__':
    from setting import TRAIN_FILE, DEV_FILE, TEST_FILE, SAVE_FILE
    from train import model
    from data_pre import PrepareData

    model.load_state_dict(torch.load(SAVE_FILE, map_location=torch.device('cpu'), weights_only=True))

    # model.load_state_dict(torch.load('save/n_modelp.pt', map_location=torch.device('cpu')))
    # data = PrepareData(TRAIN_FILE, DEV_FILE)
    data = PrepareData(TRAIN_FILE, DEV_FILE)

    evaluate_test(data, model)
