"""ben-sh

Usage:
  ben-sh [-v | -vv ] CAMPAIGN_FILE
  ben-sh (-h | --help)
  ben-sh --version

Options:
  -h --help   Show this screen
  --version   Show version
  -v -vv -vvv Increase program verbosity
"""

from docopt import docopt

from hpcbench import __version__
from hpcbench.driver import CampaignDriver
from hpcbench.toolbox.loader import load_components
from . import setup_logger


def main():
    arguments = docopt(__doc__, version='hpcbench ' + __version__)
    setup_logger(arguments['-v'])
    load_components()
    campaign_file = arguments['CAMPAIGN_FILE']
    driver = CampaignDriver(campaign_file=campaign_file)
    driver()


if __name__ == '__main__':
    main()