# MSV-MEM Simulation Framework (DebriSolver)

This repository contains the simulation framework for the **DebriSolver** architecture, designed for Active Debris Removal (ADR) and satellite servicing in Geostationary Earth Orbit (GEO). 

The system models a modular approach utilizing a **Main Service Vehicle (MSV)** and multiple **Mission Extension Modules (MEMs)**.

## Technical Specifications
Based on the DebriSolver research paper:
- **MSV Launch Mass**: ~3,550 kg (stack with 3 MEMs and chemical fuel)
- **MSV Dry Mass**: 1,100 kg
- **MEM Wet Mass**: 300 kg (target capacity: 1,500 kg per MEM)
- **Propulsion**: Hybrid (Chemical for MSV GTO-GEO raising, Electric/Solar Sail for MEM operations)

## Operations Modeled
- **Scenario A**: Life Extension and Atmospheric Deorbit (5 years active station-keeping).
- **Scenario B**: Graveyard Retrieval and immediate deorbit.

## Prerequisites
- Python 3.10+
- [GMAT R2025a](https://gmat.atlassian.net/wiki/spaces/GW/overview) (optional, for trajectory propagation)

## Installation and Execution
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/MacOS
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the full simulation pipeline:
   ```bash
   python run_all_simulations.py
   ```

## GMAT Integration
To automatically run the generated GMAT scripts, set the `GMAT_EXEC` environment variable to point to your GMAT executable.
```bash
export GMAT_EXEC=/path/to/GMAT/bin/GMAT.exe
```
If not set, the script will generate the `.gmat` file in `gmat/outputs/` which you can open and run manually in the GMAT GUI.
