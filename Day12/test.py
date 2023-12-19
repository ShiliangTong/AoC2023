def early_termination(string, pos, required_groups, current_group, current_groups):
    # Early termination: If the current group size exceeds the corresponding required group size
    if current_group > 0 and current_group > required_groups[len(current_groups)]:
        return []

    # If we have processed the entire string
    if pos == len(string):
        if current_group > 0:
            current_groups.append(current_group)
        return [string] if current_groups == required_groups else []

    if string[pos] != '?':
        # Continue with the current group or start a new group
        return early_termination(string, pos + 1, required_groups, 
                                 current_group + 1 if string[pos] == '#' else 0, 
                                 current_groups + [current_group] if string[pos] == '.' and current_group > 0 else current_groups)

    # Replace '?' with '#' and '.'
    arrangements = []
    arrangements.extend(early_termination(string[:pos] + '#' + string[pos + 1:], pos + 1, required_groups, current_group + 1, current_groups))
    if current_group > 0:
        arrangements.extend(early_termination(string[:pos] + '.' + string[pos + 1:], pos + 1, required_groups, 0, current_groups + [current_group]))
    else:
        arrangements.extend(early_termination(string[:pos] + '.' + string[pos + 1:], pos + 1, required_groups, 0, current_groups))

    return arrangements

# Test the function
test_string = "?###????????"
required_groups = [3, 2, 1]
valid_arrangements = early_termination(test_string, 0, required_groups, 0, [])
valid_arrangements, len(valid_arrangements)
