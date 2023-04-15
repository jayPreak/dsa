def find_color_order(N, colors):
    color_dict = {}
    last_written = {}

    for i, color in enumerate(colors):
        if color not in color_dict:
            color_dict[color] = [i]
        else:
            color_dict[color].append(i)

    color_order = sorted(color_dict.keys())

    for i in range(len(color_order)):
        indices = color_dict[color_order[i]]
        if i == 0:
            last_written[color_order[i]] = indices[-1]
        else:
            prev_color = color_order[i - 1]
            if indices[0] <= last_written[prev_color]:
                return "IMPOSSIBLE"
            last_written[color_order[i]] = indices[-1]

    return " ".join(str(color) for color in color_order)


def main():
    T = int(input().strip())
    for t in range(1, T + 1):
        N = int(input().strip())
        colors = list(map(int, input().strip().split()))
        result = find_color_order(N, colors)
        print(f"Case #{t}: {result}")


if __name__ == "__main__":
    main()
