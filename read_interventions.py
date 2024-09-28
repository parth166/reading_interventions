import pickle
import os
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='Create Micro-Intervention',
        description='Creates micro-intervention for students.'
    )    

    parser.add_argument("--read_path", required=True, help="Path where the interventions will be saved")

    args = parser.parse_args()
    read_path = args.read_path

    files = []
    for (dirpath, dirnames, filenames) in os.walk(read_path):
        files.extend(filenames)
    
    for f_name in files:
        with open(os.path.join(read_path, f_name), "rb") as file:
            intervention = pickle.load(file)

            print("Word: ", intervention.word.word)
            print("Intervention type: ", intervention.type)
            print("Word meaning: ", intervention.meaning)
            print("Rhyming words: ", intervention.rhyming_words)
            print("Story related to word: ", intervention.story)
            print("Pronunciation: ", intervention.pronunciation)
            print("Id: ", intervention.unique_id)
            break

if __name__ == "__main__":
    main()