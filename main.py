import argparse
import json
import os
import random
import pickle

from tqdm import tqdm
from utils import extract_phrases, get_students, get_intervention

def create_interventions(write_path, conf):
    """
        ideal case would be of dynamic intervention ~ student specific interventions
        but if static interventions are enabled.
    """
    phrases = random.sample(list(extract_phrases("./dataset/passage.txt").values()), 1)
    students = get_students("./dataset/students.json").values()

    for student in students:
        for phrase in tqdm(phrases):
            for word in phrase.split(" "):
                intervention = get_intervention(word, phrase, conf, student)
                with open(os.path.join(write_path, f'{intervention.unique_id}.pkl'), "wb") as file:
                    pickle.dump(intervention, file)

def create_word_level_intervention(word, phrase, write_path, conf):
    print(write_path)
    intervention = get_intervention(word, phrase, conf)
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

    # Create the argument parser
    parser = argparse.ArgumentParser(
        prog='Create Micro-Intervention',
        description='Creates micro-intervention for students.'
    )    

    parser.add_argument("--write_path", required=True, help="Path where the interventions will be saved")
    parser.add_argument("--llm_conf_path", required=True, help="Path to the LLM configuration file")
    parser.add_argument("--word", default="", help="Optional word for specific intervention (default: empty string)")
    parser.add_argument("--context", default="", help="Optional context for the word (default: empty string)")
    parser.add_argument("--static", default=False, help="Optional flag to indicate if the intervention should be static (default: False)")

    args = parser.parse_args()

    is_static = args.static
    write_path = args.write_path
    llm_config = args.llm_conf_path
    word = args.word
    phrase = args.context

    llm_config = json.load(open(llm_config))

    os.makedirs(write_path, exist_ok=True)

    if is_static:
        create_word_level_intervention(word, phrase, write_path, llm_config)
    else:
        create_interventions(write_path, llm_config)
    
if __name__ == "__main__":
    main()
    