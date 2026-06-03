import csv
import copy

# ----------------------------
# Journey 1 Routes
# Vauxhall -> Mile End
# ----------------------------

route1 = {
    "name": "J1 Route 1",
    "start": "Vauxhall",
    "end": "Mile End",
    "lines": ["Victoria", "District"],
    "interchanges": [
        {
            "station": "Victoria",
            "complexity": "high",
            "lifts_required": 7
        }
    ],
    "estimated_time_mins": 32,
    "start_step_free": True,
    "destination_step_free": False,
    "notes": "Google Maps marked as accessible but Mile End is not fully step-free"
}

route2 = {
    "name": "J1 Route 2",
    "start": "Vauxhall",
    "end": "Mile End",
    "lines": ["Victoria", "Jubilee", "Bus D7"],
    "interchanges": [
        {
            "station": "Green Park",
            "complexity": "medium",
            "lifts_required": 2
        },
        {
            "station": "Canary Wharf",
            "complexity": "medium",
            "lifts_required": 3
        }
    ],
    "estimated_time_mins": 56,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Fully step-free journey via Green Park and Canary Wharf"
}

route3 = {
    "name": "J1 Route 3",
    "start": "Vauxhall",
    "end": "Mile End (Bus Stop)",
    "lines": ["Bus 196", "Northern", "DLR", "Bus D7"],
    "interchanges": [
        {
            "station": "Bank",
            "complexity": "high",
            "lifts_required": 4
        },
        {
            "station": "Westferry",
            "complexity": "low",
            "lifts_required": 2
        }
    ],
    "estimated_time_mins": 55,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Bus and DLR alternative via Nine Elms and Westferry — destination reached by bus, fully step-free"
}

# ----------------------------
# Journey 2 Routes
# Wembley Park -> Elephant & Castle
# ----------------------------

j2_route1 = {
    "name": "J2 Route 1",
    "start": "Wembley Park",
    "end": "Elephant & Castle (Bus Stop)",
    "lines": ["Jubilee", "Bus BL1"],
    "interchanges": [
        {
            "station": "Waterloo",
            "complexity": "high",
            "lifts_required": 3
        }
    ],
    "estimated_time_mins": 45,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "High complexity interchange but fully step-free"
}

j2_route2 = {
    "name": "J2 Route 2",
    "start": "Wembley Park",
    "end": "Elephant & Castle",
    "lines": ["Metropolitan", "Bakerloo"],
    "interchanges": [
        {
            "station": "Baker Street",
            "complexity": "high",
            "lifts_required": 2
        }
    ],
    "estimated_time_mins": 40,
    "start_step_free": True,
    "destination_step_free": False,
    "notes": "Destination not step-free from Bakerloo line"
}

j2_route3 = {
    "name": "J2 Route 3",
    "start": "Wembley Park",
    "end": "Elephant & Castle (Bus Stop)",
    "lines": ["Metropolitan", "Bus 63", "Bus 40"],
    "interchanges": [
        {
            "station": "King's Cross St. Pancras",
            "complexity": "high",
            "lifts_required": 4
        },
        {
            "station": "Farringdon",
            "complexity": "medium",
            "lifts_required": 2
        }
    ],
    "estimated_time_mins": 62,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Long but fully accessible journey"
}

# ----------------------------
# Journey 3 Routes
# Kingsbury -> Paddington
# ----------------------------

j3_route1 = {
    "name": "J3 Route 1",
    "start": "Kingsbury",
    "end": "Paddington",
    "lines": ["Jubilee", "Elizabeth"],
    "interchanges": [
        {
            "station": "Green Park",
            "complexity": "medium",
            "lifts_required": 2
        },
        {
            "station": "Bond Street",
            "complexity": "medium",
            "lifts_required": 2
        }
    ],
    "estimated_time_mins": 60,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Fully step-free via Green Park and Bond Street to Elizabeth line"
}

j3_route2 = {
    "name": "J3 Route 2",
    "start": "Kingsbury",
    "end": "Paddington",
    "lines": ["Jubilee", "Bakerloo"],
    "interchanges": [
        {
            "station": "Baker Street",
            "complexity": "high",
            "lifts_required": 4
        }
    ],
    "estimated_time_mins": 35,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Faster route but Baker Street is a high complexity interchange with significant lift dependency"
}

j3_route3 = {
    "name": "J3 Route 3",
    "start": "Kingsbury",
    "end": "Paddington",
    "lines": ["Jubilee", "Bus 16"],
    "interchanges": [
        {
            "station": "Kilburn",
            "complexity": "low",
            "lifts_required": 1
        }
    ],
    "estimated_time_mins": 61,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Bus alternative via Kilburn — low complexity, minimal lift dependency, fully step-free"
}

# ----------------------------
# Journey 4 Routes
# Canary Wharf -> King's Cross St. Pancras
# ----------------------------

j4_route1 = {
    "name": "J4 Route 1",
    "start": "Canary Wharf",
    "end": "King's Cross St. Pancras",
    "lines": ["Elizabeth", "Circle / H&C / Metropolitan"],
    "interchanges": [
        {
            "station": "Farringdon",
            "complexity": "medium",
            "lifts_required": 2
        }
    ],
    "estimated_time_mins": 27,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Fastest route — single medium complexity interchange at Farringdon, fully step-free"
}

j4_route2 = {
    "name": "J4 Route 2",
    "start": "Canary Wharf",
    "end": "King's Cross St. Pancras",
    "lines": ["DLR", "Northern"],
    "interchanges": [
        {
            "station": "Bank",
            "complexity": "high",
            "lifts_required": 4
        }
    ],
    "estimated_time_mins": 26,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Marginally fastest but Bank is a high complexity interchange despite step-free upgrades completing in February 2023"
}

j4_route3 = {
    "name": "J4 Route 3",
    "start": "Canary Wharf",
    "end": "King's Cross St. Pancras",
    "lines": ["Jubilee", "Circle / H&C"],
    "interchanges": [
        {
            "station": "Baker Street",
            "complexity": "high",
            "lifts_required": 4
        }
    ],
    "estimated_time_mins": 36,
    "start_step_free": True,
    "destination_step_free": True,
    "notes": "Slower route via Baker Street — high complexity interchange, significant lift dependency"
}

# Core Logic

def compute_risk(route, weights=None):
    if weights is None:
        weights = {
            "interchange_base": 1,
            "complexity_high": 4,
            "complexity_medium": 2,
            "complexity_low": 1,
            "lift_high": 5,
            "lift_moderate": 3,
            "lift_low": 1,
            "destination_penalty": 14
        }

    if not route.get("start_step_free", True):
        return 25, ["Start is not step-free, journey not feasible!"]

    risk = 0
    reasons = []

    interchange_count = len(route["interchanges"])
    risk += interchange_count * weights["interchange_base"]
    if interchange_count > 0:
        reasons.append(f"{interchange_count} interchange(s) (+{interchange_count * weights['interchange_base']})")

    for interchange in route["interchanges"]:
        if interchange["complexity"] == "high":
            risk += weights["complexity_high"]
            reasons.append(f"{interchange['station']} is high complexity (+{weights['complexity_high']})")
        elif interchange["complexity"] == "medium":
            risk += weights["complexity_medium"]
            reasons.append(f"{interchange['station']} is medium complexity (+{weights['complexity_medium']})")
        elif interchange["complexity"] == "low":
            risk += weights["complexity_low"]
            reasons.append(f"{interchange['station']} is low complexity (+{weights['complexity_low']})")

    total_lifts = sum(i["lifts_required"] for i in route["interchanges"])
    if total_lifts >= 5:
        risk += weights["lift_high"]
        reasons.append(f"High lift dependency ({total_lifts} lifts) (+{weights['lift_high']})")
    elif total_lifts >= 2:
        risk += weights["lift_moderate"]
        reasons.append(f"Moderate lift dependency ({total_lifts} lifts) (+{weights['lift_moderate']})")
    elif total_lifts == 1:
        risk += weights["lift_low"]
        reasons.append(f"Low lift dependency (1 lift) (+{weights['lift_low']})")

    if not route["destination_step_free"]:
        risk += weights["destination_penalty"]
        reasons.append(f"Destination is not step-free (+{weights['destination_penalty']})")

    return risk, reasons


def normalize_risk(raw_score, max_score=25):
    return round(min((raw_score / max_score) * 10, 10), 1)


def classify_risk(score):
    if score >= 7:
        return "HIGH"
    elif score >= 4:
        return "MEDIUM"
    return "LOW"


def print_route(route):
    raw_score, reasons = compute_risk(route)
    normalized_score = normalize_risk(raw_score)

    if not route.get("start_step_free", True):
        print(f"\n=== {route['name']} ===")
        print("Journey not feasible")
        return

    risk_label = classify_risk(normalized_score)

    print(f"\n {route['name']}")
    print(f"Time: {route['estimated_time_mins']} mins")
    print(f"Risk: {normalized_score}/10 ({risk_label})")

    for r in reasons:
        print(f"  - {r}")


# Journey Evaluation

def evaluate_journey(name, routes):
    print(f"\n============================")
    print(name)
    print(f"============================")

    scored = []

    for route in routes:
        print_route(route)

        if route.get("start_step_free", True):
            raw_score, _ = compute_risk(route)
            score = normalize_risk(raw_score)
            scored.append((route["name"], route["estimated_time_mins"], score))

    print("\n--- Summary ---")
    for r in scored:
        print(f"{r[0]}: {r[1]} mins, risk {r[2]}/10")

    fastest = min(scored, key=lambda x: x[1])
    safest = min(scored, key=lambda x: x[2])

    print(f"\nFastest: {fastest[0]}")
    print(f"Safest: {safest[0]}")

    return scored


# Implementing Disruption Testing
# Minor: short-duration fault, one lift reduced - average repair < 10 hours
# Major: extended outage, interchange rendered impassable - average repair > 20 hours

SEVERITY_LEVELS = ["minor", "major"]

def simulate_disruption(route, disrupted_station, severity="minor"):
    disrupted = copy.deepcopy(route)
    affected = False

    for interchange in disrupted["interchanges"]:
        if interchange["station"] == disrupted_station:
            affected = True

            if severity == "major":
                interchange["lifts_required"] = 0
                disrupted["start_step_free"] = False

            elif severity == "minor":
                if interchange["lifts_required"] == 1:
                    interchange["lifts_required"] = 0
                    disrupted["start_step_free"] = False
                else:
                    interchange["lifts_required"] = max(interchange["lifts_required"] - 1, 0)

    return disrupted, affected


def run_disruption_test(routes, disrupted_station, severity="minor"):
    print(f"\n--- Disruption Scenario: {severity.capitalize()} fault at {disrupted_station} ---")

    results = []

    for route in routes:
        original_raw, _ = compute_risk(route)
        original_score = normalize_risk(original_raw)
        original_class = classify_risk(original_score)

        disrupted_route, affected = simulate_disruption(route, disrupted_station, severity)

        if not affected:
            print(f"\n  {route['name']}: Not affected")
            results.append({
                "route": route["name"],
                "disrupted_station": disrupted_station,
                "severity": severity,
                "base_score": original_score,
                "disrupted_score": original_score,
                "base_class": original_class,
                "disrupted_class": original_class,
                "affected": False,
                "infeasible": False
            })
            continue

        if not disrupted_route.get("start_step_free", True):
            print(f"\n  {route['name']}: INFEASIBLE after {severity} fault at {disrupted_station}")
            results.append({
                "route": route["name"],
                "disrupted_station": disrupted_station,
                "severity": severity,
                "base_score": original_score,
                "disrupted_score": 10.0,
                "base_class": original_class,
                "disrupted_class": "INFEASIBLE",
                "affected": True,
                "infeasible": True
            })
            continue

        disrupted_raw, _ = compute_risk(disrupted_route)
        disrupted_score = normalize_risk(disrupted_raw)
        disrupted_class = classify_risk(disrupted_score)

        classification_changed = original_class != disrupted_class

        print(f"\n  {route['name']}:")
        print(f"    Base score:      {original_score}/10 ({original_class})")
        print(f"    Disrupted score: {disrupted_score}/10 ({disrupted_class})")
        if classification_changed:
            print(f"    ** Classification changed: {original_class} -> {disrupted_class} **")
        else:
            print(f"    Classification stable: {original_class}")

        results.append({
            "route": route["name"],
            "disrupted_station": disrupted_station,
            "severity": severity,
            "base_score": original_score,
            "disrupted_score": disrupted_score,
            "base_class": original_class,
            "disrupted_class": disrupted_class,
            "affected": True,
            "infeasible": False
        })

    return results

# Sensitivity Analysis

DEFAULT_WEIGHTS = {
    "interchange_base": 1,
    "complexity_high": 4,
    "complexity_medium": 2,
    "complexity_low": 1,
    "lift_high": 5,
    "lift_moderate": 3,
    "lift_low": 1,
    "destination_penalty": 14
}

VARIATION = 0.20

def run_sensitivity_analysis(all_routes):
    print("\n============================")
    print("SENSITIVITY ANALYSIS")
    print("============================")

    results = []

    for penalty_name in DEFAULT_WEIGHTS:
        base_value = DEFAULT_WEIGHTS[penalty_name]
        low_value = round(base_value * (1 - VARIATION), 2)
        high_value = round(base_value * (1 + VARIATION), 2)

        print(f"\n-- Varying: {penalty_name} (base={base_value}, -{int(VARIATION*100)}%={low_value}, +{int(VARIATION*100)}%={high_value}) --")

        for route in all_routes:
            if not route.get("start_step_free", True):
                continue

            base_raw, _ = compute_risk(route)
            base_score = normalize_risk(base_raw)
            base_class = classify_risk(base_score)

            low_weights = {**DEFAULT_WEIGHTS, penalty_name: low_value}
            high_weights = {**DEFAULT_WEIGHTS, penalty_name: high_value}

            low_raw, _ = compute_risk(route, weights=low_weights)
            low_score = normalize_risk(low_raw)
            low_class = classify_risk(low_score)

            high_raw, _ = compute_risk(route, weights=high_weights)
            high_score = normalize_risk(high_raw)
            high_class = classify_risk(high_score)

            low_changed = base_class != low_class
            high_changed = base_class != high_class
            stable = not low_changed and not high_changed

            print(f"  {route['name']}: base={base_score} ({base_class}) | "
                  f"-20%={low_score} ({low_class}) | "
                  f"+20%={high_score} ({high_class}) | "
                  f"{'STABLE' if stable else 'CLASS CHANGED'}")

            results.append({
                "route": route["name"],
                "penalty": penalty_name,
                "base_score": base_score,
                "base_class": base_class,
                "low_score": low_score,
                "low_class": low_class,
                "high_score": high_score,
                "high_class": high_class,
                "stable": stable
            })

    return results


#Exporting to CSV

def export_base_scores(all_routes, filename="base_scores.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "route", "start", "end", "time_mins",
            "raw_score", "normalised_score", "classification"
        ])
        writer.writeheader()
        for route in all_routes:
            if not route.get("start_step_free", True):
                continue
            raw, _ = compute_risk(route)
            score = normalize_risk(raw)
            writer.writerow({
                "route": route["name"],
                "start": route["start"],
                "end": route["end"],
                "time_mins": route["estimated_time_mins"],
                "raw_score": raw,
                "normalised_score": score,
                "classification": classify_risk(score)
            })
    print(f"\nBase scores exported to {filename}")


def export_disruption_results(results, filename="disruption_results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "route", "disrupted_station", "severity", "base_score", "disrupted_score",
            "base_class", "disrupted_class", "affected", "infeasible"
        ])
        writer.writeheader()
        writer.writerows(results)
    print(f"Disruption results exported to {filename}")


def export_sensitivity_results(results, filename="sensitivity_results.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "route", "penalty", "base_score", "base_class",
            "low_score", "low_class", "high_score", "high_class", "stable"
        ])
        writer.writeheader()
        writer.writerows(results)
    print(f"Sensitivity results exported to {filename}")


#Testing

def run_manual_testing(route, expected_raw, expected_normalised, expected_class):
    raw, _ = compute_risk(route)
    normalised = normalize_risk(raw)
    classification = classify_risk(normalised)

    raw_ok = raw == expected_raw
    norm_ok = normalised == expected_normalised
    class_ok = classification == expected_class

    print(f"\n Test Case: {route['name']}")
    print(f"Raw:          {raw} (expected {expected_raw}) {'✓' if raw_ok else 'X'}")
    print(f"Normalised:   {normalised} (expected {expected_normalised}) {'✓' if norm_ok else 'X'}")
    print(f"Class:        {classification} (expected {expected_class}) {'✓' if class_ok else 'X'}")


# All Routes

all_routes = [
    route1, route2, route3,
    j2_route1, j2_route2, j2_route3,
    j3_route1, j3_route2, j3_route3,
    j4_route1, j4_route2, j4_route3
]


# Run Base Evaluation

evaluate_journey("Journey 1: Vauxhall -> Mile End", [route1, route2, route3])
evaluate_journey("Journey 2: Wembley Park -> Elephant & Castle", [j2_route1, j2_route2, j2_route3])
evaluate_journey("Journey 3: Kingsbury -> Paddington", [j3_route1, j3_route2, j3_route3])
evaluate_journey("Journey 4: Canary Wharf -> King's Cross St. Pancras", [j4_route1, j4_route2, j4_route3])


# Running the Disruption Tests

print("\n\n============================")
print("DISRUPTION TESTING")
print("============================")

all_disruption_results = []

# Victoria - highest OOS fault count in J1, average repair 26:22 hrs (major severity justified)
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [route1, route2, route3],
        "Victoria",
        severity
    )

# Westferry - low complexity single interchange in J1 Route 3
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [route1, route2, route3],
        "Westferry",
        severity
    )

# Waterloo - 2nd highest OOS fault count, average repair 35:40 hrs
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [j2_route1, j2_route2, j2_route3],
        "Waterloo",
        severity
    )

# King's Cross St. Pancras - 3rd highest OOS fault count, average repair 18:13 hrs
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [j2_route1, j2_route2, j2_route3],
        "King's Cross St. Pancras",
        severity
    )

# Kilburn - single-lift low complexity station
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [j3_route1, j3_route2, j3_route3],
        "Kilburn",
        severity
    )

# Farringdon - medium complexity, moderate repair time (J2)
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [j2_route1, j2_route2, j2_route3],
        "Farringdon",
        severity
    )

# Bank - high complexity, J4 Route 2
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [j4_route1, j4_route2, j4_route3],
        "Bank",
        severity
    )

# Farringdon - J4 Route 1
for severity in SEVERITY_LEVELS:
    all_disruption_results += run_disruption_test(
        [j4_route1, j4_route2, j4_route3],
        "Farringdon",
        severity
    )


#Running Sensitivity Analysis

sensitivity_results = run_sensitivity_analysis(all_routes)


#Exporting to CSV

export_base_scores(all_routes)
export_disruption_results(all_disruption_results)
export_sensitivity_results(sensitivity_results)


#Carrying out testing

print("\n\nMANUAL TEST CASES")

run_manual_testing(route1, 24, 9.6, "HIGH")
run_manual_testing(route2, 11, 4.4, "MEDIUM")
run_manual_testing(route3, 12, 4.8, "MEDIUM")
run_manual_testing(j2_route2, 22, 8.8, "HIGH")
run_manual_testing(j3_route3, 3, 1.2, "LOW")
run_manual_testing(j3_route2, 8, 3.2, "LOW")
run_manual_testing(j3_route1, 9, 3.6, "LOW")
run_manual_testing(j4_route1, 6, 2.4, "LOW")
run_manual_testing(j4_route2, 8, 3.2, "LOW")
run_manual_testing(j4_route3, 8, 3.2, "LOW")