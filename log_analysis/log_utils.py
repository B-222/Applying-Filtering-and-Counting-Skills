def filter_by_level(lines, wanted_level):
    filtered = []
    for line in lines:
        parts = line.split("|")
        if len(parts) < 3:
            continue  # skip malformed lines
        level = parts[1].strip()
        if level == wanted_level:
            filtered.append(line)
    return filtered

def count_levels(lines):
    counts = {}
    for line in lines:
        parts = line.split("|")
        if len(parts) < 3:
            continue
        level = parts[1].strip()
        counts[level] = counts.get(level, 0) + 1
    return counts

def count_services(lines):
    counts = {}
    for line in lines:
        parts = line.split("|")
        if len(parts) < 3:
            continue
        service = parts[2].strip()
        counts[service] = counts.get(service, 0) + 1
    return counts
