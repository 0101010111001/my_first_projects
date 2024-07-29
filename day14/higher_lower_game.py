import random
import os

art_logo = r"""
        _________ _______           _______  _______    _        _______           _______  _______ 
|\     /|\__   __/(  ____ \|\     /|(  ____ \(  ____ )  ( \      (  ___  )|\     /|(  ____ \(  ____ )
| )   ( |   ) (   | (    \/| )   ( || (    \/| (    )|  | (      | (   ) || )   ( || (    \/| (    )|
| (___) |   | |   | |      | (___) || (__    | (____)|  | |      | |   | || | _ | || (__    | (____)|
|  ___  |   | |   | | ____ |  ___  ||  __)   |     __)  | |      | |   | || |( )| ||  __)   |     __)
| (   ) |   | |   | | \_  )| (   ) || (      | (\ (     | |      | |   | || || || || (      | (\ (   
| )   ( |___) (___| (___) || )   ( || (____/\| ) \ \__  | (____/\| (___) || () () || (____/\| ) \ \__
|/     \|\_______/(_______)|/     \|(_______/|/   \__/  (_______/(_______)(_______)(_______/|/   \__/
                                                                                                        
"""

vs = r"""
_    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

    """

data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

# format the account into printable format | get account info(name, description, country)
def get_account_info(account):
    """get account name, description, and country ther retrun them"""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}"

# get follower count of each account
def get_account_followers(account):
    """this function get account and return it's followers account"""
    follower_count = account['follower_count']
    return follower_count

# use if statement to check if user is correct
# check if user is correct
def check_user_answer(guess, account_a_followers, account_b_followers):
    """this function check guess option with (if account_a_followers > account_b_followers) and return True if they are correct , or return False if it's not correct"""
    if account_a_followers > account_b_followers and guess == "a":     
        return True
    elif account_b_followers > account_a_followers and guess == "b":
        return True
    else:
        return False
    
def game_play():
    """ this funtion when calling it the higher lower game start """
    # score keeping
    score = 0
    game_is_running = True
    account_b = random.choice(data)
    # make the game repeatable
    while game_is_running:
        # display art logo
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print(art_logo)
        print("-----------------------------------------------------------------------------------------------------------------------------")
        # generate a random account from data
        # making account at position B become the next account at position A
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {get_account_info(account_a)}")
        print(vs)
        print(f"Against B: {get_account_info(account_b)}")

        # ask user for guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess in ["a","b"]:
            account_a_followers = get_account_followers(account_a)
            account_b_followers = get_account_followers(account_b)

            # clear the screen between rounds
            os.system('cls' if os.name == 'nt' else 'clear')

            # give user feedback on their guess
            if check_user_answer(guess, account_a_followers, account_b_followers):
                score += 1
                print("---------------------------------------")
                print(f"You're right! Current score: {score}")
                print("---------------------------------------")

            else:
                print("-------------------------------------------")
                print(f"Sorry, that's wrong. Final score: {score}")
                print("Game Over :( ")
                print("-------------------------------------------")
                game_is_running = False

        else:   
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Invalid choice, please try again...")


# playing the game
game_play()

run_game_again = True
#check if the user want to play again or not, 
# and if he/she enters something other than yes/y or no/n "Invalid input, please try again..." appeared.

while run_game_again:
    play_again = input("You want to play again? 'Yes' or 'No: ").lower()

    if play_again == "yes" :
        game_play()
    elif play_again == "no" :
        print("Thank you for trying my game, see you later :)")
        run_game_again = False
    else:
        print("Invalid input, please try again...")