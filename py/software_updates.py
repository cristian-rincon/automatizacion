import os
import logging
from sys import platform

log = logging.getLogger(__name__)

update = "sudo apt update"
upgrade = "sudo apt upgrade"



def updater():
    """
    docstring
    """
    os.system(update)

    if platform == "linux" or platform == "linux2":
        log.debug(">>> Linux Platform")
        try:
            os.system(upgrade)
        except Exception as e:
            log.info(e)
    elif platform == "darwin":
        # OS X
        pass
    elif platform == "win32":
        # Windows...
        pass


if __name__ == "__main__":
    updater()