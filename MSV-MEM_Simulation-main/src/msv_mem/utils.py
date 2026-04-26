import logging
from pathlib import Path

# Project root is two levels up from this file (src/msv_mem/utils.py -> src/msv_mem -> src -> project root)
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Define directories
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
GMAT_DIR = PROJECT_ROOT / "gmat"
GMAT_OUT_DIR = GMAT_DIR / "outputs"

def setup_logger(name: str = "msv_mem") -> logging.Logger:
    """Configure and return the standard logger for the application."""
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        
        # File handler (optional, writes to results/simulation.log)
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        fh = logging.FileHandler(RESULTS_DIR / "simulation.log")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
    return logger
