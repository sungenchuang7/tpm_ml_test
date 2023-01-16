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


# TODO - DEFINE YOUR FEATURE EXTRACTOR HERE
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

def get_sentiment(text):
    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    # PT
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    #model.save_pretrained(MODEL)
    text = "he's a human"
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    keys = ['positive', 'negative', 'neutral']

    dictionary = {}
    dictionary[keys[0]] = scores[2]
    dictionary[keys[1]] = scores[0]
    dictionary[keys[2]] = scores[1]

    return dictionary

    # tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    # model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")

    # inputs = tokenizer(text, return_tensors="pt")
    # with torch.no_grad():
    #     logits = model(**inputs).logits
    # scores = {k: v for k, v in zip(model.config.id2label.values(), scipy.special.softmax(logits.numpy().squeeze()))}
        
    # return scores
    # sample output format
    # return({'positive': 0.0, 'negative': 0.0, 'neutral': 0.0})