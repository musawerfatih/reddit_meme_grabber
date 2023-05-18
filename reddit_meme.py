import praw
import requests
import random
import uuid
import os
import tempfile

CLIENT_ID = "KWe5KYIicftzRv9_fNFgbw"
CLIENT__SECRET = "XVJEfk-jHWaIIOL9ZEF08weVjXv7TA"
USER_AGENT = "My Programming Meme/1.0 (by /u/programming-memes)"

while True:
    reddit = praw.Reddit(client_id=CLIENT_ID,
                        client_secret=CLIENT__SECRET,
                        user_agent=USER_AGENT,)

    subreddit = reddit.subreddit('ProgrammerHumor') # subreddit for programming memes
    memes = subreddit.hot(limit=50) # grab 50 hottest posts from subreddit
    # Filter posts that contain an image and store their URLs
    image_urls = [post.url for post in memes if post.url.endswith(('.jpg', '.jpeg', '.png'))]
    # Choose a random image URL from the filtered list
    random_image_url = random.choice(image_urls)

    print(random_image_url)
    # Download the image using requests
    response = requests.get(random_image_url)

    # Random string to add to image name
    rand_string = str(uuid.uuid4())[:6]


import os

# Get the path to the Termux home directory
home_directory = os.path.expanduser('~')

# Specify the directory where you want to save the image
save_directory = os.path.join(home_directory, 'Download')

# Create the save directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# ...

# Save the image to a file in the specified directory
image_file_path = os.path.join(save_directory, f"programming_meme_{rand_string}.jpg")
with open(image_file_path, 'wb') as f:
    f.write(response.content)

print(f"Image saved at: {image_file_path}")
    print("-"*30)
    
    cont = input("\nDo you want to download another meme (y/n): ")
    if cont in ['y','Y']:
        continue
    else:
        break
print("Thanks for using the service.")
