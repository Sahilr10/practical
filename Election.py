#Bully algo
# List of processes (IDs)
processes = [1, 2, 3, 4, 5]

# Initially highest process is coordinator
coordinator = max(processes)

print("Initial Coordinator:", coordinator)

# Function to start election
def election(initiator):
    global coordinator
    print(f"\nProcess {initiator} starts election")

    higher = [p for p in processes if p > initiator]

    if not higher:
        coordinator = initiator
        print(f"Process {initiator} becomes Coordinator")
    else:
        print(f"Process {initiator} sends election to {higher}")
        election(max(higher))


# Simulate failure of coordinator
print("\nCoordinator fails!")
processes.remove(coordinator)

# Start election from a process
election(2)

print("\nNew Coordinator:", coordinator)