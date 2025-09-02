# Observation Challenge Scaffold

This folder contains a clean scaffold to solve the multi-station Observation Challenge.

## Files
- `station1.py` ... `station7.py`: put the decoded algorithm for each station here.
- `main.py`: harness that imports all stations, enforces types, and computes the combined outputs.

## How to proceed
1. Gather the **sample inputs/outputs** from each station.
2. For each station file, implement `solution_station_X(x)` so it reproduces the mapping from input to output.
   - Keep it pure (no prints / I/O). Return the required type indicated by assertions in `main.py`.
3. Capture **three synchronized observations** in `main.py`:
   ```python
   observation1 = ('HH:MM:SS', station1_input:int, station2_input:str, station3_input:int, station4_input:int, station5_input:str, station6_input:int, station7_input:str)
   observation2 = (...)
   observation3 = (...)
   ```
4. Run:
   ```bash
   python main.py
   ```
5. If you have the official `tests` package available, the harness will run `tests.Test_Exercise(combined_algorithm)` automatically.

## Need help decoding?
When you paste each station's sample I/O (a few examples per station are enough), we can infer the underlying rules and complete the functions for you.
