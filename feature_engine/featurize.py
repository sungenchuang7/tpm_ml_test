import csv
import pandas as pd

"""
file: featurize.py
---
This file is the main "engine" that takes as input a cleaned 
data file (as CSV) and outputs a bunch of generated conversational 
features (as another CSV, in the output/ folder).

Primarily, it adds columns to the input CSV, in which every column
transforms the message/conversation using one of the functions in
the features/ folder.
"""

# import our feature files
from features.basic_features import *
from features.gini_coefficient import *
from features.sentiment_features import * # TPM TAKE-HOME: THIS IS THE FILE YOU'LL EDIT!

'''
@param df = the name of the dataframe on which the operation is being applied.
	- assumes that the df is a chat-by-chat setup in which each row is 1 chat.
	- assumes that the chat is stored in a column called 'message'
@param feature_name = the name of the column you want the feature to be named
@param function_name = the name of the function used to create the feature
'''
def create_chat_level_feature(df, feature_name, function_name):
	df[feature_name] = df['message'].apply(lambda x: function_name(str(x)))
	return(df)


# Main Function
if __name__ == "__main__":

	# import the data from the data file
	INPUT_FILE_PATH = './data/raw_data/jury_conversations_with_outcome_var.csv'
	# INPUT_FILE_PATH = './data/raw_data/sample.csv'
	OUTPUT_FILE_PATH_CHAT_LEVEL = './output/jury_output_chat_level.csv'

	conversation_data = pd.read_csv(INPUT_FILE_PATH)
	output_data_chats = conversation_data



	### CHAT-LEVEL FEATURES --------------------------------------------------------------
	'''
	chat-level features take place on the single-utterance level. Each person will make
	many utterances throughout a conversation.
	'''
	
	output_data_chats = create_chat_level_feature(output_data_chats, "num_words", count_words)
	output_data_chats = create_chat_level_feature(output_data_chats, "num_chars", count_characters)
	
	# TPM TAKE-HOME: YOUR FEATURE EXTRACTOR GOES HERE.

	output_data_chats = create_chat_level_feature(output_data_chats, "sentiment", get_sentiment)

	# generate output file
	output_data_chats.to_csv(OUTPUT_FILE_PATH_CHAT_LEVEL)


	### CONVERSATION-LEVEL FEATURES --------------------------------------------------------------
	OUTPUT_FILE_PATH_CONVERSATION_LEVEL = './output/sample.csv'
	OUTPUT_FILE_PATH_CONVERSATION_LEVEL = './output/test-output.csv'

	'''
	conversation-level features take place at the level of the entire conversation; 
	we may need to pass the chat-level features into additional functions in order 
	to calculate conversation-level features. As an example, Gini is a conversational-
	level summary of how many chats each person in the conversation made.
	'''
	# basic output data on the conversation level -- just the batch and round nums
	output_data_conversations = conversation_data.groupby(['batch_num', 'round_num']).sum(numeric_only = True).reset_index().iloc[: , :2]
	
	# generate all conversation level features here
	output_data_conversations = pd.merge(output_data_conversations, get_gini(output_data_chats, "num_words"), on=['batch_num', 'round_num'])
	output_data_conversations = pd.merge(output_data_conversations, get_gini(output_data_chats, "num_chars"), on=['batch_num', 'round_num'])

	# generate output file
	output_data_conversations.to_csv(OUTPUT_FILE_PATH_CONVERSATION_LEVEL)

