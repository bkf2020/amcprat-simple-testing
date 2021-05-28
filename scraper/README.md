# Webscrapper for Art of Problem Solving
This is a Python webscrapper that webscrapes the following problems:
- 2014 to 2020 AMC8 Problems
- 2015 to 2021 AMC10 Problems
- 2015 to 2021 AMC12 Problems
- 2015 to 2021 AIME Problems

Is much more efficient than the old scraper.

# Running
To run the webscrapper, run:
```
python3 scraper.py
```

# Dependencies
You will need to install beautifulsoup4:
```
pip install bs4
```

There may be other dependencies, and usually the error from Python will tell you what to install.

# I got an error!
First, make sure this isn't a dependency error. If it isn't, then please open an issue on github.
The error will usually occur under text that says "Creating problem x."
Please include in your issue the text above. (The text that says "creating problem x.")
Then copy and paste the error from Python.

Usually, this error is from the Art of Problem Solving wiki. Sometimes, the wiki is inaccurate
and missing some links. I can debug the program and fix the issue on the wiki, since anyone
on AoPS can edit it.

# What is `old_scraper.py`?
It is an outdated version of this scraper. It is used to create the problemset of ONE YEAR
for a specific test. Using it to scrape all the problems in AMCPRAT is much less efficient.
If you want to use it, please see `README_old.md` (which will be updated) for details.
I can use this as a backup, in case the AoPS wiki has issues when scrapping a certain year.
