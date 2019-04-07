# Author: Matthew Bolger
# Can be used and/or edited for any purpose (including the assignment).

import logging
import random
try:
    from sense_hat import SenseHat
except ImportError:
    pass

class VirtualSenseHat:
    @staticmethod
    def getSenseHat(logError = True):
        try:
            return SenseHat()
        except Exception as e:
            if(logError):
                logging.error("Falling back to VirtualSenseHat because: " + str(e))
            return VirtualSenseHat()

