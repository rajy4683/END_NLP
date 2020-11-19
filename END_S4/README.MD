# Assignment-4: Training a basic Sentiment analyzer

## TOC

1. [Overview](#overview)
2. [Sentiment Analysis with LSTMs](#sentiment-analysis-with-lstms)
3. [Training Methodology](#training-methodology)
4. [Results](#results)
3. [References](#references)

## Overview

This assignment is a foray into LSTMs and NLP models. The model is trained on IMDB dataset available with PyTorch
Glove embeddings are used as the embedding layers
The original notebook which forms the basis can be found [here](https://github.com/bentrevett/pytorch-sentiment-analysis/blob/master/2%20-%20Upgraded%20Sentiment%20Analysis.ipynb)

## Seq2Seq Translation with Bahdnau Attention

The model consists of following elements:

1. Embedding Layer: Glove embeddings of 100 dimension
2. LSTM Block: 3 Single layer(384 dimension), unidirectional LSTM blocks with `hidden` and `cell` parameters cascaded.
3. Fully connected layer: Final Layer to provide prediction of +ve or -ve sentiment

Adam optimizer with default settings (β1=0.9, β2=0.999 and ϵ=10−8). Binary Cross-Entropy loss is used as the cost-function.


## Training Methodology

1. The training data was first **reversed** and fed to the model. The training was done for 20 epochs
2. The training data was corrected back to normal and fed to the model and the model was trained for further 20 epochs


Training code can be found in this [notebook](https://github.com/rajy4683/EVA4P2/blob/master/S11-Attention/EVA4P2S11_Attention.ipynb)

## Results

In the first stage training Validation Accuracy reached was 87.43%.
In the second stage training Validation Accuracy reached was 87.43%.

## References

- END Course content
- [Ben Trevett's Repo](https://github.com/bentrevett/pytorch-sentiment-analysis)
- [Packing and Padding demo](https://gist.github.com/HarshTrivedi/f4e7293e941b17d19058f6fb90ab0feIc)
