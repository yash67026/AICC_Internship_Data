import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

nltk.download('punkt')
nltk.download('stopwords')

def extract_keywords(text):
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize
    words = word_tokenize(text)
    
    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Count frequency
    freq = Counter(words)
    
    # Get top keywords
    keywords = freq.most_common(5)
    
    return keywords


text = "Natural Language Processing helps computers understand human language and extract useful information."

print("Keywords:", extract_keywords(text))