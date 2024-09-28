import json
from tqdm import tqdm
import random
from utils import extract_phrases, get_students, get_word_intervention

def create_interventions(phrases, students):
    """
        ideal case would be of dynamic intervention ~ student specific interventions
        but if static interventions are enabled. We can try 
    """

    llm_config = json.load(open("llm_config.json"))

    with open("interventions.jsonl", "a") as f:
        for student in students:
            for phrase in tqdm(phrases):
                for word in phrase.split(" "):
                    intervention = get_word_intervention(word, phrase, student, llm_config)

                    json.dump(intervention, f)
                    f.write("\n")
    
    f.close()

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

    create_interventions(phrases, students.values())

if __name__ == "__main__":
    main()
    