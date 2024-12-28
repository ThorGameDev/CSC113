# November 8, 2023

# is file will be used latter to warn the user if they intend to override their file
from os.path import isfile

print("Welcome to the simple personal website generator!\n\n")

def create_website():
    # requests user input and stores it for latter use
    print("Enter your name:")
    name = input()

    # Checks if the html file already exists, and warns the user
    if isfile(f"{name}_Website.html"):
        print("Your website already exists!")
        print("Do you want to override it? y/n")
        if input() != "y":
            return

    # Begins creating the website. It can fail in certain cases, such as the user deleting the website mid creation
    try:
        with open(f"{name}_Website.html", "w") as file:
            # Requests user input to use in the website
            print("Describe yourself")
            text = input()
            # begins writing the file.
            file.writelines(["<!DOCTYPE html>",
                             "<html>",
                             "<body>",
                             "",
                             f"<h1>{name}</h1>",
                             f"<p>{text}</p>",
                             ""])
            
            # Prompts the user to embed a game
            print("Embed a game? y/n")
            if input() == "y":
                # Creates a variable representing the HTML line necessary to embed a game
                game = '<iframe frameborder="0" src="https://itch.io/embed-upload/8423457?color=460006" allowfullscreen="" width="1000" height="720"><a href="https://a-thor.itch.io/indefinite-dungeons">Play Indefinite Dungeons on itch.io</a></iframe>'
                # Gives the user an opportunity to change the message just above the game
                print("Use default message? y/n")
                game_message = "BTW, this game is cool"
                if input() != "y":
                    print("The new message should try to explain the presence of the game.")
                    print(f"The default is '{game_message}'")
                    game_message = input("New message:") 
                # Adds the message and the embedded game to the HTML file
                file.writelines([f"<p>{game_message}</p>",
                                 game,
                                 ""])

            # Completes the file 
            file.writelines(["</body>",
                             "</html>"])
    except:
        print("Your website was not created successfully...")
    finally:
        print("Your website was created successfully!")

# Core program loop
while True:
    print("Create a website? y/n")
    if input() == "y":
        create_website()
    else:
        print("Goodbye!")
        exit()
