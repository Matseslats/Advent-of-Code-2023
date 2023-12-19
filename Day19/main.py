import time
import json

def get_rule(rule):
    condition, dest = rule.split(":")
    part_type = None
    operand = None
    if "<" in condition:
        condition = condition.split("<")
        operand = "<"
    elif ">" in condition:
        condition = condition.split(">")
        operand = ">"
    part_type = condition[0]
    value_check = condition[1]
    return {
        "part_type": part_type,
        "operand": operand,
        "value_check": int(value_check),
        "dest": dest
    }

def get_rules(line):
    key, values = line.split("{")
    values = values[:-1].split(",")
    int_rules = values[:-1]
    int_rules = [get_rule(rule) for rule in int_rules]
    dest = values[-1]
    rule = {
        "key": key,
        "int_rules": int_rules,
        "dest": dest
    }
    return rule


def get_vars(line):
    vars = {}
    line = line[1:-1].split(",")
    for var in line:
        var = var.split("=")
        vars[var[0]] = int(var[1])
    return vars


def accept_or_reject(conditions, rules):
    # print(conditions)
    key = "in"
    while True:
        # print(key)
        if key == "A":
            return sum(conditions.values())
            pass
        elif key == "R":
            return 0
            pass

        # Match the condition to a rule
        # print("Key not accepted or rejected")
        # print(conditions)
        rule = rules[key]
        # If it passes all int_riles, update the key
        # print(rule)
        start_key = key
        for int_rule in rule["int_rules"]:
            # print(int_rule)
            if int_rule["operand"] == "<":
                if int_rule["value_check"] > conditions[int_rule["part_type"]]:
                    key = int_rule["dest"]
                    # print("Found", key)
                    break
            elif int_rule["operand"] == ">":
                # print(int_rule["value_check"], conditions[int_rule["part_type"]])
                if int_rule["value_check"] < conditions[int_rule["part_type"]]:
                    key = int_rule["dest"]
                    # print("Found", key)
                    break
        
        if start_key == key:
            # print("Default key")
            # Part not found, use default
            key = rule["dest"]
    print("Exiting...")
    exit()


if __name__ == "__main__":
    lines = []
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    start_time = time.time()
    is_rule = True
    rules = {}
    tot_sum = 0
    for line in lines:
        if line == "":
            is_rule = False
            continue
        if is_rule:
            rule = get_rules(line)
            rules[rule["key"]] = rule 
        else:
            tot_sum += accept_or_reject(get_vars(line), rules)
            # print(tot_sum)

    end_time = time.time()
    print(f"Solution Pt1: {tot_sum}")
    # print(f"Solution Pt2: {loss_pt2}")
    # print(f"Solution Pt2: {max_energized}")
    print(f"Took {((end_time - start_time) * 1000):.4}ms")
