import os

_current_dir = os.path.abspath(os.path.dirname(__file__))
HOME_CRAWLER_ROOT = os.path.normpath(os.path.join(_current_dir, "..", ".."))
THIRD_ROOT=os.path.normpath(os.path.join(_current_dir,"..","third"))

