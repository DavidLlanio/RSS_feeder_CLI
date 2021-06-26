# Import the necessary libraries
import argparse   # Command Line interface tools
import feedparser # RSS parser
import json       # Json tools



class RSS_Feed():
    """
    Main class
    """
    def __init__(self):

        self.rss_parser = None
        self.parsed_args = None

    def parse_rss(self):
        rss_url = self.parsed_args["rss_url"]
        self.rss_parser = feedparser.parse(rss_url)

        if self.parsed_args["save"]:
            pass


    def parse_cli_arguments(self):
        arg_parser = argparse.ArgumentParser(description="CLI for viewing RSS feeds")
        arg_parser.add_argument("rss_url", metavar="URL", type=str, help="URL of RSS feed")
        arg_parser.add_argument("-s", "--save", action="store_true", help="Save the URL")
        self.parsed_args = vars(arg_parser.parse_args())

    def run(self):
        self.parse_cli_arguments()
        self.parse_rss()
        print(self.parsed_args)
        print(self.rss_parser.keys())
        print(self.rss_parser.feed.title)

if __name__ == '__main__':
    runner = RSS_Feed()
    runner.run()
