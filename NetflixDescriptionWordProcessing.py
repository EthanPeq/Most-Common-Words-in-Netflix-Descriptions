# Netflix Show descriptions

import matplotlib.pyplot as plt
with open('netflixshowdescriptions.txt', 'r', encoding='utf-8') as file: netflix = file.readlines()


# Strip away newline characters in the dataset
netflix = list(filter(None, [item.strip('\n') for item in netflix]))


# Graphing the number of characters per sentence
line_lengths = [len(sentence) for sentence in netflix]
plt.hist(line_lengths)
plt.title("Number of Chars Per Sentence")
plt.show()


# Break the sentences up into tokens
tokens = [item.split() for item in netflix]


# Graphing the number of tokens per sentence
tokens_per_sentence = [len(sentence.split()) for sentence in netflix]
plt.hist(tokens_per_sentence, color ='blue')
plt.title("Number of tokens per sentence")
plt.show()


# Creating one big list of tokens named words
words = [word for sentence in tokens for word in sentence]


# Printing the 10 most common words in the text corpus
from collections import Counter
print()
print("10 most common words")
words = [word.lower() for word in words]
c = Counter(words)
c10 = c.most_common(10)
for x in c10:
    print(x)


# Removing stopwords from the list of tokens
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]


# Printing the 10 most common non-stop words in the text corpus
print()
print("10 most filtered common words")
fw = Counter(filtered_words) #filtered word counter
fw10 = fw.most_common(10)
for x in fw10:
    print(x)


#Creating a WordCloud out of
from wordcloud import WordCloud
from PIL import Image
import numpy as py
words_string = " ".join(filtered_words)
word_mask = py.array(Image.open('netflix.png'))
wordcloud3 = WordCloud(max_words=30, background_color="white",
                        mask=word_mask, contour_width=3, contour_color="teal").generate(words_string)

    # Displaying the generated image
plt.imshow(wordcloud3, interpolation='bilinear')
plt.axis('off')
plt.show()


