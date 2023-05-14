import openai
import random

# Set up OpenAI API credentials
openai.api_key = "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"


class ChatBot:
    def __init__(self):
        self.prev_inputs = []

    def get_response(self, prompt):
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.7
            ).choices[0].text.strip()
            if response in self.prev_inputs:
                response = self.get_response(prompt)
            else:
                self.prev_inputs.append(response)
        except Exception as e:
            print("Error:", e)
            response = "Sorry, I couldn't generate a response."
        return response


# Define functions for generating jokes and trivia
def get_joke():
    prompt = "Tell me a joke."
    return chatbot.get_response(prompt)


def get_trivia():
    categories = ["history", "science", "geography", "pop culture"]
    category = random.choice(categories)
    prompt = f"Give me a trivia fact about {category}."
    return chatbot.get_response(prompt)


# Set up chatbot instance
chatbot = ChatBot()


# Define main loop
def main():
    while True:
        user_input = input("Say something: ")
        if user_input.lower() == "quit":
            break
        elif user_input.lower() in ["tell me a joke", "give me a joke", "joke"]:
            response = get_joke()
        elif user_input.lower() in ["give me trivia", "tell me trivia", "trivia"]:
            response = get_trivia()
        else:
            response = chatbot.get_response(user_input)
        print(response)


if __name__ == "__main__":
    main()
