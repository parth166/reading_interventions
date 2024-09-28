# Micro-Intervention Codebase
This repository contains the code for generating micro-interventions aimed at improving students' reading skills. The interventions are designed to target specific words in a passage and offer tailored support based on the student's profile.

# Project Overview
The project utilizes generative AI to create dynamic and adaptable word-level interventions for students. By analyzing the student's profile and the context of the passage, the system produces tailored support for word pronunciation, contextual understanding, and more. This helps students overcome specific reading challenges, making the learning experience more personalized and effective.

# Project Structure
The repository is organized into different directories and files for efficient management:

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
	├── read_interventions.py # File to view and extract intervention content for downstream pipeline	
	└── requirements.txt            # List of dependencies for the project
    └── generate_interventions.sh   # File to simulate interventions


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

	bash generate_interventions.sh

This script supports 2 functions

1. Static interventions
    - Make sure to set static variable in the arguments.
    - Replace write path with your destination folder path (the script will create a folder in the path you mention if it does not exist).
    - Replace with word and context accordingly.
2. Dynamic interventions
    - Remove the static argument.
    - Change the write path.

### To read the saved interventions

	python read_interventions.py

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

# Intervention Design Motivation

## Interventions implemented 
1. intervention by rhyming words: Hearing rhyming words for a given word can help the students understand tail sounds Example: Ping, Sing, Sling etc. (helps in pronunciation)
2. Synthetically create Stories: Having an engaging story using the given word makes the students retain the words better. (helps in retention and comprehension)

## Considerations for interventions
1. Intervention should be broadly applicable to a lot of words (Generalisable). There can be very unique and creative interventions but scalable and simple interventions are the best for a quick MVP.
2. Dynamic interventions are extremely important as compared to static interventions as they cover numerous cases like:
	- Context dependent pronunciation (Past tense pronunciation of "read" is "RED" and present tense pronunciation is "REED")
	- Cultural impact of pronunciation is extremely important (American English has different pronunciations when compared to British English, hence such information should be incorporated while designing interventions).
3. Intervention object  should be unique for every student.
4. Student preference is modelled inside the student object but intervention object contains both (story based) and (rhyming based) interventions (can be extended to more in the future). Hence, each word can be presented in multiple ways to the student (motivation: Having more data and not needing it is better than having no data and needing it).

## Pipeline Design Approach
1. Brainstorming different ideas for intervention and discussing drawbacks and strengths for each. This includes first identifying levels of intervention (at word level and at student level), followed by research on different components at word level intervention grounded on student and nearby context)
2. Building an MVP (minimum viable product) by shortlisting easier to implement but effective interventions. 
3. Designing a class structure and making sure there are no redundancies or cyclic dependencies in the pipeline design.
4. Making additional placeholders in classes to store more data and allow for future interventions.
5. Trying to use hashed values (at a very surface level) to give a sense of privacy while storing student specific intervention as we are storing complete data ~ can be improved.

# Future Enhancements

Dynamic Intervention Strategies:

1. Personalized Learning Paths: Create a system that adapts the intervention style based on student preferences and progress over time (information can be extracted for every student from the student object)
2. Support for Multilingual Interventions: Extend support for students from different language backgrounds with tailored multilingual interventions.
3. Prompt caching (to avoid using multiple gpt calls).
4. Analytics on student's performance. (LLM driven/expert interventions)