import time
from ClassJson import ClassJson

def calcolo_punteggio_giocatore(lista_risposte_computer, lista_risposte_utente):
    count = 0
    # Iterate over both lists (correct answers and user answers) simultaneously
    for risposta_corretta, risposta_utente in zip(lista_risposte_utente, lista_risposte_computer):
        # Normalize and split the strings into lists of words, then sort and compare
        if sorted(risposta_corretta.lower().split()) == sorted(risposta_utente.lower().split()):
            count += 1

    print("🤯 The score obtained by the user, based on the correct questions, is equal to:", count)

def main():
    # Initialize the custom JSON class to load the questions
    classe_json = ClassJson('question_game.json')
    print("Welcome to my quiz dear user 👻")
    var_bool = True
    while var_bool:
        question_play = input("Do you want to play? ").lower()
        if question_play == "yes" or question_play == "y":
            # Loop until the user inputs a valid difficulty
            while True:
                difficolta_gioco = input("So good, we can start our game! 🧑🏻‍💻 But before I need to set the difficulty (please write easy/medium/hard): ").lower()
                if difficolta_gioco in ["easy", "medium", "hard"]:
                    break
                else:
                    print("Please answer with easy / medium / hard 😡")
            
            var_bool = False
            array_risposte_utente = []

            # Handle EASY difficulty
            if difficolta_gioco == "easy":
                # Retrieve questions and answers for EASY mode
                lista_domande_easy, lista_risposte_easy = classe_json.return_easy()
                for domanda in lista_domande_easy:
                    risposta_utente_easy = input(str(domanda) + " ").lower()
                    array_risposte_utente.append(risposta_utente_easy)

                print()
                print("😎 Congratulations you finished the game EASY, give me a moment to calculate the score...")
                time.sleep(2)
                calcolo_punteggio_giocatore(lista_risposte_easy, array_risposte_utente)

            # Handle MEDIUM difficulty
            elif difficolta_gioco == "medium":
                lista_domande_medium, lista_risposte_medium = classe_json.return_medium()
                for domanda_med in lista_domande_medium:
                    risposta_utente_medium = input(str(domanda_med) + " ").lower()
                    array_risposte_utente.append(risposta_utente_medium)

                print()
                print("😎 Congratulations you finished the game MEDIUM, give me a moment to calculate the score...")
                time.sleep(2)
                calcolo_punteggio_giocatore(lista_risposte_medium, array_risposte_utente)

            # Handle HARD difficulty
            elif difficolta_gioco == "hard":
                lista_domande_hard, lista_risposte_hard = classe_json.return_hard()
                for domanda_hard in lista_domande_hard:
                    risposta_utente_hard = input(str(domanda_hard) + " ").lower()
                    array_risposte_utente.append(risposta_utente_hard)

                print()
                print("😎 Congratulations you finished the game HARD, give me a moment to calculate the score...")
                time.sleep(2)
                calcolo_punteggio_giocatore(lista_risposte_hard, array_risposte_utente)

        # If user decides not to play
        elif question_play == "no" or question_play == "n":
            print("See you soon, I hope you will come back to try my game 🫠")
            quit()
        else:
            # Handle invalid input for starting the game
            print("Please answer with yes/y or no/n 😡")

main()
