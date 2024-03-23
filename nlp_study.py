# -*- coding: utf-8 -*-
"""NLP_study.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/115IfpAqnI0GrlUAP6udFUomEbfe3yles

# 0.Importing libraries
"""

import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import tensorflow
import keras
import gensim
import warnings
warnings.filterwarnings('ignore')

#nltk.download()

!curl -s https://raw.githubusercontent.com/teddylee777/machine-learning/master/99-Misc/01-Colab/mecab-colab.sh | bash

!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git

cd Mecab-ko-for-Google-Colab

!bash install_mecab-ko_on_colab_light_220429.sh

from konlpy.tag import Okt, Mecab

"""# 1.Warming up - Pandas & Numpy

##Pandas - Series
"""

sr = pd.Series([100, 200], index = ["pizza", "chicken"])
print("Print the Series :")
print('-' * 20)
print(sr)

print("Values of the series {}:" .format(sr.values))
print("Indices of the series {}:" .format(sr.index))

"""##Pandas - DataFrame"""

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index = index, columns = columns)

print("Print the DataFrame : ")
print('-' * 20)
print(df)

print(df.values)
print(df.index)
print(df.columns)

df['A']

df.iloc[0]

"""##Numpy - array"""

vec = np.array(np.arange(1, 6))
mat = np.array([[10, 20, 30], [ 60, 70, 80]])

print(mat)

print(vec.ndim)
print(vec.shape)

print(mat.ndim)
print(mat.shape)

zero_mat = np.zeros((2, 3))
print(zero_mat)

one_mat = np.ones((2, 3))
print(one_mat)

same_value_mat = np.full((2, 3), 5)
print(same_value_mat)

eye_mat = np.eye(5)
print(eye_mat)

random_mat = np.random.random((2, 3))
print(random_mat)

reshape_mat = np.array(np.arange(30)).reshape((5, 6))
print(reshape_mat)

slicing_mat = reshape_mat[0, :]
print(slicing_mat)

indexing_mat = reshape_mat[[0, 1], [1, 2]]
print(indexing_mat)

mat1 = np.arange(1, 5).reshape((2, 2))
mat2 = np.arange(5, 9).reshape((2, 2))
mat3 = np.dot(mat1, mat2)
print(mat3)

"""##Matplotlib"""

plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.show()

plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.xlabel('hours')
plt.ylabel('score')
plt.show()

plt.title('test')
plt.plot([1, 2, 3, 4], [2, 4, 8, 6])
plt.plot([1.5, 2.5, 3.5, 4.5], [3, 5, 8, 10])
plt.xlabel('hours')
plt.ylabel('score')
plt.legend(['A student', 'B student'])
plt.show()

"""# 2.Text preprocessing

##2-1.Tokenization

###Word Tokenization
"""

from nltk.tokenize import word_tokenize, WordPunctTokenizer
from tensorflow.keras.preprocessing.text import text_to_word_sequence

nltk.download('punkt')

print('Tokenize word1 : ',word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pasty shop."))

print('Tokenize word2 : ', WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

print('Tokenize word3 : ', text_to_word_sequence("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."

print("Treebank word tokenizer : ", tokenizer.tokenize(text))

"""###Sentence Tokenization"""

from nltk.tokenize import sent_tokenize

text = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."

print("Sentence tokenization1 : ", sent_tokenize(text))

text = "I am actively looking for Ph.D. students. and you are a Ph.D student."
print("Sentence tokenization2 : ", sent_tokenize(text))

!pip install kss

import kss

text = '딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?'

print('Korean sentence tokenization : ', kss.split_sentences(text))

"""###POS tagging"""

from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger')

text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."
tokenized_sentence = word_tokenize(text)

print('Word tokenization :', tokenized_sentence)
print('POS tagging : ',pos_tag(tokenized_sentence))

from konlpy.tag import Okt
from konlpy.tag import Kkma

okt = Okt()
kkma = Kkma()

print("OKT morpheme analysis : ", okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print("OKT POS tagging : ", okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print("OKT extracting Noun : ", okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

print('꼬꼬마 morpheme analysis : ', kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print('꼬꼬마 POS tagging : ', kkma.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))
print('꼬꼬마 extracting Noun : ', kkma.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))

"""##2-2.Cleaning and Normalization"""

import re
text = "I was wondering if anyone out there could enlighten me on this car."
shortword = re.compile(r'\w*\b\w{1,2}\b')
print(shortword.sub('', text))

"""##2-3.Stemming and Lemmatization

Lemmatization
"""

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print('Before lemmatization : ', words)
print('After lemmatization : ',[lemmatizer.lemmatize(word) for word in words])

lemmatizer.lemmatize('dies', 'v')

lemmatizer.lemmatize('watched', 'v')

lemmatizer.lemmatize('has', 'v')

"""Stemming"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('punkt')

stemmer = PorterStemmer()

sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
tokenized_sentence = word_tokenize(sentence)

print("Before stemming : ", tokenized_sentence)
print("After stemming : ", [stemmer.stem(word) for word in tokenized_sentence])

words = ['formalize', 'allowance', 'electricical']

print("Before stemming : ", words)
print("After stemming : ", [stemmer.stem(word) for word in words])

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print("Before stemming : ", words)
print("After Porter Stemming : ", [porter_stemmer.stem(word) for word in words])
print("After Lancaster Stemming : ", [lancaster_stemmer.stem(word) for word in words])

"""##2-4.Stopword"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

nltk.download('stopwords')
stop_words_list = stopwords.words('english')
print('Number of stopword : ', len(stop_words_list))
print('Print 10 stopwords : ', stop_words_list[:10])

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example)
result = []
for word in word_tokens:
  if word not in stop_words:
    result.append(word)
print("Before eliminating stopword : ",word_tokens)
print("After eliminating stopword : ", result)

#Korean
okt = Okt()

example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "를 아무렇게나 구 우려 고 안 돼 같은 게 구울 때 는"

stop_words = set(stop_words.split(' '))
word_tokens = okt.morphs(example)

result = [word for word in word_tokens if not word in stop_words]

print('Before eliminating stopword : ', word_tokens)
print('After eliminating stopword : ', result)

"""##2-5.Regular Expression"""

import re

r = re.compile("a.c")
r.search("kkk")

r.search("abc")

r = re.compile("ab?c")
r.search("abbc")

r.search("abc")

r.search("ac")

r = re.compile("ab*c")
r.search("a")

r.search("ac")

r.search("abc")

r.search("abbbc")

r = re.compile("ab+c")
r.search("ac")

r.search("abc")

r.search("abbbbc")

r = re.compile("^ab")
r.search("bbc")
r.search("zab")

r.search("abz")

r = re.compile("ab{2}c")
r.search("ac")
r.search("abc")
r.search("abbbbc")

r.search("abbc")

r = re.compile("ab{2,8}c")
r.search("ac")
r.search("abc")
r.search("abbbbbbbbbc")

r.search("abbc")

r.search("abbbbbbbbc")

r = re.compile("a{2,}bc")
r.search("bc")
r.search("aa")

r.search("aabc")

r.search("aaaaaaaabc")

r = re.compile("[abc]") #[abc] equals to [a-c]
r.search("zzzz")

r.search("a")

r.search("aaaa")

r.search("zbaac")

r = re.compile("[a-z]")
r.search("AAA")
r.search("111")

r.search("aBC")

r = re.compile("[^abc]")
r.search("a")
r.search("ab")
r.search("b")

r.search("d")

r.search("1")

r = re.compile("ab.")
r.match("kkkabc")

r.match("abckkk")

text = "사과 딸기 수박 메론 바나나"
re.split(" ", text)

text = """사과
딸기
수박
메론
바나나"""

re.split("\n", text)

text = "사과+딸기+수박+메론+바나나"

re.split("\+", text)

text = """이름 : 김철수
전화번호 : 010 - 1234 - 1234
나이 : 30
성별 : 남"""

re.findall("\d+", text)

re.findall("\d+", "문자열입니다.")

text = "Regular expression : A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern."

preprocessed_text = re.sub('[^a-zA-Z]', ' ', text)
print(preprocessed_text)

text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""

re.split('\s+', text)

re.findall('\d+', text)

re.findall('[A-Z]', text)

re.findall('[A-Z]{4}', text)

re.findall('[A-Z][a-z]+', text)

from nltk.tokenize import RegexpTokenizer

text = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"

tokenizer1 = RegexpTokenizer("[\w]+")
tokenizer2 = RegexpTokenizer("\s+", gaps = True)

print(tokenizer1.tokenize(text))
print(tokenizer2.tokenize(text))

"""##2-6.Integer Encoding

###1)Integer Encoding
"""

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

raw_text = "A barber is a person. a barber is good person. a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. But keeping and keeping such a huge secret to himself was driving the barber crazy. the barber went up a huge mountain."

nltk.download('punkt')
sentences = sent_tokenize(raw_text)
print(sentences)

nltk.download('stopwords')
vocab = {}
preprocessed_sentences = []
stop_words = set(stopwords.words('english'))

for sentence in sentences:
  tokenized_sentence = word_tokenize(sentence)
  result = []

  for word in tokenized_sentence:
    word = word.lower()

    if word not in stop_words:

      if len(word) > 2:
        result.append(word)

        if word not in vocab:
          vocab[word] = 0
        vocab[word] += 1
  preprocessed_sentences.append(result)
print(preprocessed_sentences)

print("Word set :", vocab)

print(vocab["barber"])

vocab_sorted = sorted(vocab.items(), key = lambda x : x[1], reverse = True)
print(vocab_sorted)

word_to_index = {}
i = 0
for (word, frequency) in vocab_sorted:
  if frequency > 1:
    i = i + 1
    word_to_index[word] = i
print(word_to_index)

vocab_size = 5

words_frequency = [word for word, index in word_to_index.items() if index >= vocab_size + 1]

for w in words_frequency:
  del word_to_index[w]
print(word_to_index)

word_to_index['OOV'] = len(word_to_index) + 1
print(word_to_index)

encoded_sentences = []
for sentence in preprocessed_sentences:
  encoded_sentence = []
  for word in sentence:
    try:
      encoded_sentence.append(word_to_index[word])
    except KeyError:
      encoded_sentence.append(word_to_index['OOV'])
  encoded_sentences.append(encoded_sentence)
print(encoded_sentences)

"""###2)Using Counter"""

from collections import Counter

print(preprocessed_sentences)

#words = np.hstack(preprocessed_sentences)
all_words_list = sum(preprocessed_sentences, [])
print(all_words_list)

vocab = Counter(all_words_list)
print(vocab)

print(vocab["barber"])

vocab_size = 5
vocab = vocab.most_common(vocab_size)
vocab

word_to_index = {}
i = 0
for (word, frequency) in vocab:
  i = i + 1
  word_to_index[word] = i
print(word_to_index)

"""###3)Using FreqDist of NLTK"""

from nltk import FreqDist
import numpy as np

vocab = FreqDist(np.hstack(preprocessed_sentences))

print(vocab["barber"])

vocab_size = 5
vocab = vocab.most_common(vocab_size)
print(vocab)

word_to_index = {word[0] : index + 1 for index, word in enumerate(vocab)}
print(word_to_index)

test_input = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(test_input):
  print("value : {}, index : {}".format(value, index))

"""###Text preprocessing with Keras"""

from tensorflow.keras.preprocessing.text import Tokenizer

preprocessed_sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(preprocessed_sentences)

print(tokenizer.word_index)

print(tokenizer.word_counts)

print(tokenizer.texts_to_sequences(preprocessed_sentences))

vocab_size = 5
tokenizer = Tokenizer(num_words = vocab_size + 1)
tokenizer.fit_on_texts(preprocessed_sentences)

print(tokenizer.word_index)

print(tokenizer.word_counts)

print(tokenizer.texts_to_sequences(preprocessed_sentences))

tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_sentences)

vocab_size = 5
words_frequency = [word for word, index in tokenizer.word_index.items() if index >= vocab_size + 1]

for word in words_frequency:
  del tokenizer.word_index[word]
  del tokenizer.word_counts[word]

print(tokenizer.word_index)
print(tokenizer.word_counts)
print(tokenizer.texts_to_sequences(preprocessed_sentences))

voacb_size = 5
tokenizer = Tokenizer(num_words = vocab_size + 2, oov_token = 'OOV')
tokenizer.fit_on_texts(preprocessed_sentences)

print('Number of OOV\'s index : {}'.format(tokenizer.word_index['OOV']))

print(tokenizer.texts_to_sequences(preprocessed_sentences))

"""##2-7.Padding

###1.Padding with Numpy
"""

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

preprocessed_sentences = [['barber', 'person'], ['barber', 'good', 'person'], ['barber', 'huge', 'person'], ['knew', 'secret'], ['secret', 'kept', 'huge', 'secret'], ['huge', 'secret'], ['barber', 'kept', 'word'], ['barber', 'kept', 'word'], ['barber', 'kept', 'secret'], ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy'], ['barber', 'went', 'huge', 'mountain']]

tokenizer = Tokenizer()
tokenizer.fit_on_texts(preprocessed_sentences)
encoded = tokenizer.texts_to_sequences(preprocessed_sentences)
print(encoded)

max_len = max(len(item) for item in encoded)
print("Max length :", max_len)

for sentence in encoded:
  while len(sentence) < max_len:
    sentence.append(0)
padded_np = np.array(encoded)
padded_np



"""###2.Padding with Keras preprocessing"""

from tensorflow.keras.preprocessing.sequence import pad_sequences

encoded = tokenizer.texts_to_sequences(preprocessed_sentences)
print(encoded)

padded = pad_sequences(encoded)
padded

padded = pad_sequences(encoded, padding = 'post')
padded

(padded == padded_np).all()

padded = pad_sequences(encoded, padding = 'post', maxlen = 5)
padded

padded = pad_sequences(encoded, padding = 'post', truncating = 'post', maxlen = 5)
padded

last_value = len(tokenizer.word_index) + 1
print(last_value)

padded = pad_sequences(encoded, padding = 'post', value = last_value)
padded

"""##2-8.One-Hot Encoding

###with konlpy
"""

from konlpy.tag import Okt

okt = Okt()
tokens = okt.morphs("나는 자연어 처리를 배운다")
print(tokens)

word_to_index = {word : index for index, word in enumerate(tokens)}
print("Word set :", word_to_index)

def one_hot_encoding(word, word_to_index):
  one_hot_vector = [0] * (len(word_to_index))
  index = word_to_index[word]
  one_hot_vector[index] = 1
  return one_hot_vector

one_hot_encoding("자연어", word_to_index)

"""###with Keras"""

text = "나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical

text = "나랑 점심 먹으러 갈래 점심 메뉴는 햄버거 갈래 갈래 햄버거 최고야"

tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])
print("Word set :", tokenizer.word_index)

sub_text = "점심 먹으러 갈래 메뉴는 햄버거 최고야"
encoded = tokenizer.texts_to_sequences([sub_text])[0]
print(encoded)

one_hot = to_categorical(encoded)
print(one_hot)

"""##2-9.Splitting Data"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

"""###1.Splitting into X and y from the original data"""

#with zip function
X, y = zip(['a', 1], ['b', 2], ['c', 3])
print("X data :", X)
print("y data :", y)

sequences = [['a', 1], ['b', 2], ['c', 3]]
X, y = zip(*sequences)
print("X data :", X)
print("y data :", y)

#with DataFrame

values = [['당신에게 드리는 마지막 혜택!', 1],
['내일 뵐 수 있을지 확인 부탁드...', 0],
['도연씨. 잘 지내시죠? 오랜만입...', 0],
['(광고) AI로 주가를 예측할 수 있다!', 1]]
columns = ['메일 본문', '스팸 메일 유무']

df = pd.DataFrame(values, columns = columns)
df

X = df['메일 본문']
y = df['스팸 메일 유무']

print("X data :", X.to_list())
print("y data :", y.to_list())

#with Numpy
np_array = np.arange(0, 16).reshape((4, 4))
print("Whole data :")
print(np_array)

X = np_array[:, :3]
y = np_array[:, 3]

print("X data :")
print(X)
print("y data :", y)

"""###2.Extracting test data"""

#with scikit-learn

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)

X, y = np.arange(10).reshape((5, 2)), range(5)

print("Whole X data :")
print(X)
print("Whole y data :")
print(list(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1234)

print("X train data :")
print(X_train)
print("X test data :")
print(X_test)

print("y train data :")
print(y_train)
print("y test data :")
print(y_test)

#different value for random_state

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)

print("y train data :")
print(y_train)
print("y test data :")
print(y_test)

# back to 1234 for random_state value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

print('y 훈련 데이터 :')
print(y_train)
print('y 테스트 데이터 :')
print(y_test)

#manual extracting from here
X, y = np.arange(0, 24).reshape((12, 2)), range(12)

print("Whole X data :")
print(X)
print("Whole y data :")
print(list(y))

num_of_train = int(len(X) * 0.8)
num_of_test = int(len(X) - num_of_train)
print("Size of train data :", num_of_train)
print("Size of test data :", num_of_test)

X_test = X[num_of_train:]
y_test = y[num_of_train:]
X_train = X[:num_of_train]
y_train = y[:num_of_train]

print("X test data :")
print(X_test)
print("y test data :")
print(list(y_test))

"""##2-10.Text Preprocessing Tools for Korean Text

###1.PyKoSpacing
"""

pip install git+https://github.com/haven-jeon/PyKoSpacing.git

sent = '김철수는 극중 두 인격의 사나이 이광수 역을 맡았다. 철수는 한국 유일의 태권도 전승자를 가리는 결전의 날을 앞두고 10년간 함께 훈련한 사형인 유연재(김광수 분)를 찾으러 속세로 내려온 인물이다.'

new_sent = sent.replace(" ", "")
print(new_sent)

from pykospacing import Spacing
spacing = Spacing()
kospacing_sent = spacing(new_sent)

print(sent)
print(kospacing_sent)

"""###2.Py-Hanspell

*   Skip running the following cells
*   Because currently Py-hanspell doesn't work. (03/03/2024)




"""

#pip install git+https://github.com/ssut/py-hanspell.git

#from hanspell import spell_checker

#sent = "맞춤법 틀리면 외 않되? 쓰고싶은대로쓰면돼지 "
#spelled_sent = spell_checker.check(sent)

#hanspell_sent = spelled_sent.checked
#print(hanspell_sent)

#spelled_sent = spell_checker.check(new_sent)

#hanspell_sent = spelled_sent.checked
#print(hanspell_sent)
#print(kospacing_sent)

"""###3.Tokenization with SOYNLP"""

pip install soynlp

from konlpy.tag import Okt
tokenizer = Okt()
print(tokenizer.morphs("에이비식스 이대휘 1월 최애돌 기부 요정"))

import urllib.request
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor

urllib.request.urlretrieve("https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt", filename="2016-10-20.txt")

corpus = DoublespaceLineCorpus("2016-10-20.txt")
len(corpus)

i = 0
for document in corpus:
  if len(document) > 0:
    print(document)
    i = i + 1
  if i == 3:
    break

word_extractor = WordExtractor()
word_extractor.train(corpus)
word_score_table = word_extractor.extract()

word_score_table["반포한"].cohesion_forward

word_score_table["반포한강"].cohesion_forward

word_score_table["반포한강공"].cohesion_forward

word_score_table["반포한강공원"].cohesion_forward

word_score_table["반포한강공원에"].cohesion_forward

word_score_table["디스"].right_branching_entropy

word_score_table["디스플"].right_branching_entropy

word_score_table["디스플레"].right_branching_entropy

word_score_table["디스플레이"].right_branching_entropy

from soynlp.tokenizer import LTokenizer

scores = {word : score.cohesion_forward for word, score in word_score_table.items()}
l_tokenizer = LTokenizer(scores = scores)
l_tokenizer.tokenize("국제사회와 우리의 노력들로 범죄를 척결하자", flatten = False)

from soynlp.tokenizer import MaxScoreTokenizer

maxscore_tokenizer = MaxScoreTokenizer(scores = scores)
maxscore_tokenizer.tokenize("국제사회와 우리의 노력들로 범죄를 척결하자")

"""###4.Cleaning repetitive letters with SOYNLP"""

from soynlp.normalizer import *

print(emoticon_normalize('앜ㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠ', num_repeats = 2))
print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠ', num_repeats=2))
print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠㅠ', num_repeats=2))
print(emoticon_normalize('앜ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ이영화존잼쓰ㅠㅠㅠㅠㅠㅠㅠㅠㅠ', num_repeats=2))

print(repeat_normalize('와하하하하하하하하하핫', num_repeats=2))
print(repeat_normalize('와하하하하하하하핫', num_repeats=2))
print(repeat_normalize('와하하하하하핫', num_repeats=2))

"""###5.Customized KoNLPy"""

pip install customized_konlpy

from ckonlpy.tag import Twitter
twitter = Twitter()
twitter.morphs('은경이는 사무실로 갔습니다.')

twitter.add_dictionary('은경이', 'Noun')

twitter.morphs('은경이는 사무실로 갔습니다.')

"""#3.Labguage Model"""

