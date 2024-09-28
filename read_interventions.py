import pickle
import os

def main():
    files = []
    for (dirpath, dirnames, filenames) in os.walk("./generated_interventions"):
        files.extend(filenames)
    
    for f_name in files:
        with open(os.path.join("./generated_interventions", f_name), "rb") as file:
            intervention = pickle.load(file)

            print("Word: ", intervention.word.word)
            print("Intervention type: ", intervention.type)
            print("Word meaning: ", intervention.meaning)
            print(intervention.rhyming_words)
            print("Story related to word: ", intervention.story)
            print("Pronunciation: ", intervention.pronunciation)
            print("Id: ", intervention.unique_id)
            break

if __name__ == "__main__":
    main()