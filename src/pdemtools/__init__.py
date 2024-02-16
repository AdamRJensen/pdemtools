from importlib.metadata import version

from . import load
from . import data
from ._index_search import search

from ._accessor import DemAccessor

__version__ = version("pdemtools")

__all__ = ["search", "DemAccessor"]
