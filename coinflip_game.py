import random

#creating  a  class
class CoinFlipGame:
    def __init__(self):
        self.client_guesses = []
        self.flip_results = []

    def guess_flips(self, flips):
        if len(flips) != 10:
            return "you have exactly 10 guesses  to  win ."

        self.client_guesses = flips
        return "Guesses submitted successfully......"

    def provide_flip_results(self):
        if not self.client_guesses:
            return "User guesses are missing. Please submit guesses first."

        self.flip_results = [random.choice([0, 1]) for _ in range(10)]

        correct_guesses = sum(1 for guess, result in zip(self.client_guesses, self.flip_results) if guess == result)
        if correct_guesses == 10:
            return "Congratulations!! You've guessed all flips correctly and been  declare the winner!!"
        else:
            return f"Sorry, you've guessed {correct_guesses} flips correctly out of 10."


# Example usage
game = CoinFlipGame()
user_guesses = [0, 1, 0, 0, 0, 1, 1, 0, 1, 0]
print(game.guess_flips(user_guesses))
print(game.provide_flip_results())
