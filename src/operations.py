from difflib import SequenceMatcher
# from language_tool_python import LanguageTool
from nltk.collocations import BigramCollocationFinder
from nltk.corpus import stopwords, wordnet
from nltk.metrics import BigramAssocMeasures
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import nltk

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def find_grammar_errors(text):
    # Tokenize the text into words
    words = word_tokenize(text)

    # Perform part-of-speech tagging
    pos_tags = nltk.pos_tag(words)

    # Identify potential subject-verb agreement errors
    errors = []
    for i in range(len(pos_tags) - 1):
        word, pos = pos_tags[i]
        next_word, next_pos = pos_tags[i + 1]
        if pos.startswith('V') and next_pos.startswith('NN'):
            errors.append(f"Possible subject-verb agreement error: '{word}' is a verb followed by '{next_word}' which is a noun.")
    return errors

def calculate_lexical_diversity(text):
    words = text.lower().split()  # Tokenize text into words (case-insensitive)
    unique_words = set(words)     # Get unique words
    total_words = len(words)      # Total number of words
    unique_word_count = len(unique_words)  # Number of unique words

    if total_words == 0:
        return 0  # Avoid division by zero error
    else:
        return unique_word_count / total_words  # Lexical diversity score

def get_sentences(text):
    return nltk.sent_tokenize(text)

def calculate_phraseology_score(text1, text2):
    # Tokenize the texts into n-grams
    vectorizer = CountVectorizer(analyzer='word', ngram_range=(1, 3))
    X = vectorizer.fit_transform([text1, text2])

    # Calculate cosine similarity between the n-gram vectors
    cosine_sim = cosine_similarity(X[0], X[1])[0][0]

    return cosine_sim

def calculate_phrase_relation_score(sentence1, sentence2):
    # Tokenize the sentences into words
    words1 = nltk.word_tokenize(sentence1.lower())
    words2 = nltk.word_tokenize(sentence2.lower())

    # Calculate bigrams for each sentence
    bigrams1 = set(nltk.bigrams(words1))
    bigrams2 = set(nltk.bigrams(words2))

    # Calculate the number of shared bigrams
    shared_bigrams = bigrams1.intersection(bigrams2)

    # Calculate the phrase relation score
    score = len(shared_bigrams) / (len(bigrams1) + len(bigrams2))

    return score

def calculate_vocabulary_score(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Count the unique tokens
    unique_tokens = set(tokens)

    # Calculate vocabulary score
    vocabulary_score = len(unique_tokens) / len(tokens)

    return vocabulary_score

def calculate_vocabulary_score2(essay_text):
    # Tokenize the text into words
    words = word_tokenize(essay_text)

    # Convert words to lowercase
    words = [word.lower() for word in words]

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # Calculate vocabulary score
    vocabulary_score = len(set(words)) / len(words) * 100
    return vocabulary_score

# Function to calculate cohesion score for a given sentence
def calculate_cohesion_score(sentence):
    # sentences = sent_tokenize(sentence)
    words = word_tokenize(sentence)
    cohesion_score = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            word1 = words[i]
            word2 = words[j]
            # Calculate the similarity between two words using WordNet
            synsets1 = wordnet.synsets(word1)
            synsets2 = wordnet.synsets(word2)
            if synsets1 and synsets2:
                similarity = synsets1[0].path_similarity(synsets2[0])
                if similarity:
                    cohesion_score += similarity
    return cohesion_score

def conventions_score(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]

    # Calculate sentiment score using Vader sentiment analyzer
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(" ".join(filtered_tokens))

    # Conventions score calculation
    score = (sentiment_score['pos'] - sentiment_score['neg']) / (sentiment_score['pos'] + sentiment_score['neg'] + sentiment_score['neu'])
    return score