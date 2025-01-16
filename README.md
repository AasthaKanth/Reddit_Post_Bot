# Reddit_Post_Bot

This repository contains a Python bot that generates AI-based content using the Groq API and posts it to Reddit. The bot also includes functionality to comment on posts in a specified subreddit. The bot uses the PRAW (Python Reddit API Wrapper) library for Reddit interaction and the `groq` library for AI-generated content.

## Working of the Code

**Initialization:** The bot initializes by loading the necessary credentials and configurations from bot.py.

**Content Generation:**

The bot sends a prompt to the Groq API and receives AI-generated text.

**Reddit Interaction:**

Using PRAW, the bot connects to the specified subreddit.

Posts the generated content as a new submission.

Comments on the latest posts in the subreddit with AI-generated replies.

**Scheduling:**

Tasks for posting and commenting are scheduled using the schedule library.

Logging:

All actions, including errors and successful tasks, are logged in bot.log for future reference.

## Features

- **AI-Generated Content**: The bot uses the Groq API to generate text based on a given prompt.
- **Automated Reddit Posting**: Posts generated content to a specified subreddit daily at a scheduled time.
- **Automated Commenting**: Comments on the latest posts in the target subreddit using AI-generated replies.
- **Error Logging**: All errors and activities are logged in a `bot.log` file for debugging and tracking.

## Prerequisites

1. **Python 3.7 or higher**
2. **Required Python Libraries**:
   - `praw`
   - `requests`
   - `schedule`
   - `groq`

   Install these libraries using:
   ```bash
   pip install -r requirements.txt
   ```
3. **Reddit API Credentials**:
   - Create a Reddit app [here](https://www.reddit.com/prefs/apps).
   - Note the `client_id`, `client_secret`, `username`, `password`, and `user_agent`.
4. **Groq API Key**:
   - Sign up for the Groq AI API and obtain an API key.

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/reddit-ai-bot.git
   cd reddit-ai-bot
   ```

2. Update the configuration in `bot.py`:
   - Replace placeholders with your Reddit API credentials.
   - Replace the Groq API key with your actual key.

3. Run the bot:
   ```bash
   python bot.py
   ```

## Configuration

### Scheduled Tasks
- **Posting AI-Generated Content**:
  - The bot is configured to post daily at `09:36`. You can change the time by modifying this line in the code:
    ```python
    schedule.every().day.at("09:36").do(post_to_reddit)
    ```
- **Commenting on Posts**:
  - The bot comments daily at `12:00`. Adjust the time here:
    ```python
    schedule.every().day.at("12:00").do(comment_on_posts)
    ```

## Logging
- Logs are stored in `bot.log`.
- Tracks:
  - Successful posts
  - Comments made
  - Errors encountered

## Example Usage

- **Generate Content**:
  The bot uses a prompt to generate content. Example prompt:
  ```python
  prompt = "Explain the importance of low latency LLMs"
  ```

- **Post to Reddit**:
  Posts the generated content as a submission:
  ```python
  subreddit.submit(title="Daily AI Post", selftext=content)
  ```

- **Comment on Posts**:
  The bot comments on the top 10 posts in the subreddit.

## Error Handling
- Errors related to the Groq API or Reddit API are logged in `bot.log`.
- Common issues include invalid API keys, network errors, or rate limits.

