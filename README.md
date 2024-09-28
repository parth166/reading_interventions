# Micro-Intervention Codebase
This repository contains the code for generating micro-interventions aimed at improving students' reading skills. The interventions are designed to target specific words in a passage and offer tailored support based on the student's profile.

# Project Overview
The project utilizes generative AI to create dynamic and adaptable word-level interventions for students. By analyzing the student's profile and the context of the passage, the system produces tailored support for word pronunciation, contextual understanding, and more. This helps students overcome specific reading challenges, making the learning experience more personalized and effective.

# Project Structure
The repository is organized into different directories and files for efficient management:

├── classes
micro-intervention/
├── classes/                    # Contains class definitions
│   ├── intervention.py         # Defines the Intervention class for intervention data
│   ├── student.py              # Defines the Student class for a student profile
│   └── word.py                 # Defines the Word class and its properties
├── dataset/                    # Contains the dataset files used for intervention creation
│   ├── passage.txt             # List of passages used in the study
│   ├── students.json           # Sample synthetic student data
│   └── words.csv               # Extracted set of words from the passage
├── intervention_components/    # Contains prompt templates and components
│   ├── template.txt            # Prompt template for the generative AI model
│   └── emotional_tones.txt     # Template for generating emotional tone-based variations
├── gpt.py                      # Wrapper for OpenAI API integration
├── main.py                     # Main script to create interventions for students
├── utils.py                    # Helper functions for data extraction and intervention generation
└── requirements.txt            # List of dependencies for the project


# Installation and Setup

## To run the project, follow these steps:

Clone the Repository

1. git clone https://github.com/parth166/reading_interventions.git
2. cd into the directory

## Install Dependencies:

Use the requirements.txt file to install the necessary libraries

pip install -r requirements.txt

## Set Up Environment Variables:

Make sure to set the OPENAI_API_KEY in your environment variables

export OPENAI_API_KEY='your_openai_api_key'

# How to Run the Project

## Run the Main Script:

### To generate interventions for students:

python main.py

This script will:
Load student data from students.json.
Extract phrases from the given passage (passage.txt).
Use the defined generative AI model to create interventions for each student based on the context of the passage and the student’s profile.

Understanding main.py:

The core logic in main.py is responsible for creating and saving interventions for each student:

def create_interventions(phrases, students):
    llm_config = json.load(open("llm_config.json"))

    with open("interventions.jsonl", "a") as f:
        for student in students:
            for phrase in tqdm(phrases):
                for word in phrase.split(" "):
                    intervention = get_word_intervention(word, phrase, student, llm_config)
                    json.dump(intervention, f)
                    f.write("\n")

Interventions are saved in the interventions.jsonl file in JSON format.

## Key Components
1. Student Class (student.py):

The Student class stores information about individual students, such as their name, age, grade, school, and country. It also tracks each student's vocabulary and learning quirks, making it easier to design targeted interventions.

2. Intervention Class (intervention.py):

The Intervention class defines the structure of each word-level intervention, storing details like word meaning, synonyms, antonyms, pronunciation guide, and personalized story prompts.

3. LLM Integration (gpt.py):

The script interacts with OpenAI's API using a wrapper function. It sends customized prompts to the model and parses the responses to ensure relevant content is generated.

4. Helper Functions (utils.py):

Utility functions for data extraction, such as:
- extract_phrases(file_path): Extracts phrases from a given text file.
- get_students(file_path): Creates Student objects from the student data file.
- get_word_intervention(...): Generates word-specific interventions using LLM.

## Data Files and Templates
Passage File (dataset/passage.txt): Contains a list of passages for intervention study.

Student Profiles (dataset/students.json): Synthetic student data for testing and evaluation.

Prompt Templates (intervention_components/):
- template.txt: Template prompt for the generative AI model.
- emotional_tones.txt: List of emotional tones for generating context-sensitive pronunciation.

# Interventions implemented: 
1. intervention by rhyming words: Hearing rhyming words for a given word can help the students understand tail sounds Example: Ping, Sing, Sling etc. (helps in pronunciation)
2. Stories: Having an engaging story using the given word makes the students retain the words better. (helps in retention and comprehension)

# Intervention Design Motivation

Dynamic interventions are extremely important as compared to static interventions as they cover numerous cases like:
- Context dependent pronunciation (Past tense pronunciation of "read" is "RED" and present tense pronunciation is "REED")
- Cultural impact of pronunciation is extremely important (American English has different pronunciations when compared to British English, hence such information should be incorporated while designing interventions).
- Intervention object is unique for every student for a given phrase as both the "phrase" and "region" are used.
- Student preference is modelled inside the student object but intervention object contains both (story based) and (rhyming based) interventions. Hence, each word can be presented in multiple ways to the student. (idea: Having more data and not needing it is better than having no data and needing it).

# Future Enhancements

Dynamic Intervention Strategies:

1. Develop more dynamic and adaptable intervention strategies based on real-time student performance data (Information can be extracted from student.py)
2. Personalized Learning Paths: Create a system that adapts the intervention style based on student preferences and progress over time.
3. Support for Multilingual Interventions: Extend support for students from different language backgrounds with tailored multilingual interventions.
4. Prompt caching (to avoid using multiple gpt calls).
5. Analytics on student's performance. (LLM driven/expert interventions)


