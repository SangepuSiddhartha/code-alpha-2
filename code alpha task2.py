import nltk
from nltk.chat.util import Chat, reflections

# Ensure required NLTK resources are downloaded
nltk.download('punkt')

# Define pairs of questions and responses
faq_pairs = [
    (r'What is the product?', 'Our product is an advanced AI-powered chatbot that helps you with FAQs.'),
    (r'How does the product work?', 'The product uses natural language processing to understand and generate responses to your queries.'),
    (r'What are the features of the product?', 'Our product includes features like real-time responses, personalized interactions, and continuous learning capabilities.'),
    (r'How can I contact support?', 'You can contact our support team via email at support@example.com or call us at (123) 456-7890.'),
    (r'What is the price of the product?', 'The price depends on the package you choose. Please visit our website for detailed pricing information.'),
    (r'Can I get a demo?', 'Yes, we offer a free demo. Please visit our website to schedule one.')
]

# Create a chatbot instance
chatbot = Chat(faq_pairs, reflections)

def chatbot_response(user_input):
    return chatbot.respond(user_input)

# Main function to interact with the chatbot
def main():
    print("Hello! I'm here to answer your questions about our product. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
