# Import the necessary libraries
import os  # OS tools
import argparse  # Command Line interface tools
import feedparser  # RSS parser


class RssFeed:
    """
    Main class
    """

    def __init__(self):
        """
        Initializer
        """
        self.rss_parser = None  # Holds the parser object with parsed xml
        self.parsed_args = None  # Holds command line arguments
        self.rss_url = None  # Holds the RSS feed url

    def parse_cli_arguments(self):
        """
        Parses the command line arguments passed by user and defines interface.
        :return: None
        """
        arg_parser = argparse.ArgumentParser(description="CLI for viewing RSS feeds")
        arg_parser.add_argument("rss_url", metavar="URL", type=str, help="URL of RSS feed")
        arg_parser.add_argument("-s", "--save", action="store_true", help="Save the URL")
        self.parsed_args = vars(arg_parser.parse_args())

    def parse_rss(self, first_lap=False):
        """
        Uses the feedparser package to parse the xml from the RSS feed url
        :param first_lap: True if first time being used
        :return: None
        """

        # Get url from command line argument if first time being used
        if first_lap:
            self.rss_url = self.parsed_args["rss_url"]

        # Parse the xml from the RSS feed url
        self.rss_parser = feedparser.parse(self.rss_url)

        # Save the RSS feed url if user input save option
        if self.parsed_args["save"]:
            with open("saved_rss.txt", 'ra') as f:
                if self.rss_url not in f.read():
                    f.write(self.rss_url)

    def iterate_feeds(self):
        """
        Goes through the url feed input by user and all the saved RSS feed urls
        :return: None
        """
        if os.path.isfile("saved_rss.txt"):
            self.parse_rss(True)
            self.display_items()

            with open("saved_rss.txt", 'r') as f:
                for link in f.readlines():
                    self.rss_url = link
                    self.parse_rss()
                    self.display_items()
        else:
            self.parse_rss(True)
            self.display_items()

    def display_items(self):
        """
        Prints out the feed title, description, and entries
        :return: None
        """
        feed_title = self.rss_parser.feed.title
        feed_description = self.rss_parser.feed.title
        print("Feed: " + feed_title)
        print("Description:" + feed_description)

        for entry in self.rss_parser.entries:
            print("***")
            print(entry.title)
            print("")
            print(entry.description)
            print("")
            print(entry.link)
            print("***")
            print("")

    def run(self):
        """
        Runs the main processes
        :return: None
        """
        self.parse_cli_arguments()
        self.iterate_feeds()


if __name__ == '__main__':
    runner = RssFeed()
    runner.run()
