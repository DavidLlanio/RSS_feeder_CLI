# Import the necessary libraries
import os         # Command line tools
import argparse   # To get the command line arguments
import feedparser # RSS parser



class RSS_Feed():
    """
    Main class
    """
    def __init__(self):

        self.store_rss = False
        self.rss_parser = None
        self.parsed_args = None

    def parse_rss(self):
        pass

    def parse_cli_arguments(self):
        arg_parser = argparse.ArgumentParser(description="CLI for viewing RSS feeds")
        arg_parser.add_argument("rss_url", metavar="URL", type=str, help="URL of RSS feed")
        arg_parser.add_argument("-s", "--save", action="store_true", help="Save the URL")
        self.parsed_args = vars(arg_parser.parse_args())

    def run(self):
        self.parse_cli_arguments()
        print(self.parsed_args)

if __name__ == '__main__':
    runner = RSS_Feed()
    runner.run()
