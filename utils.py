import json

from classes.student import Student
from classes.word import Word
from classes.intervention import Intervention
from gpt import call_model

def extract_phrases(file_path):
    phrases = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            if ". " in line:
                index, phrase = line.split(". ", 1)
                index = int(index.strip())
                phrases[index] = phrase.strip()
    
    return phrases

def get_students(file_path):
    students = json.load(open(file_path)) # the last 2 students are from 
    student_objects = {}
    
    for student in students:
        obj = Student(**student)
        student_objects[obj.get_hash_id()] = obj

    return student_objects

def get_word_object(word, phrase, config):
    prompt = open("./intervention_components/template.txt", "r").read()
    prompt = prompt.replace("{{word}}", word).replace("{{context}}", phrase)

    expected_keywords = ["meaning", "synonyms", "antonyms", "pronunciation_american", "pronunciation_british", "rhyming_words", "story"]

    response = call_model(prompt, config, expected_keywords)
    
    word_obj = None
    try:
        # word_obj = Word(word, phrase, response["pronunciation_american"], response["pronunciation_british"], response["meaning"], response["synonyms"], response["antonyms"], response["r"])
        word_obj = Word(word, phrase, **response)
    except:
        print("Could not fetch details for the word", word)

    return word_obj

def get_intervention(word, phrase, student_obj, config):
    """
        This is a wrapper function to get a word level intervention for a given student
        
        Args: 
            - word : str (word dor which we need to obtain an intervention)
            - phrase: str (context in which the word appears)
            - student: object (student type object containing student's details)
            - config: llm generation config

        Returns:
            - intervention object
    """
    word_obj = get_word_object(word, phrase, config)

    intervention_obj = Intervention(word_obj, student_obj)

    return intervention_obj

def main():
    phrases = extract_phrases("./dataset/passage.txt")

if __name__ == "__main__":
    main()