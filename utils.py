import json

from classes.student import Student
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

def get_word_intervention(word, phrase, student, config):
    """
        This is a wrapper function to get a word level intervention for a given student
        
        Args: 
            - word : str (word dor which we need to obtain an intervention)
            - phrase: str (context in which the word appears)
            - student: object (student type object containing student's details)

        Returns:
            - intervention object
    """
    accent = "American"
    if student.country == "UK":
        accent = "British"
    
    prompt = open("./intervention_components/template.txt", "r").read()
    prompt = prompt.replace("{{word}}", word).replace("{{context}}", phrase).replace("{{accent}}", accent)

    expected_keywords = ["meaning", "synonyms", "antonyms", "pronunciation", "story"]

    response = call_model(prompt, config, expected_keywords)

    intervention_obj = Intervention(word, response["meaning"], response["synonyms"], response["antonyms"], student.prefers)
    intervention_obj.set_pronunciation_attributes(response["pronunciation"], "American" if student.country == "America" else "British")
    intervention_obj.set_story(response["story"])

    return intervention_obj.to_json()

def main():
    phrases = extract_phrases("./dataset/passage.txt")

if __name__ == "__main__":
    main()