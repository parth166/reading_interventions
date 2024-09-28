class Word:
    def __init__(self, word, meaning):
        """
            A word class that captures different aspects of a word.

            Assumption is english language based intervention
        """
        self.word = word
        self.meaning = meaning
        self.pronunciation = {} # dictionary object because of region specific word intervention (American/British English)
        self.context_sentences = []
        self.synonyms = set()
        self.antonyms = set()
        self.rhyming_words = set()
        self.story = ""
        