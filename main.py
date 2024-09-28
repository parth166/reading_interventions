import json
import os
import random
import pickle

from tqdm import tqdm
from utils import extract_phrases, get_students, get_intervention

def create_interventions(phrases, students, write_path):
    """
        ideal case would be of dynamic intervention ~ student specific interventions
        but if static interventions are enabled. We can try 
    """

    llm_config = json.load(open("llm_config.json"))

    for student in students:
        for phrase in tqdm(phrases):
            for word in phrase.split(" "):
                intervention = get_intervention(word, phrase, student, llm_config)
                with open(os.path.join(write_path, f'{intervention.unique_id}.pkl'), "wb") as file:
                    pickle.dump(intervention, file)

def main():
    """
        The main idea of interventions is that we should have dynamic and adaptable interventions.

        Example:

        1: word pronunciation may differ because of British/American English
        2: A student has shown immense improvements with a specific style of intervention (Ex: story based intervention)
        3: Also, using phrases instead of working at individual word level to incorporate for in-context word meaning.
           [read (reed) vs read (red)]
    """

    random.seed(42)

    phrases = random.sample(list(extract_phrases("./dataset/passage.txt").values()), 1)
    students = get_students("./dataset/students.json")

    write_path = f'./generated_interventions/'
    os.makedirs(write_path, exist_ok=True)

    create_interventions(phrases, students.values(), write_path)

if __name__ == "__main__":
    main()
    