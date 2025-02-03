#Magic8Ball.py
#Name: Aurora Gunubu  
#Date: 2/3/25
#Assignment: Lab #2

#We will need random for this program, import to use this package.
import random

def main():
  print("Magic 8 Ball")

  #Prompt the user for their question.
  question = input("Ask a question\n")
  #List of possible answers. 
  answers = [
    "As I see it, yes", "Ask again later", "Better not tell you now", "Cannot predict now", 
    "Concentrate and ask again", "Don't count on it", "It is certain", "It is decidely so", "Most likely", 
    "My sources say no", "Outlook not so good", "Outlook good", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes", "Yes - definitely"
  ]

  #Answer question randomly with one of the options from your earlier list.

  r = random.randint(0, len(answers) - 1)

  response = answers[r]
  print(response)


if __name__ == '__main__':
  main()
