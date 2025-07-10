import json
import random

class ClassJson():
    def __init__(self, name_file_json):
        # Store the name of the JSON file containing the questions
        self.name_file_json = name_file_json
    
    def getNameFileJSON(self):
        # Return the JSON file name
        return self.name_file_json

    def read_file_JSON(self):
        # Open and parse the JSON file
        with open(self.name_file_json, 'r') as file:
            data = json.load(file)
        return data

    def return_easy(self):
        # Lists to store the selected questions and answers for easy difficulty
        lista_domande_easy = []
        lista_risposte_easy = []
        # Load all easy questions
        data_easy = self.read_file_JSON()["easy"]
        # Shuffle the questions randomly
        random.shuffle(data_easy)
        # Select the first 5 questions after shuffling
        selected_questions = data_easy[:5]
        # Build the lists of questions and answers
        for elemento in selected_questions:
            lista_domande_easy.append(elemento["question"])
            lista_risposte_easy.append(elemento["answer"])
        return lista_domande_easy, lista_risposte_easy

    def return_medium(self):
        # Lists to store the selected questions and answers for medium difficulty
        lista_domande_medium = []
        lista_risposte_medium = []
        # Load all medium questions
        data_medium = self.read_file_JSON()["medium"]
        # Shuffle the questions randomly
        random.shuffle(data_medium)
        # Select the first 5 questions after shuffling
        selected_questions = data_medium[:5]
        # Build the lists of questions and answers
        for elemento in selected_questions:
            lista_domande_medium.append(elemento["question"])
            lista_risposte_medium.append(elemento["answer"])
        return lista_domande_medium, lista_risposte_medium

    def return_hard(self):
        # Lists to store the selected questions and answers for hard difficulty
        lista_domande_hard = []
        lista_risposte_hard = []
        # Load all hard questions
        data_hard = self.read_file_JSON()["hard"]
        # Shuffle the questions randomly
        random.shuffle(data_hard)
        # Select the first 5 questions after shuffling
        selected_questions = data_hard[:5]
        # Build the lists of questions and answers
        for elemento in selected_questions:
            lista_domande_hard.append(elemento["question"])
            lista_risposte_hard.append(elemento["answer"])
        return lista_domande_hard, lista_risposte_hard
