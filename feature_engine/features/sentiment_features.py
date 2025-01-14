# imports
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import scipy
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

from transformers import logging

logging.set_verbosity_warning()


# TODO - DEFINE YOUR FEATURE EXTRACTOR HERE
# source: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)


def get_sentiment(text):
    
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    # PT
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    #model.save_pretrained(MODEL)
    text = preprocess(text)

    ###
    print("current text: ",end="")
    print(text)
    ###
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    keys = ['positive', 'negative', 'neutral']

    dictionary = {}
    dictionary[keys[0]] = scores[2]
    dictionary[keys[1]] = scores[0]
    dictionary[keys[2]] = scores[1]

    ###
    print(dictionary)
    ###
    
    return dictionary

    # sample output format
    # return({'positive': 0.0, 'negative': 0.0, 'neutral': 0.0})