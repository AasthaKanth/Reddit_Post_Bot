import praw
import requests
import schedule
import time
import logging
from groq import Groq

# Reddit API Authentication
reddit = praw.Reddit(
    client_id="{CLIENT_ID}", # Enter the client id
    client_secret="{CLIENT_SECRET}", #Enter the client secret fromt he reddit api
    username="{REDDIT_USERNAME}", # Enter your Reddit username
    password="{REDDIT_PASSWORD}", # Enter your reddit password
    user_agent="Reddit bot for AI-generated posts",
)

# Function to generate content using Groq API
client = Groq(
    api_key="{GROQ_API_KEY}"  # Enter your Groq API key
)

def generate_content(prompt):
    """
    Generates content using the Groq AI API.
    
    Args:
        prompt (str): The input prompt for generating content.
    
    Returns:
        str: Generated content or None if an error occurred.
    """
    try:
        # Send a chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,  # Use the provided prompt
                }
            ],
            model='llama-3.3-70b-versatile'  # Specify the model
        )
        # Return the generated content
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        logging.error("Error with Groq API: %s", e)
        return None


# Function to post AI-generated content to Reddit
def post_to_reddit():
    prompt = input()
    # "Write a fun fact about technology"
    content = generate_content(prompt)
    if content:
        try:
            subreddit = reddit.subreddit("test")  # Target subreddit to post on
            subreddit.submit(title="Daily AI Post", selftext=content)
            print("Posted successfully:", content)
            logging.info("Posted to Reddit: %s", content)
        except Exception as e:
            logging.error("Error posting to Reddit: %s", e)

# Function to comment on posts
def comment_on_posts():
    try:
        subreddit = reddit.subreddit("test")
        for post in subreddit.hot(limit=10):
            if not post.stickied:
                comment = generate_content("Write a comment on this post")
                if comment:
                    post.reply(comment)
                    print(f"Commented on: {post.title}")
                    logging.info("Commented on post: %s", post.title)
    except Exception as e:
        logging.error("Error commenting on posts: %s", e)



if __name__ == "__main__":
    print("Bot is running...")
    # Logging configuration
    logging.basicConfig(
        filename="bot.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Bot started successfully.")

    while True:
        try:
            # Schedule the post
            schedule.every().day.at("09:36").do(post_to_reddit)
            # Schedule comments most liked post
            schedule.every().day.at("12:00").do(comment_on_posts)
            # For testing: schedule.every(1).minutes.do(post_to_reddit)
            schedule.run_pending()
            time.sleep(1)  
        except KeyboardInterrupt:
            print("Bot stopped by user.")
            logging.info("Bot stopped by user.")
            break
        except Exception as e:
            logging.error("Unexpected error: %s", e)
