def vacuum_cleaner(env, initial_position):
    state = env.copy()
    position = initial_position
    steps = 0

    print("Initial Environment State:", state)
    print("Starting at Room", position)
    
    while "Dirty" in state.values():
        print(f"\nStep {steps}:")
        print(f"Vacuum is in Room {position}")
        
        if state[position] == "Dirty":
            print("Action: CLEAN")
            state[position] = "Clean"
        else:
            position = "B" if position == "A" else "A"
            print(f"Action: MOVE to Room {position}")
        
        steps += 1

    print("\nFinal Environment State:", state)
    print("All rooms are clean in", steps, "steps.")

environment = {"A": "Dirty", "B": "Dirty"}  
vacuum_cleaner(environment, "A")
