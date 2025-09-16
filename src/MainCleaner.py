import logging
from typing import List, Tuple, Optional
from cleaners.BaseCleaner import BaseCleaner
from cleaners.EmptySegementCleaner import EmptySegmentCleaner
from cleaners.NonTextCleaner import NonTextCleaner
from cleaners.NormalizeControlCharactersCleaner import NormalizeControlCharactersCleaner
from cleaners.NormalizeEscapedCharactersCleaner import NormalizeEscapedCharactersCleaner
from cleaners.NormalizeQuoteCleaner import NormalizeQuoteCleaner
from cleaners.RemoveLongShortCleaner import RemoveLongShortCleaner
from cleaners.RemoveSenselessCleaner import RemoveSenselessCleaner
from cleaners.UnbalancedBracketCleaner import UnbalancedBracketCleaner
from post_cleaners.BasePostCleaner import BasePostCleaner
from post_cleaners.DuplicatePostCleaner import DuplicatePostCleaner
from post_cleaners.LengthRatioCleaner import LengthRatioCleaner

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class MainCleaner:
    """
    Main cleaner that orchestrates all individual cleaners.
    Runs validation and cleaning pipelines on data segments.
    """
    
    def __init__(self):
        """Initialize the main cleaner with all available cleaners."""
        self.cleaners: List[BaseCleaner] = []
        self.post_cleaners: List[BasePostCleaner] = []
        
        self._initialize_cleaners()
        self._initialize_post_cleaners()
        
        logger.info(f"Initialized MainCleaner with {len(self.cleaners)} cleaners and {len(self.post_cleaners)} post cleaners")
    
    def _initialize_cleaners(self):
        """Initialize all individual segment cleaners."""
        try:
            self.cleaners = [
                EmptySegmentCleaner(),
                NonTextCleaner(),
                NormalizeControlCharactersCleaner(),
                NormalizeEscapedCharactersCleaner(),
                NormalizeQuoteCleaner(),
                RemoveLongShortCleaner(),
                RemoveSenselessCleaner(),
                UnbalancedBracketCleaner()
            ]
            logger.info("Successfully initialized all segment cleaners")
        except Exception as e:
            logger.error(f"Error initializing cleaners: {e}")
            raise
    
    def _initialize_post_cleaners(self):
        """Initialize all post cleaners."""
        try:
            self.post_cleaners = [
                DuplicatePostCleaner(),
                LengthRatioCleaner()
            ]
            logger.info("Successfully initialized all post cleaners")
        except Exception as e:
            logger.error(f"Error initializing post cleaners: {e}")
            raise