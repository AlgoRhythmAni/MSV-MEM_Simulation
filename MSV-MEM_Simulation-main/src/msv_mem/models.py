from pydantic import BaseModel, Field, model_validator

class MSVParameters(BaseModel):
    """Parameters for the Main Service Vehicle (MSV)."""
    dry_mass: float = Field(1100.0, description="MSV Dry Mass (Bus) in kg")
    launch_mass: float = Field(3550.0, description="MSV Launch Mass (total stack including 3 MEMs and chemical fuel) in kg")
    chem_delta_v: float = Field(1800.0, description="Chemical Delta V for GTO to GEO in m/s")

class MEMParameters(BaseModel):
    """Parameters for the Mission Extension Module (MEM)."""
    wet_mass: float = Field(300.0, description="MEM Wet Mass in kg")
    target_mass: float = Field(1500.0, description="Target Satellite Mass in kg")
    n_mem: int = Field(3, description="Number of MEMs")
    ep_isp: float = Field(1800.0, description="Electric Propulsion Specific Impulse in seconds")
    ep_propellant: str = Field("Xenon", description="Propellant type")
    sail_area: float = Field(50.0, description="Solar Sail Area in m^2")

class OrbitParameters(BaseModel):
    """Orbital parameters."""
    r_geo: float = Field(42164.0, description="GEO Radius in km")
    atmo_interface: float = Field(6478.0, description="Atmospheric Interface (100km alt) in km")

class ScenarioAParameters(BaseModel):
    """Scenario A: Life Extension and Atmospheric Deorbit."""
    station_keeping_fuel: float = Field(25.3, description="Station-Keeping Fuel (5 years) in kg")
    deorbit_dv: float = Field(1495.0, description="Deorbit Delta V in m/s")
    deorbit_fuel: float = Field(144.0, description="Deorbit Fuel in kg")
    total_xenon: float = Field(170.0, description="Total Xenon Load in kg")
    dry_mass_margin: float = Field(130.0, description="Dry Mass Margin in kg")

class ScenarioBParameters(BaseModel):
    """Scenario B: Graveyard Retrieval."""
    deorbit_dv: float = Field(1505.0, description="Deorbit Delta V in m/s")
    total_xenon: float = Field(147.0, description="Total Xenon Load in kg")
    dry_mass_margin: float = Field(153.0, description="Dry Mass Margin in kg")

class DebriSolverSystem(BaseModel):
    """Complete system parameter model for DebriSolver."""
    msv: MSVParameters = Field(default_factory=MSVParameters)
    mem: MEMParameters = Field(default_factory=MEMParameters)
    orbit: OrbitParameters = Field(default_factory=OrbitParameters)
    scenario_a: ScenarioAParameters = Field(default_factory=ScenarioAParameters)
    scenario_b: ScenarioBParameters = Field(default_factory=ScenarioBParameters)

    @model_validator(mode='after')
    def validate_mass_budget(self) -> 'DebriSolverSystem':
        """Validate that the calculated launch mass does not exceed the allowed launch mass limit."""
        # Total mass = MSV Dry Mass + (N_MEM * MEM Wet Mass) + Chem Propellant
        # The paper implies 3550kg is the limit.
        calculated_stack_dry = self.msv.dry_mass + (self.mem.n_mem * self.mem.wet_mass)
        if calculated_stack_dry >= self.msv.launch_mass:
            raise ValueError(f"Dry stack mass ({calculated_stack_dry} kg) exceeds launch mass ({self.msv.launch_mass} kg)")
        return self
