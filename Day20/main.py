from math import lcm
import time
import queue

# Huge thank you to https://www.youtube.com/watch?v=lxm6i21O83k for teaching me how to approach pt2


def init_gates(lines):
    gates = {}
    for line in lines:
        gatename, outputs = line.split(" -> ")
        outputs = outputs.split(", ")
        if gatename == "broadcaster":
            gates[gatename] = [outputs, False, 'b', {}]
        else:
            gates[gatename[1:]] = [outputs, False, gatename[0], {}]
    
    # Link Conjunction gates
    for gate_name in gates:
        if gates[gate_name][2] == "&": # This is a conjunction gate
            for gate_ in gates:
                if gate_name in gates[gate_][0]:
                    gates[gate_name][3][gate_] = [False, -1]
    
    return gates


def to_state_str(state):
    if state:
        return "high"
    return "low"



last_found = {}
cycles = {}
def sim_gates(gates, pt2=False):
    if pt2:
        (feed,) = [gate for gate in gates if "rx" in gates[gate][0]]
        # feed -> Outputs high on lcm of cycle lengths of cycles of gates that feed into it (Assumed)
        cycle_lengths = {}
        seen = {gate: 0 for gate in gates if feed in gates[gate][0]}

    btn_presses = 0
    low_sent, high_sent = 0, 0
    q = queue.Queue()
    to_do = 1
    while to_do:
        if not pt2:
            to_do -= 1

        btn_presses += 1
        q.put(("broadcaster", 0, "button", btn_presses))
        while not q.empty():
            gate_name, state, trigger_name, pressed_at = q.get()
            if state:
                high_sent += 1
            else:
                low_sent += 1
            
            if gate_name not in gates:
                continue
            
            gate = gates[gate_name]

            if pt2:
                if gate_name == feed and state == True:
                    seen[trigger_name] += 1
                    if trigger_name not in cycle_lengths:
                        cycle_lengths[trigger_name] = btn_presses
                    else:
                        assert btn_presses == seen[trigger_name]*cycle_lengths[trigger_name]
                    
                    if all(seen.values()):
                        x = 1
                        for v in cycle_lengths.values():
                            x = lcm(x, v)
                        return x

            if gate[2] == "b":
                for output in gate[0]:
                    # print(f"{gate_name} -{to_state_str(state)}-> {output}")
                    q.put((output, state, gate_name, btn_presses))
            if gate[2] == "%":
                if state == 0: # Recieved a low
                    gate[1] = not gate[1]
                    for output in gate[0]:
                        out_state = gate[1]
                        # print(f"{gate_name} -{to_state_str(out_state)}-> {output}")
                        q.put((output, out_state, gate_name, btn_presses))
            if gate[2] == "&":
                # Update input for the gate that triggered this pulse
                gate[3][trigger_name] = [state, gate[3][trigger_name][1]]

                # If all inputs are high, send low, otherwise send high
                out_state = False
                if all([v[0] for v in gate[3].values()]):
                    out_state = False
                else:
                    out_state = True

                for output in gate[0]:
                    # print(f"{gate_name} -{to_state_str(out_state)}-> {output}")
                    q.put((output, out_state, gate_name, btn_presses))

    # print()
    return low_sent, high_sent


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    start_time = time.time()

    gates = init_gates(lines)
    # for gate in gates:
    #     print(gate, gates[gate])
    # print()

    btn_presses = 0
    
    tot_l = tot_h = 0
    for _ in range(1000):
        l, h = sim_gates(gates, pt2=False)
        tot_l += l
        tot_h += h
    pt1 = tot_l*tot_h

    gates = init_gates(lines)
    pt2 = sim_gates(gates, pt2=True)


    end_time = time.time()
    print(f"Solution Pt1: {pt1}")
    print(f"Solution Pt2: {pt2}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
