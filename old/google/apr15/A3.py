def find_color_order(N, colors):
    last_color = colors[0]
    color_order = [last_color]
    impossible = False

    for i in range(1, N):
        if colors[i] != last_color:
            if last_color > colors[i]:
                impossible = True
                break
            last_color = colors[i]
            color_order.append(last_color)

    if impossible:
        return "IMPOSSIBLE"
    else:
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
