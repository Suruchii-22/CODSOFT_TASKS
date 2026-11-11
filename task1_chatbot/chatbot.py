"""Task 1: Rule-based chatbot using regex pattern matching."""
import re
import random
from datetime import datetime

RULES = [
    (r"\b(hi|hello|hey|namaste)\b",
     ["Hello! How can I help you today?", "Hey there! What can I do for you?"]),
    (r"how are you|how's it going",
     ["I'm just code, but I'm running great! How about you?"]),
    (r"(what('s| is) your name|who are you)",
     ["I'm CodBot, a rule-based chatbot built for the CodSoft AI internship."]),
    (r"my name is (\w+)",
     ["Nice to meet you, {0}!"]),
    (r"\b(time)\b",
     [lambda: "The time is " + datetime.now().strftime("%I:%M %p") + "."]),
    (r"\b(date|today)\b",
     [lambda: "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."]),
    (r"\b(joke)\b",
     ["Why do programmers prefer dark mode? Because light attracts bugs!",
      "There are 10 kinds of people: those who understand binary and those who don't."]),
    (r"\b(help|what can you do)\b",
     ["I can chat, tell the time/date, tell jokes, and remember your name. Type 'bye' to exit."]),
    (r"\b(thanks|thank you)\b",
     ["You're welcome!", "Happy to help!"]),
    (r"\b(bye|goodbye|exit|quit)\b",
     ["Goodbye! Have a great day!"]),
]
FALLBACK = ["Sorry, I didn't get that. Type 'help' to see what I can do.",
            "Hmm, I don't know that one yet. Try asking for a joke or the time!"]


def respond(text: str) -> str:
    text = text.lower().strip()
    for pattern, replies in RULES:
        m = re.search(pattern, text)
        if m:
            reply = random.choice(replies)
            if callable(reply):
                return reply()
            if "{0}" in reply:
                return reply.format(m.group(1).capitalize())
            return reply
    return random.choice(FALLBACK)


def main():
    print("CodBot: Hi! Type 'help' for options, 'bye' to quit.")
    while True:
        user = input("You: ")
        print("CodBot:", respond(user))
        if re.search(r"\b(bye|goodbye|exit|quit)\b", user.lower()):
            break


if __name__ == "__main__":
    main()
