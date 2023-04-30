# Internet-Speed-Twitter-Complaint-Bot

Selenium script that gets your current download/upload speed and tweets at your provider if speeds are below what 
is written in your contract

Features:
- Utilizes Selenium to automate internet speed checking, so you don't have to
- Automatically retrieves your current download / upload speed using `speedtest.net`
- Logs into twitter automatically. Added checks to bypass unusual login activity
- If your current download / upload speeds are below the values promised in your internet contract, the script will 
tweet at your provider
- Reruns every 5 minutes

How to run:
- Download repository
- Get your ISP's guaranteed internet speeds (Download and Upload in Mbps) and update `PROMISED_DOWNLOAD` and 
`PROMISED_UPLOAD` in `main.py`. You should find this in your contract
- Add your twitter login info in `main.py` to the variables of `TWITTER_LOGIN`, `TWITTER_PASSWORD`, and 
`TWITTER_USERNAME_OR_PHONE_NUMBER`
- Open downloaded repository with a command line interface
- run `pip install selenium`
- run `python main.py`
- Script start and windows will open. If current download / upload speed values are too low a tweet will be made

Example Tweet:

![alt text](https://github.com/J0K3Rn/Internet-Speed-Twitter-Complaint-Bot/blob/main/screenshots/tweet.png?raw=true)
