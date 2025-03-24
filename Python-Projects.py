#----------------Project 1----------------

# print("Hello, World!")

#----------------Project 2----------------

# first_number = float(input("Enter the first number: "))
# operation = input("Enter operation (+, -, *, /): ")
# second_number = float(input("Enter the second number: "))
# result=None

# if operation=="+":
#     result=first_number+second_number
# elif operation=="-":
#     result=first_number-second_number
# elif operation=="*":
#     result=first_number*second_number
# elif operation == '/':
#     if second_number!=0:
#         result=first_number/second_number
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Error: Invalid operation.")
    
# if result is not None:
#     print(f"Result: {result}")
    
#----------------Project 3----------------

# import random

# secret_number = random.randint(1, 100)

# guess = None

# while guess != secret_number:
#     guess = int(input("Enter your guess: "))

#     if guess < secret_number:
#         print("Too low! Try again.")
#     elif guess > secret_number:
#         print("Too high! Try again.")
#     else:
#         print("Correct! You guessed the number.")

#----------------Project 4----------------

# class ToDoList:
#     def __init__(self):
#         self.tasks=[]
    
#     def display_menu(self):
#         print("\n1. Add Task")
#         print("2. Edit Task")
#         print("3. Delete Task")
#         print("4. Exit")
        
#     def add_task(self):
#         task=input("Enter task: ")
#         self.tasks.append(task)
#         print("Task added successfully.")
        
#     def edit_task(self):
#         if self.tasks:
#             self.display_tasks()
#             try:
#                 task_index = int(input("Enter task index to edit: ")) - 1
#                 if 0 <= task_index < len(self.tasks):
#                     new_task = input("Enter new task: ")
#                     self.tasks[task_index] = new_task
#                     print("Task edited successfully.")
#                 else:
#                     print("Invalid index.")
#             except ValueError:
#                 print("Please enter a valid number.")
#         else:
#             print("No tasks available to edit.")
            
#     def delete_task(self):
#         if self.tasks:
#             self.display_tasks()
#             try:
#                 task_index = int(input("Enter task index to delete: ")) - 1
#                 if 0 <= task_index < len(self.tasks):
#                     self.tasks.pop(task_index)
#                     print("Task deleted successfully.")
#                 else:
#                     print("Invalid index.")
#             except ValueError:
#                 print("Please enter a valid number.")
#         else:
#             print("No tasks available to delete.")
    
#     def display_tasks(self):
#         for index, task in enumerate(self.tasks):
#             print(f"{index + 1}. {task}")
            
#     def run(self):
#         while True:
#             self.display_menu()
#             choice = input("Select an option: ")

#             if choice == '1':
#                 self.add_task()
#             elif choice == '2':
#                 self.edit_task()
#             elif choice == '3':
#                 self.delete_task()
#             elif choice == '4':
#                 print("Exiting the application. Goodbye!")
#                 break
#             else:
#                 print("Invalid choice. Please select a valid option.")

# todo_list = ToDoList()
# todo_list.run()


#----------------Project 5----------------

# import random

# class Dice:
#     def __init__(self,sides=6):
#         self.sides=sides
        
#     def roll(self):
#         return random.randint(1,self.sides)
    
# dice=Dice()
# result=dice.roll()

# print(f"The dice were rolled: {result}")

#----------------Project 6----------------

# class TemperatureConverter:
    
#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit-32)*5/9
    
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9 / 5) + 32
            
#     def convert_temperature(self):
#         temperature = float(input("Enter temperature: "))
#         conversion_type = input("Select a conversion type (1 for Fahrenheit to Celsius, 2 for Celsius to Fahrenheit): ")
        
#         if conversion_type == '1':
#             converted_temperature = self.fahrenheit_to_celsius(temperature)
#             print(f"Converted temperature: {converted_temperature:.1f}°C")
#         elif conversion_type == '2':
#             converted_temperature = self.celsius_to_fahrenheit(temperature)
#             print(f"Converted temperature: {converted_temperature:.1f}°F")
#         else:
#             print("Invalid selection. Please choose 1 or 2.")

# converter = TemperatureConverter()
# converter.convert_temperature()    

#----------------Project 7----------------

# import time
# from datetime import datetime

# def get_current_time():
#     return datetime.now().strftime("%I:%M %p")

# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}. Waiting...")
    
#     while True:
#         current_time = get_current_time()
        
#         if current_time == alarm_time:
#             print(f"Alarm! It's {alarm_time}. Time to wake up!")
#             break
        
#         time.sleep(60)

# alarm_time = input("Set alarm time (e.g., 07:30 AM): ")
# set_alarm(alarm_time)

#----------------Project 8----------------

# import secrets
# import string

# def generate_secure_password(length):
#     all_characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(secrets.choice(all_characters) for _ in range(length))
#     return password

# password_length = int(input("Enter the desired password length: "))
# generated_password = generate_secure_password(password_length)
# print(f"Generated password: {generated_password}")

#----------------Project 9---------------

# class AdventureGame:
#     def __init__(self):
#         print("Welcome to the Adventure Game!")
#         print("You find yourself at a crossroads in a dense forest.")

#     def start(self):
#         print("1. Enter the dark cave.")
#         print("2. Follow the path through the forest.")
#         choice1 = input("What do you want to do? (1 or 2): ")
#         self.first_choice(choice1)
        
#     def first_choice(self, choice):
#         if choice == '1':
#             self.enter_cave()
#         elif choice == '2':
#             self.follow_path()
#         else:
#             print("\nInvalid choice. The adventure ends here.")
            
#     def enter_cave(self):
#         print("\nYou chose to enter the dark cave. Inside, you find a treasure chest.")
#         print("1. Open the chest.")
#         print("2. Leave the cave.")
#         choice = input("What do you want to do? (1 or 2): ")

#         if choice == '1':
#             print("\nYou chose to open the chest. Congratulations! You found a valuable gem.")
#         elif choice == '2':
#             print("\nYou chose to leave the cave. As you exit, the cave entrance collapses behind you.")
#         else:
#             print("\nInvalid choice. The adventure ends here.")
            
#     def follow_path(self):
#         print("\nYou chose to follow the path through the forest. The path splits into two directions.")
#         print("1. Take the left path.")
#         print("2. Take the right path.")
#         choice = input("What do you want to do? (1 or 2): ")

#         if choice == '1':
#             print("\nYou chose the left path. After a short walk, you find a beautiful clearing with a hidden waterfall.")
#         elif choice == '2':
#             print("\nYou chose the right path. Unfortunately, it leads to a dead end.")
#         else:
#             print("\nInvalid choice. The adventure ends here.")
            
# game = AdventureGame()
# game.start()

#----------------Project 10---------------

# import random

# class RockPaperScissors:
#     def __init__(self):
#         self.moves = {1: "Rock", 2: "Paper", 3: "Scissors"}
#         print("Welcome to Rock, Paper, Scissors!")
    
    # def get_player_move(self):
    #     try:
    #         player_move = int(input("Select your move (1 for Rock, 2 for Paper, 3 for Scissors): "))
    #         if player_move not in self.moves:
    #             print("Invalid input. Please enter 1, 2, or 3.")
    #             return None
    #         return player_move
    #     except ValueError:
    #         print("Invalid input. Please enter a number.")
    #         return None
        
    # def get_computer_move(self):
    #     return random.randint(1, 3)
    
    # def determine_winner(self, player_move, computer_move):
    #     print(f"Computer chose {self.moves[computer_move]}. You chose {self.moves[player_move]}.")

#         if player_move == computer_move:
#             print("It's a tie!")
#         elif (player_move == 1 and computer_move == 3) or \
#              (player_move == 2 and computer_move == 1) or \
#              (player_move == 3 and computer_move == 2):
#             print("You win!")
#         else:
#             print("You lose!")
            
#     def play(self):
#         player_move = self.get_player_move()
#         if player_move:
#             computer_move = self.get_computer_move()
#             self.determine_winner(player_move, computer_move)
            
# game = RockPaperScissors()
# game.play()

#----------------Project 11---------------

# class CurrencyConverter:
    
#     def __init__(self):
#         self.exchange_rates = {
#             'EUR': 0.85,  
#             'GBP': 0.75,  
#             'JPY': 110.0  
#         }
        
#     def convert(self, amount, target_currency):
#         if target_currency in self.exchange_rates:
#             converted_amount = amount * self.exchange_rates[target_currency]
#             symbol = '€' if target_currency == 'EUR' else '£' if target_currency == 'GBP' else '¥'
#             print(f"Converted amount in {target_currency}: {symbol}{converted_amount:.2f}")
#         else:
#             print("Invalid currency selection.")
            
#     def get_user_input(self):
#         amount_in_usd = float(input("Enter the amount in USD: "))
#         print("Select target currency (EUR, GBP, JPY): ")
#         target_currency = input("Enter the currency code (e.g., EUR, GBP, JPY): ").upper()
#         self.convert(amount_in_usd, target_currency)
        
# converter = CurrencyConverter()
# converter.get_user_input()

#----------------Project 12---------------

# import requests
# from bs4 import BeautifulSoup

# class WebScraper:
#     def __init__(self, url):
#         self.url=url
#         self.soup=None
        
#     def fetch_content(self):
#         try:
#             response=requests.get(self.url)
#             if response.status_code==200:
#                 self.soup = BeautifulSoup(response.text, 'html.parser')
#                 print(f"Successfully fetched content from {self.url}")
#             else:
#                 print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
                
#         except requests.RequestException as e:
#             print(f"An error occurred: {e}")
    
#     def extract_h1_tags(self):
#         if self.soup:
#             h1_tags = self.soup.find_all('h1')

#             print(f"List all the h1 tags from {self.url}:")
#             for tag in h1_tags:
#                 print(tag)
#         else:
#             print("No content fetched. Please call fetch_content() first.")
            
# url = "https://en.wikipedia.org/wiki/Main_Page"
# scraper = WebScraper(url)
# scraper.fetch_content()
# scraper.extract_h1_tags()

#----------------Project 13---------------


