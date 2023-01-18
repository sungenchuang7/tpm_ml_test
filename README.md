# Team Process Mapping Take-Home Task: [Sean Chuang].

Goal: In this pre-test, you will implement a feature extractor that detects sentiment from team conversations. Specifically, given an input of conversation data, you should output: (1) a sentiment label of ‘positive,’ ‘negative,’ or ‘neutral,’ alongside a score for each label, from 0-1. You will run your feature extractor on a dataset of team jury conversations.

You will then write a reflection on how well you think this feature extractor performed on the data. Please write your reflection in this README document.

## 1. What method(s) did you choose?
In 1-2 sentences each, describe your sentiment analysis method(s).

> I chose to use a model on HuggingFace that's pre-trained with 50M+ tweets, which are kind of similar to the data being dealt with (short and context dependent). With the model incorporated, get_sentiment() takes each utterance as an input parameter and feeds it to the model. The model then returns 3 scores for 3 sentiment labels respectively. 

## 2. Method evaluation
Next, we would like you to consider how you would evaluate your method. How do you know the classification or quantification of emotion is “right?” Try to think critically!

2a. Open up output/jury_output_chat_level.csv and look at the columns you generated. Do the values “make sense” intuitively? Why or why not?

> It makes sense intuitively, but with a bit of observation, it's easy to see some problems with the model. For example, if we feed the sentence "No I don't think he's an asshole", the model will return {'positive': 0.03134448, 'negative': 0.63912714, 'neutral': 0.32952848}. However, this sentence is apparently not negative, but because the word "asshole" is itself too negative, so the model seems to return a pretty negative outcome, regardless of how the sentence is phrased. It might be possible that during the pre-training process of the model, "asshole" was labeled as a very negative slur. Therefore, no matter in what form the word appears in the sentence, the sentence will be deemed very negative. 

2b. Propose an evaluation mechanism for your method(s). What metric would you use (e.g., F1, AUC, Accuracy, Precision, Recall)?

> To evaluate the "accuracy" of the model's predictions, I adopted the formula accuracy = ( number of correct predictions) / (number of all predictions), so basically calculating accuracy rate (true positive, true negative and true neutral)
 

2c. Describe the steps you would take in evaluating this method. Be as specific as possible.

> Since no labeled data is provided, I took a sample of size 52 (basically all utterances in batch 0 round 0) and asked 2 human friends of mine along with myself to participate in a majority vote to determine the label for each utterance. I then compared the result with the output from the model to calculate the accurary rate. This was tracked in test-data.xlsx

## 3. Overall reflection
3a. How much time did it take you to complete this task? (Please be honest; we are looking for feedback to make sure the task is scoped appropriately, as this is one of the first times we’re using this task.)

> Roughly 15 hours (including the running time of the program taking roughly 9 hours). 

3b. Finally, provide an overall reflection of your experience. How did you approach this task? What challenge(s) did you encounter? If you had more time, what are additional extensions, improvements, or tests that you would want to implement?

> - This task is quite challenging to me because it was really hard to define "positive" and "negative" for use in this case. I do not possess complete knowledge of how the model is pre-trained and the text data being dealth with in this task is quite niche. Hence, there's no guarantee that the model can work well with the data at hand. 

> - Another issue I encountered was, actually I would say a mistake I made was, I ran my Python script in my Terminal overnight since I noticed it took some time for the model to process my sample. However, when I woke up in the morning, the Terminal was still running the script. Due to the structure of featurize.py, nothing will be outputted to jury_output_chat_level.csv if jury_conversations_with_outcome_var.csv isn't fully processed yet. Unfortunately, a 24 hour extension helped tremendously. 

> - If I had additional time, first, I would find a way to make the raw dataset into different section and run the program in batches so it wouldn't be so risky to run it for 9 hours. 

> - Also, if I had more time, I would try to think of a less biased way of measuring the accurary of output. Human interpretation of the raw data seems to involve moral judgement (e.g. judging if the person is really an asshole instead of really objectively judging if the sentence sounds negative or positive) thus creating biases. In other words, the test data created by humans might also be biased. If I had more time, I would try to look into how the model I used was trained and also some papers to design better algorithm for testing data. 

