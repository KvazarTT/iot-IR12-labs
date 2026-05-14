def find_shortest_path(n, start, dest):
    if start == dest:
        return 0

    queue = [(start[0], start[1], 0)]
    visited = set()
    visited.add(start)

    moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]

    while len(queue) > 0:
        current_x, current_y, current_dist = queue.pop(0)
        for dx, dy in moves:
            next_x = current_x + dx
            next_y = current_y + dy
            if 0 <= next_x < n and 0 <= next_y < n:
                if (next_x, next_y) == dest:
                    return current_dist + 1
                if (next_x, next_y) not in visited:
                    visited.add((next_x, next_y))
                    queue.append((next_x, next_y, current_dist + 1))
    return -1

if __name__ == '__main__':
    try:
        with open('input.txt', 'r', encoding='utf-8') as file_in:
            lines = file_in.readlines()
        n = int(lines[0].split('#')[0].strip())

        start_str = lines[1].split('#')[0].replace(',', ' ').split()
        start = (int(start_str[0]), int(start_str[1]))
        target_str = lines[2].split('#')[0].replace(',', ' ').split()
        target = (int(target_str[0]), int(target_str[1]))

        result = find_shortest_path(n, start, target)

        with open('output.txt', 'w', encoding='utf-8') as file_out:
            file_out.write(str(result))
        print(f"Результат: {result}. Записано у файл output.txt")
    except FileNotFoundError:
        print("Файл input.txt не знайдено. Створи його перед запуском.")