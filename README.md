# DevProjects - RSS_feeder_CLI

This is an open source project from [DevProjects](http://www.codementor.io/projects). Feedback and questions are welcome!
Find the project requirements here: [RSS feed reader in terminal](https://www.codementor.io/projects/tool/rss-feed-reader-in-terminal-atx32jp82q)

## Tech/framework used
Built with: 
- Python v3.9
- feedparser v6.0.8

## Installation
1. Clone repo into your environment
2. Install necessary package: ```pip install feedparser```
4. Open terminal to directory with rss.py and run with: ```python rss.py [options]```

To view usage of command line interface run: ```python rss.py -h``` or ```python rss.py --help```

## How to use
Once you have installed it and have navigated to the directory you can run ```python rss.py <url>``` where url is your RSS feed url. The command line interface will only take one url at a time. You can save the RSS feed url to output later with the save optiont by running ```python rss.py <url> -s``` or ```python rss.py <url> --save```

## License
[MIT](https://choosealicense.com/licenses/mit/)
