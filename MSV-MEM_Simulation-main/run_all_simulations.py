"""
Main Entry Point for the MSV-MEM DebriSolver Simulation
"""
import sys
import os
import logging
from pathlib import Path

# Ensure src/ is in the python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "src"))

from msv_mem.utils import setup_logger
from msv_mem.models import DebriSolverSystem
from msv_mem.trajectory import TrajectoryAnalyzer
from msv_mem.gmat_driver import GMATDriver

def main():
    setup_logger("msv_mem")  # Configure the base logger for all msv_mem.* modules
    logger = logging.getLogger("msv_mem.main")
    logger.info("========================================")
    logger.info("Starting MSV-MEM DebriSolver Simulation")
    logger.info("========================================")
    
    # 1. Initialize parameters
    try:
        logger.info("Initializing system parameters...")
        system = DebriSolverSystem()
        logger.info("System parameters initialized and validated successfully.")
    except Exception as e:
        logger.error(f"Parameter validation failed: {e}")
        return
        
    # 2. Trajectory Analysis (Scenarios)
    logger.info("\n--- Trajectory Analysis ---")
    analyzer = TrajectoryAnalyzer(system)
    analyzer.run_all_analyses()
    
    # 3. GMAT Simulation Preparation
    logger.info("\n--- GMAT Integration ---")
    driver = GMATDriver(system)
    script_path = driver.write_script()
    driver.run_script(script_path)
    
    logger.info("\n========================================")
    logger.info("Master run finished. Inspect results/ and gmat/outputs/")
    logger.info("========================================")

if __name__ == "__main__":
    main()
