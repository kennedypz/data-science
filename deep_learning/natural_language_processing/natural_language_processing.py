#!pip install nltk

from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
import pandas as pd
import re
import nltk
nltk.download('rslp')
nltk.download('stopwords')
nltk.download('punkt')
# Use stemmer and stopwords from training/test data


# Importing dataset
df = pd.read_csv("deep_learning/data/dataset.csv", sep=",", encoding="utf8")

# df.head()

# How many positives and negatives in the dataset
# df.groupby('sentiment').count()

# Removing unecessary columns and creating a new
# binary colomn for the sentiment called "classification"
# because it's easier to work with numbers.
df.drop(columns=['id', 'text_en'], axis=1, inplace=True)
df['classification'] = df["sentiment"].replace(["neg", "pos"], [0, 1])

# Making all texts lowercase
text_lower = [t.lower() for t in df['text_pt']]
df['text_pt'] = text_lower

# df.head(5)


def remove_brackets(column):
    for x in range(1, len(column)):
        return (re.sub('[\[\]]', '', repr(column)))


stop_words = nltk.corpus.stopwords.words('portuguese')
stemmer = nltk.stem.RSLPStemmer()


for x in range(0, len(df['text_pt'])):
    # Removing stop words from text
    word_tokens = word_tokenize(df['text_pt'][x])
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    # Removing suffixes
    line = []
    text_tokenized = word_tokenize((remove_brackets(filtered_sentence)))
    line = [stemmer.stem(word) for word in text_tokenized]
    df['text_pt'][x] = (remove_brackets(line))

# Regex to remove symbols and numbers from data
token = RegexpTokenizer(r'[a-zA-Z0-9]+')

# Creates the vectorizer basend on passed params
cv = CountVectorizer(lowercase=True, stop_words=None, ngram_range=(1, 2),
                     tokenizer=token.tokenize)

# Matrixsparse text_pt column representation
text_counts = cv.fit_transform(df['text_pt'])

# Vocabulary
cv.vocabulary_

# Testing model using Naive Bayes instead of deep learning
# for it is less demanding to the system's setup

# Dividing dataset in train and test
X_train, X_test, y_train, y_test = train_test_split(text_counts, df['classification'],
                                                    test_size=0.34, random_state=1,
                                                    shuffle=True)
# Creates the model and train it
clf = MultinomialNB().fit(X_train, y_train)

# Predicting the value of X to test accuracy
y_predicted = clf.predict(X_test)
print("MultinomialNB Accuracy:", metrics.accuracy_score(
    y_test, y_predicted).round(3))

# Receiving data
# Split text in paragraphs
with open('texto_teste.txt', 'r') as file_teste:
    paragraph = file_teste.read().split('\n\n')

# Split paragraphs in phrase
with open('./texto_teste.txt', 'r') as file_teste:
    phrase = file_teste.read().split('.')


# Stemmer and remove stopwords from text
stemmer = nltk.stem.RSLPStemmer()

# Criate data frame
df_result = pd.DataFrame()


# Tokenize, remove stop words and transform data to predict
neg, pos = 0, 0
for x in range(0, len(phrase)-1):

    # Tokenized text
    text_tokenized = word_tokenize(phrase[x])

    # Remove stop words from text
    filtered_sentence = [w for w in text_tokenized if not w in stop_words]

    # Create stemmer from input text
    line = [stemmer.stem(word) for word in filtered_sentence]
    line = (remove_brackets(line))

    # Criar prediction para cada frase
    # Create prediction for each phrase
    value_trans = cv.transform([line])
    predict_phrase = clf.predict(value_trans)

    # Count by prediction type (positive and negative)
    if predict_phrase == 0:
        pos += 1
    else:
        neg += 1

# Store values in data frame
df_result['positive'] = [pos]
df_result['negative'] = [neg]

# Creating chart to visualize results


def generate_piechart(df_result):

    import matplotlib.pyplot as plt
    labels = df_result.columns.tolist()
    sizes = df_result.values.tolist()[0]
    color = ['lightskyblue', 'lightcoral']
    explode = (0.15, 0)

    fig1, ax1 = plt.subplots(figsize=(5, 5))
    ax1.pie(sizes, labels=labels,  explode=explode,
            shadow=True, autopct='%1.1f%%',  startangle=140, colors=color)

    ax1.set_title('Sentiment Analysis by phrases - NLTK', fontsize=15)

    ax1.axis('equal')
    plt.show()
    print("Quantity by paragraph: {}".format(len(paragraph)))
    print("Quantity by phrases: {}".format(len(phrase)-1))
    print("Quantity by positives phrases: {}".format(df_result['positive']
                                                     .values.tolist()[0]))

    print("Quantity by negatives phrases: {}".format(df_result['negative']
                                                     .values.tolist()[0]))


# Generates graph
generate_piechart(df_result)
