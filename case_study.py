# q16_mapping.py
# Q16: Mapping Functions Case Study
# Compare Direct, Set-Associative, and Fully Associative mapping
# across the three workload types

from main import run_simulation
from functions import calculate_rates, get_num_of_set

BLOCK_SIZE = 16
CACHE_SIZE = 64          # 64 bytes / 16 = 4 slots
POLICY = "LRU"

# Workloads (same strings as Q14)
SEQUENTIAL = [0, 16, 32, 48, 64, 80, 96, 112,
              128, 144, 160, 176, 192, 208, 224, 240]

LOCALITY = [0, 16, 0, 16, 0, 16, 32, 32, 0, 16, 0, 16, 0, 16]

CONFLICT = [0, 64, 128, 192, 0, 64, 128, 192, 0, 64, 128, 192]

WORKLOADS = {
    "sequential": SEQUENTIAL,
    "locality":   LOCALITY,
    "conflict":   CONFLICT,
}

# Mapping functions expressed as associativity values
# 1 = direct, 2 = 2-way set-assoc, 4 = fully associative (all 4 slots in 1 set)
MAPPINGS = {
    "Direct (1-way)":        1,
    "Set-Assoc (2-way)":     2,
    "Fully Assoc (4-way)":   4,
}


def run_q16():
    results = []

    for workload_name, addresses in WORKLOADS.items():
        for mapping_name, assoc in MAPPINGS.items():
            hits, misses = run_simulation(
                CACHE_SIZE, BLOCK_SIZE, assoc, POLICY,
                addresses, verbose=False
            )
            hit_rate, miss_rate = calculate_rates(hits, misses)
            num_sets = get_num_of_set(CACHE_SIZE, BLOCK_SIZE, assoc)

            results.append({
                "workload": workload_name,
                "mapping": mapping_name,
                "assoc": assoc,
                "sets": num_sets,
                "references": len(addresses),
                "hits": hits,
                "misses": misses,
                "hit_rate": hit_rate,
                "miss_rate": miss_rate,
            })

    return results


def print_q16_table(results):
    header = (f"{'Workload':<12} {'Mapping':<22} {'Sets':>5} "
              f"{'Refs':>5} {'Hits':>5} {'Miss':>5} {'Hit%':>8}")
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['workload']:<12} {r['mapping']:<22} {r['sets']:>5} "
              f"{r['references']:>5} {r['hits']:>5} {r['misses']:>5} "
              f"{r['hit_rate']:>8.2f}")


def print_q16_tsv(results):
    print("Workload\tMapping\tSets\tReferences\tHits\tMisses\tHit rate")
    for r in results:
        print(f"{r['workload']}\t{r['mapping']}\t{r['sets']}\t"
              f"{r['references']}\t{r['hits']}\t{r['misses']}\t{r['hit_rate']}")


if __name__ == "__main__":
    results = run_q16()
    print_q16_table(results)
    print()
    print_q16_tsv(results)