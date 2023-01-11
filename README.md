# Team Process Mapping Take-Home Task: [YOUR NAME HERE].

Goal: In this pre-test, you will implement a feature extractor that detects sentiment from team conversations. Specifically, given an input of conversation data, you should output: (1) a sentiment label of ‘positive,’ ‘negative,’ or ‘neutral,’ alongside a score for each label, from 0-1. You will run your feature extractor on (1) a dataset of team jury conversations; and (2) an external benchmark dataset.

You will then write a reflection on how well you think this feature extractor performed on the data. Please write your reflection in this README document.

## What method(s) did you choose?
Describe your sentiment analysis method(s) below.

[YOUR ANSWER HERE]

## Why did you choose the method(s)?
a.	Have others in the field used this method? If so, who?

[YOUR ANSWER HERE]

b.	What advantage does this method have over others?

[YOUR ANSWER HERE]

c.	What are some disadvantages or limitations of this method?

[YOUR ANSWER HERE]


## Method evaluation
Propose an evaluation mechanism for your method. How do you know the classification or quantification of emotion is “right?”

[YOUR ANSWER HERE]

### Evaluate your feature extractor based on the criteria you proposed.
First, let's start by qualitatively looking at your output on the jury dataset. Look at the output CSV and your generated results. Do your outputs qualitatively "make sense?"

[YOUR ANSWER]

a.	Give a few examples in which the feature extractor works as expected.

[YOUR ANSWER]

b.	Give a few examples in which the feature extractor does not (seem to) work as expected. Are there cases, for example, where a positive sentence is mislabeled as negative, or vice versa? What “broke?” Is this an edge case?

[YOUR ANSWER]

### Next, you will evaluate your feature extractor on an an external benchmark dataset. If you implemented multiple methods, please do this for each method, so that you can compare/contrast their performance.

c. Select an evaluation metric (e.g., F1, AUC, Accuracy, Precision, Recall). You may use a combination of multiple metrics.

[STATE YOUR EVALUATION METRIC(S) HERE]

d. Why did you select this metric? Discuss briefly.

[YOUR ANSWER]

e. Load the DynaSent benchmark dataset (https://github.com/cgpotts/dynasent). Choose the Round 2 test dataset ("Sentences crowdsourced using Dynabench"). Evaluate your model on the test dataset, using the metric(s) you selected in part (c). You may present your results in a list or table (whichever is more convenient).

[YOUR RESULTS HERE]


## Overall reflection
Finally, provide an overall reflection of your experience. How did you approach this task? How did you approach training, testing, and validation of your model? What challenge(s) did you encounter? If you had more time, what are some ways that you would want to improve your feature extractor?

[YOUR ANSWER]
