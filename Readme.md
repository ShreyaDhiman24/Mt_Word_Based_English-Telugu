# Transformer Implementation in PyTorch  
> Notes

## Files
- `setting.py`: Configuration file for model parameters and file directories.
- `utils.py`: Some utility functions, such as padding sentences of unequal length.
- `data_pre.py`: Preprocessing of data to obtain batch data and related mask matrices for model input.
- `model.py`: Model file. The model is initialized by calling the **make_model method** with the relevant initialization parameters.
- `train.py`: Training the model and saving the best model.
- `test.py`: Testing the output of sentences in the test set.
- `bleu_score.py`: Evaluating machine translation scores.
- `one_trans.py`: Translating a single sentence.
- `app.py`: Implementing a Flask API using the single sentence translation method from `one_trans`.
Model Training Data
Training using 14533 translation pairs.
Data file format: en\tcn

Results Evaluation
Evaluating translation effectiveness using the BLEU algorithm BLEU
BLEU algorithm evaluation results:

Evaluating 399 translated sentences
Validation set: 0.1075088492716548, n-gram weights: (1,0,0,0)
0.03417978514554449, n-gram weights: (1,0.2,0,0)
Attention: You need to create a save folder in the project directory before running the code.
PyTorch Official Transformer Interface

Transformer Explanation

Running the Project
python train.py: Train the model and save it.



