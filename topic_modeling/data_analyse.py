# ### Eindversie Track3
# 
# Als eindconclusie voor data-analyse voor het Track3 project zijn we tot de conclusie gekomen dat wanneer er met persoonsgegevens gewerkt moet worden dan is gebruik van een Google API of dergelijke nodig om straatnamen en steden etc eruit te kunnen filteren. Hieronder bevindt zich de code waarin de teksten worden klaargemaakt voor verder processtappen. 

# In[7]:


import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import spacy
import os

stopwoorden = set(stopwords.words('dutch'))
nlp = spacy.load('nl_core_news_lg')

def normalize_numbers(tekst):
    """
    Normalizes numbers in the text, such as phone numbers, zip codes, and house numbers.
    """
    tekst = re.sub(r'(\+31|0)[-\s]*(6-?[\d\s-]{8}|7[\d\s-]{8}|1[\d\s-]{8})', '***', tekst)
    tekst = re.sub(r'\b\d{4}\s*[a-zA-Z]{2}\b', '***', tekst)
    tekst = re.sub(r'\b\d+(?:\s*[a-zA-Z])?\b', '***', tekst)
    return tekst

def converteer_naar_kleine_letters(tekst):
    """
    Converts the text to lowercase.
    """
    return tekst.lower()

def verwijder_niet_alfanumeriek(tekst):
    """
    Removes non-alphanumeric characters from the text.
    """
    gefilterde_tekst = re.sub(r'[^\w\s]', '', tekst)
    return gefilterde_tekst

def verwijder_witruimte(tekst):
    """
    Removes whitespace from the beginning and end of the text.
    """
    return tekst.strip()

def verwijder_stopwoorden(woorden):
    """
    Removes stopwords from the list of words.
    """
    gefilterde_woorden = [woord for woord in woorden if woord.lower() not in stopwoorden]
    return gefilterde_woorden

def tokenize_zin_en_woorden(zin):
    """
    Splits the text into sentences and words.
    """
    zinnen = sent_tokenize(zin)
    woorden = word_tokenize(zin)
    return zinnen, woorden

def lemmatize_tekst(tekst):
    """
    Lemmatizes the text by reducing words to their base form.
    """
    doc = nlp(tekst)
    lemmatized_tokens = [token.lemma_ for token in doc]
    lemmatized_text = " ".join(lemmatized_tokens)
    return lemmatized_text

def tekst_pipeline(tekst):
    """
    Executes a text processing pipeline on the given text, including normalization, conversion to lowercase,
    removal of non-alphanumeric characters, removal of whitespace, tokenization, lemmatization, and removal of stopwords.
    """
    tekst = normalize_numbers(tekst)
    tekst = converteer_naar_kleine_letters(tekst)
    tekst = verwijder_niet_alfanumeriek(tekst)
    tekst = verwijder_witruimte(tekst)
    zinnen, woorden = tokenize_zin_en_woorden(tekst)
    lemmatized_text = lemmatize_tekst(" ".join(woorden))
    words = lemmatized_text.split()
    words = verwijder_stopwoorden(words)
    return words


# Folder path containing the text files
folder_path = 'T3_files'

# List all text files in the folder
txt_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

# Process each text file separately
for txt_file in txt_files:
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()
        tekst = tekst_pipeline(text)
        print(f"Processed text from {txt_file}:")
        print(tekst)
        print("--------------------")


# ### Eindversie Huisrijk
# 
# Als eindconclusie voor data-analyse voor het project Huisrijk kan er geconcludeerd worden dat de code grotendeels goed functioneert, hierbij zijn er uitzonderingen dat sommige woorden niet goed worden goedsplitst. Het ophalen van de bestanden uit de meegegeven database lukte niet, hierdoor raden we aan om het andere amanier op te slaan zoals het gebruiken van andere database(SQL), waardoor je wel makkelijk de bestanden kan ophalen daarvan. 

# In[6]:


import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import spacy
import PyPDF2
import os

stopwoorden = set(stopwords.words('dutch'))
nlp = spacy.load('nl_core_news_sm')

def normalize_numbers(tekst):
    """
    Normaliseert getallen in de tekst, zoals telefoonnummers, postcodes en huisnummers.
    """
    tekst = re.sub(r'(\+31|0)[-\s]*(6-?[\d\s-]{8}|7[\d\s-]{8}|1[\d\s-]{8})', '***', tekst)
    tekst = re.sub(r'\b\d{4}\s*[a-zA-Z]{2}\b', '***', tekst)
    tekst = re.sub(r'\b\d+(?:\s*[a-zA-Z])?\b', '***', tekst)
    return tekst

def converteer_naar_kleine_letters(tekst):
    """
    Converteert de tekst naar kleine letters.
    """
    return tekst.lower()

def verwijder_niet_alfanumeriek(tekst):
    """
    Verwijdert niet-alfanumerieke tekens uit de tekst.
    """
    gefilterde_tekst = re.sub(r'[^\w\s]', '', tekst)
    return gefilterde_tekst

def verwijder_witruimte(tekst):
    """
    Verwijdert witruimte aan het begin en einde van de tekst.
    """
    return tekst.strip()

def verwijder_stopwoorden(woorden):
    """
    Verwijdert stopwoorden uit de lijst van woorden.
    """
    gefilterde_woorden = [woord for woord in woorden if woord.lower() not in stopwoorden]
    return gefilterde_woorden

def tokenize_zin_en_woorden(zin):
    """
    Splitst de tekst op in zinnen en woorden.
    """
    zinnen = sent_tokenize(zin)
    woorden = word_tokenize(zin)
    return zinnen, woorden

def lemmatize_tekst(tekst):
    """
    Lemmatiseert de tekst door de woorden terug te brengen naar hun basisvorm.
    """
    doc = nlp(tekst)
    lemmatized_tokens = [token.lemma_ for token in doc]
    lemmatized_text = " ".join(lemmatized_tokens)
    return lemmatized_text

def tekst_pipeline(tekst):
    """
    Voert een tekstverwerkingspipeline uit op de gegeven tekst, inclusief het normaliseren, converteren naar kleine letters,
    verwijderen van niet-alfanumerieke tekens, verwijderen van witruimte, tokenizen, lemmatiseren en verwijderen van stopwoorden.
    """
    tekst = normalize_numbers(tekst)
    tekst = converteer_naar_kleine_letters(tekst)
    tekst = verwijder_niet_alfanumeriek(tekst)
    tekst = verwijder_witruimte(tekst)
    zinnen, woorden = tokenize_zin_en_woorden(tekst)
    lemmatized_text = lemmatize_tekst(" ".join(woorden))
    words = lemmatized_text.split()
    words = verwijder_stopwoorden(words)
    return words

def extract_text_from_pdf(file_path):
    """
    Extraheert tekst uit het PDF-bestand op het opgegeven bestandspad.
    """
    text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


def read_pdfs(path)
    # Folder path containing the PDF files
    folder_path = 'PDF Bestanden'

    # List all PDF files in the folder
    pdf_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.pdf')]

    # Process each PDF file separately
    for pdf_file in pdf_files:
        extracted_text = extract_text_from_pdf(pdf_file)
        tekst = tekst_pipeline(extracted_text)
        print(f"Processed text from {pdf_file}:")
        print(tekst)
        print("--------------------")

