import hashlib

class Word:
    def __init__(self, word, phrase, pronunciation_american, pronunciation_british, meaning, synonyms, antonyms, rhyming_words, story):
        """
            A word class that captures different aspects of a word.
            Every word will have a context dependent word hash.
        """
        self.word = word
        self.meaning = meaning
        self.pronunciation_american = pronunciation_american # dictionary object because of region specific word intervention (American/British English)
        self.pronunciation_british = pronunciation_british
        self.context_sentences = []
        self.synonyms = synonyms
        self.antonyms = antonyms
        self.rhyming_words = rhyming_words
        self.story = story
        self.phrase = phrase
        self.word_hash = self.set_word_hash()

    def set_word_hash(self):
        hash_object = hashlib.sha256((self.word + ": " + self.phrase).encode())
        hex_digest = hash_object.hexdigest()
        return hex_digest
    
    def get_word_hash(self):
        return self.word_hash

    
    
        