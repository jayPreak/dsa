def min_lightbulbs(M, R, street_lights):
    idx = 0
    bulbs_needed = 0
    remaining_area = 0

    while remaining_area < M:
        last_idx = -1
        while idx < len(street_lights) and street_lights[idx] - R <= remaining_area:
            last_idx = idx
            idx += 1

        if last_idx == -1:
            return "IMPOSSIBLE"

        remaining_area = street_lights[last_idx] + R
        bulbs_needed += 1

    return bulbs_needed


def main():
    T = int(input().strip())
    for t in range(1, T + 1):
        M, R, N = map(int, input().strip().split())
        street_lights = list(map(int, input().strip().split()))
        result = min_lightbulbs(M, R, street_lights)
        print(f"Case #{t}: {result}")


if __name__ == "__main__":
    main()
