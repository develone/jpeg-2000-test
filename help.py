from myhdl import *
from PIL import Image,ImageSequence
from argparse import Namespace
import pydoc

import Queue
strhelp = pydoc.render_doc(Queue, "Help on %s")
print strhelp
