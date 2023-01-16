# from transformers import pipeline
# sentiment_pipeline = pipeline("sentiment-analysis")
# data = ["I love you", "I hate you"]
# print(sentiment_pipeline(data))

# print("test1's name: {}".format(__name__)) 

from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis")
text = "hello"
print(sentiment_pipeline(text))




