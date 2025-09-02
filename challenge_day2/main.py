"""
Observation Challenge — Partial Harness (prints Stations 1 & 2 + combined)
"""

from station1 import solution_station_1
from station2 import solution_station_2

# Three sample observations (time, s1_input:int, s2_input:str)
observation1 = ('09:41:42', 20, '2023 - 03 - 21')
observation2 = ('09:55:03', 21, '2023 - 12 - 02')
observation3 = ('09:55:13', 45, '2023 - 06 - 24')

def combined_with_defaults(obs: tuple) -> int:
    """
    Compute the final combined value using real Station 1 & 2 outputs,
    and safe defaults for Stations 3–7 (since they aren't implemented yet).
      Types needed:
        s1:int, s2:str, s3:bool, s4:bool, s5:int, s6:float, s7:float
    Defaults chosen to be neutral-ish multipliers:
        s3=True -> factor 3, s4=True -> factor 5, s5=1, s6=1.0, s7=1.0
    """
    # Real calls for 1 & 2
    output1 = solution_station_1(obs[1])   # int
    output2 = solution_station_2(obs[2])   # str

    # Defaults for 3–7
    output3 = True    # bool  -> factor 3
    output4 = True    # bool  -> factor 5
    output5 = 1       # int
    output6 = 1.0     # float
    output7 = 1.0     # float

    factor2 = int.from_bytes(output2[0].encode("unicode_escape"), byteorder='big')
    factor3 = 3 if output3 else 2
    factor4 = 5 if output4 else 4
    return output1 * factor2 * factor3 * factor4 * output5 * output6 * output7

def run_one(obs):
    fib_val = solution_station_1(obs[1])
    weekday = solution_station_2(obs[2])
    combo = combined_with_defaults(obs)
    print(f"Obs @ {obs[0]} -> Station1:{fib_val}, Station2:{weekday}, Combined:{int(combo)}")

if __name__ == "__main__":
    run_one(observation1)  # expected fib=6765, weekday='tuesday'
    run_one(observation2)  # expected fib=10946, weekday='saturday'
    run_one(observation3)  # expected fib=1134903170, weekday='saturday'
