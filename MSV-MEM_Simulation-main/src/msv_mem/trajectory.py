import numpy as np
import logging
from .models import DebriSolverSystem

logger = logging.getLogger("msv_mem.trajectory")

class TrajectoryAnalyzer:
    def __init__(self, system: DebriSolverSystem):
        self.system = system
        
    def analyze_scenario_a(self):
        """Analyze Scenario A: Life Extension and Atmospheric Deorbit."""
        logger.info("Analyzing Scenario A: Life Extension and Atmospheric Deorbit")
        scen_a = self.system.scenario_a
        mem = self.system.mem
        
        logger.info(f"  Station-Keeping Fuel (5 years): {scen_a.station_keeping_fuel} kg")
        logger.info(f"  Deorbit Delta V: {scen_a.deorbit_dv} m/s")
        logger.info(f"  Deorbit Fuel: {scen_a.deorbit_fuel} kg")
        logger.info(f"  Total Xenon Load: {scen_a.total_xenon} kg")
        logger.info(f"  Dry Mass Margin: {scen_a.dry_mass_margin} kg")
        
        # Verify basic mass bounds
        required_xenon = scen_a.station_keeping_fuel + scen_a.deorbit_fuel
        if required_xenon > scen_a.total_xenon:
            logger.warning(f"  Warning: Required Xenon ({required_xenon} kg) exceeds Total Xenon Load ({scen_a.total_xenon} kg)!")
        else:
            logger.info(f"  Xenon Mass Budget Verified: {required_xenon} kg required <= {scen_a.total_xenon} kg loaded.")
            
        expected_wet_mass = scen_a.dry_mass_margin + scen_a.total_xenon
        if expected_wet_mass > mem.wet_mass:
            logger.warning(f"  Warning: Total mass ({expected_wet_mass} kg) exceeds MEM wet mass ({mem.wet_mass} kg)!")
        else:
            logger.info(f"  Total MEM Mass Verified: {expected_wet_mass} kg <= {mem.wet_mass} kg.")

    def analyze_scenario_b(self):
        """Analyze Scenario B: Graveyard Retrieval."""
        logger.info("Analyzing Scenario B: Graveyard Retrieval")
        scen_b = self.system.scenario_b
        mem = self.system.mem
        
        logger.info(f"  Deorbit Delta V: {scen_b.deorbit_dv} m/s")
        logger.info(f"  Total Xenon Load: {scen_b.total_xenon} kg")
        logger.info(f"  Dry Mass Margin: {scen_b.dry_mass_margin} kg")
        
        expected_wet_mass = scen_b.dry_mass_margin + scen_b.total_xenon
        if expected_wet_mass > mem.wet_mass:
            logger.warning(f"  Warning: Total mass ({expected_wet_mass} kg) exceeds MEM wet mass ({mem.wet_mass} kg)!")
        else:
            logger.info(f"  Total MEM Mass Verified: {expected_wet_mass} kg <= {mem.wet_mass} kg.")

    def run_all_analyses(self):
        self.analyze_scenario_a()
        self.analyze_scenario_b()
