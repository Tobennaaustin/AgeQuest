# Define the list of questions and answers
questions = [
  {
    "question": "Which of these technologies did you use the most during your childhood?",
    "answers": [
      { "text": "Dial-up Internet 😑", "score": 10 },
      { "text": "CDs and DVDs", "score": 20 },
      { "text": "USB flash drives", "score": 30 },
      { "text": "Cloud storage", "score": 40 }
    ]
  },
  {
    "question": "Which of these video game consoles do you remember playing?",
    "answers": [
      { "text": "Atari 2600 or NES", "score": 10 },
      { "text": "Sega Genesis or PlayStation 1", "score": 20 },
      { "text": "PlayStation 2 or Xbox", "score": 30 },
      { "text": "PlayStation 5 or Nintendo Switch", "score": 40 }
    ]
  },
  {
    "question": "How did you first listen to music on the go?",
    "answers": [
      { "text": "Cassette Walkman", "score": 10 },
      { "text": "CD Discman", "score": 20 },
      { "text": "MP3 player or iPod", "score": 30 },
      { "text": "Streaming on a spotify", "score": 40 }
    ]
  },
  {
    "question": "Which of these cartoons or kids' shows did you grow up watching?",
    "answers": [
      { "text": "The Jetsons or Scooby-Doo", "score": 10 },
      { "text": "DuckTales or Teenage Mutant Ninja Turtles", "score": 20 },
      { "text": "Pokémon or Dragon Ball Z", "score": 30 },
      { "text": "Adventure Time or The Amazing World of Gumball", "score": 40 }
    ]
  },
  {
    "question": "Which of these social media platforms did you start using first?",
    "answers": [
      { "text": "MySpace", "score": 10 },
      { "text": "Facebook", "score": 20 },
      { "text": "Instagram", "score": 30 },
      { "text": "TikTok", "score": 40 }
    ]
  },
  {
    "question": "How did you first communicate with friends online?",
    "answers": [
      { "text": "Bulletin board systems (BBS) or AOL", "score": 10 },
      { "text": "MSN Messenger or Yahoo! Messenger", "score": 20 },
      { "text": "Facebook Chat or BBM", "score": 30 },
      { "text": "WhatsApp or Snapchat", "score": 40 }
    ]
  },
  {
    "question": "Which movie or TV series defined your teenage years?",
    "answers": [
      { "text": "Star Wars (Original Trilogy) or Knight Rider", "score": 10 },
      { "text": "Friends or The Matrix", "score": 20 },
      { "text": "Harry Potter or Twilight", "score": 30 },
      { "text": "Stranger Things or The Hunger Games", "score": 40 }
    ]
  },
  {
    "question": "How did you usually rent or buy movies in your teens?",
    "answers": [
      { "text": "VHS tapes from Blockbuster", "score": 10 },
      { "text": "DVDs from local rental stores", "score": 20 },
      { "text": "Blu-rays or Netflix DVDs by mail", "score": 30 },
      { "text": "Streaming on Netflix or other services", "score": 40 }
    ]
  },
  {
    "question": "Which of these devices do you remember using first?",
    "answers": [
      { "text": "Typewriter or early home computer (Commodore, etc.)", "score": 10 },
      { "text": "Desktop PC with Windows 95/98", "score": 20 },
      { "text": "Laptop with Windows XP/Vista", "score": 30 },
      { "text": "Smartphone or tablet", "score": 40 }
    ]
  },
  {
    "question": "Which significant event do you remember most clearly?",
    "answers": [
      { "text": "Moon landing or Watergate", "score": 10 },
      { "text": "The fall of the Berlin Wall or Y2K", "score": 20 },
      { "text": "9/11 or the launch of Facebook", "score": 30 },
      { "text": "The rise of social media or the COVID-19 pandemic", "score": 40 }
    ]
  }
]



# Function to ask questions and calculate the score
def ask_questions(questions):
    total_score = 0

    for index, q in enumerate(questions):
        print(f"\n{index + 1}. {q['question']}")
        for i, ans in enumerate(q['answers']):
            print(f"   {i + 1}. {ans['text']}")

        # Get user input and validate it
        while True:
            try:
                user_choice = int(input("Select an option (1-4): "))
                if 1 <= user_choice <= 4:
                    break
                else:
                    print("Please select a valid option (1-4).")
            except ValueError:
                print("Please enter a number between 1 and 4.")

        total_score += q['answers'][user_choice - 1]['score']

    return total_score

# Function to estimate age based on score
def estimate_age(total_score):
    if total_score <= 100:
        return "60+ years old"
    elif total_score >= 200:
        return "40-59 years old"
    elif total_score >= 300:
        return "20-30 years old"
    elif total_score >= 400:
        return "10-19 years"
    else:
        return "Omo I no sabi your age oo"

# Main function to run the quiz
def main():
    print("Welcome to AgeQuest! Let's estimate your age based on your experiences.")
    total_score = ask_questions(questions)
    estimated_age = estimate_age(total_score)
    print("\nGuessing your age...\n")
    print(f"Your estimated age is: {estimated_age}")

if __name__ == "__main__":
    main()
