"""SciLib Configuration - Single Source of Truth."""
import logging
from typing import Any
from enum import Enum

# Logger setup
logger = logging.getLogger("scilib")

class ErrorMode(Enum):
    STRICT = "strict"      # raise alle Exceptions
    WARN = "warn"          # log warnings, return None  
    SILENT = "silent"      # nur None, keine Logs

class ErrorsConfig:
    def __init__(self):
        self._mode = ErrorMode.STRICT  # Default
        self.log_level = "WARNING"
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, value):
        self._mode = ErrorMode(value) if isinstance(value, str) else value
    
    @property
    def silent(self):
        return self._mode == ErrorMode.SILENT
    
    @property
    def raise_exceptions(self):
        return self._mode == ErrorMode.STRICT

class SISystemConfig:
    """SI Unit System configuration."""
    length_unit = "m"
    pressure_unit = "Pa"

class PrecisionConfig:
    """Set numerical precision for mathematical calculations."""
    digits = 20
    bits = 128  

class Config:
    """Lists all available config handlers"""
    def __init__(self):
        self.errors = ErrorsConfig()
        self.si = SISystemConfig()
        self.precision = PrecisionConfig()

    def handle_error(self, msg: str) -> Any:
        """Unified error handling across SciLib."""
        mode = self.errors.mode
        if mode == ErrorMode.STRICT:
            raise ValueError(msg)
        elif mode == ErrorMode.WARN:
            logger.warning(msg)
        return None  # SILENT

# Global instance
config = Config()


"""
# Nutzung:
config.errors.mode = "silent"     # 1 Zeile!
r = deg_to_rad("invalid")         # → None

config.errors.mode = "warn"       # Logs + None
"""