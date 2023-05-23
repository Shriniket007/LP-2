import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["hello %1, my name is jarvis"]
    ],
    [
        r"hi|hello|hola",
        ["hello how are you?"]
    ],
    [
        r"(.*) (city|location)",
        ["i live in pune"]
    ],
    [
        r"how is the weather in (.*)",
        ["it is cold in %1", "it is hot in %1", "weather is awesome in %1"]
    ],
    [
        r"(.*) sportsperson",
        ["my %1 sportsperson is messi"]
    ],
    [
        r"quit",
        ["thank you"]
    ]
]


def chat():
    print("hey there jarvis at your service")
    chat = Chat(pairs, reflections)
    chat.converse()
    
if __name__ == "__main__": 
    chat()