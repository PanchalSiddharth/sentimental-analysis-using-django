from django.shortcuts import render, redirect
from textblob import TextBlob,Word 
import random 
import time


def index(request):
	if request.method=='GET':
		return render(request,'index.html')

def analyse(request):
	print(request.method,'....................')
	try:
		start = time.time()
		if request.method == 'POST':
			# summary,final_time,blob_sentiment,blob_subjectivity,received_ext=None
			rawtext = request.POST.get('rawtext')
			print(".......................",rawtext)
			#NLP Stuff
			blob = TextBlob(rawtext)
			received_text = blob
			blob_sentiment,blob_subjectivity = blob.sentiment.polarity ,blob.sentiment.subjectivity
			number_of_tokens = len(list(blob.words))
			# Extracting Main Points
			nouns = list()
			for word, tag in blob.tags:
				print(tag)
				# if tag == 'NN' or True:
				nouns.append(word.lemmatize())
				len_of_words = len(nouns)
				rand_words = random.sample(nouns,len(nouns))
				final_word = list()
				for item in rand_words:
					word = Word(item).pluralize()
					final_word.append(word)
					summary = final_word
					print(summary)
					end = time.time()
					final_time = end-start
			
				# else:
				# 	summary = None
				# 	final_time = None
				# 	len_of_words = None
				# 	blob_sentiment = None
				# 	blob_subjectivity = None
				# 	received_text = None
				# 	number_of_tokens = None
			return render(request,'index.html', {'summary':summary,'blob_sentiment':blob_sentiment,'blob_subjectivity':blob_subjectivity,'final_time':final_time,'received_text':received_text,'len_of_words':len_of_words,'number_of_tokens':number_of_tokens})
	except Exception as ex:
		print(ex)		
		return redirect('index')