# Tweetbotty
Twitter bots written in Python which use Excel file as a source for tweets/search keywords.

**xls2tw.py:** endless posting of tweets from Excel spreadsheet to Twitter

**follower_people.py:** auto following people (twitter search people) based on keywords defined in Excel

**follower_tw_slow.py:** auto following people (twitter search tweets) based on keywords defined in Excel, 288 per day, avoiding Twitter limits

**unfollower.py:** unfollow people with too little tweets or followers

## :wrench: Dependencies and Installation

### Installation xls2tw.py (Twitter bot)

1. Clone repo

    ```bash
    git clone https://github.com/trozman/Tweetbotty.git
    cd Tweetbotty
    ```
2. Install dependent packages

    ```bash
    # Install Openpyxl - Excel library
    pip install openpyxl

    # Install Colorama - Coloured text output
    pip install colorama

    # Install Tweepy - Twitter library
    pip install tweepy
    ```

3. Create a project, development app and obtain Twitter keys (from your twitter development account) at https://developer.twitter.com/en/portal/dashboard
4. Upgrade your Twitter developer account to the 'Elevated' account (free)
5. Put your twitter keys to 'tweetconfig.txt'  
6. Put some tweets to 'Tweets.xlsx', worksheet 'Tweets', B Column
7. Run it:
    ```bash
    python xls2tw.py
    ```
    
8.  This tweetbot will run forewer: it will read tweets in sequence from excel tile, 
publish it to Twitter, pausing for X hours. If it finds the empty row in the 
spreadsheet(no more tweets), it will start from the beginning. You can add rows 
with tweets while this script is running.
If you interrupt it (ctrl-c) and re-run it, it will start from the last published tweet.

### Installation follower_people.py (Follower bot - people search)

The same as previous. Changes:

Step 6: Put comma separated keywords for people search in 'Tweets.xlsx', worksheet 'Keywords', cell A:2

Step 7: Run it:

    ```bash
    python follower_people.py
    ```

### Installation follower_tw_slow.py (Follower bot - tweet search)

The same as previous. Changes:

Step 6: Put comma separated keywords for people search in 'Tweets.xlsx', worksheet 'Keywords', cell B:2

Step 7: Run it:

    ```bash
    python follower_tw_slow.py
    ```

### Installation unfollower.py (Un-Follower bot, get rid of people with too little followers or tweets)

The same as previous. Changes:

Step 6: Define filters, modify variables filter_followers and filter_tweets

Step 7: Run it:

    ```bash
    python unfollower.py
    ```
