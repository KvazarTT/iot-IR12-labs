class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @classmethod
    def process_tree_from_txt(cls, filename: str):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read().strip()

            if not content:
                print("Я мучаю котят")
                return None

            clean_content = content.replace('[', '').replace(']', '').strip()
            if not clean_content:
                print("Я мучаю котят")
                return None

            raw_elements = clean_content.split(',')
            arr = []
            for el in raw_elements:
                el = el.strip()
                if el.lower() in ('none', 'null', ''):
                    arr.append(None)
                else:
                    arr.append(int(el))
        except FileNotFoundError:
            print(f"Помилка: Файл '{filename}' не знайдено.")
            return None
        except ValueError:
            print("Помилка: У файлі мають бути числа, розділені комами.")
            return None

        while arr and arr[-1] is None:
            arr.pop()

        if not arr:
            print("Я мучаю котят")
            return None

        root = cls(arr[0])
        queue = [root]
        i = 1

        while queue and i < len(arr):
            current = queue.pop(0)

            if i < len(arr):
                if arr[i] is not None:
                    current.left = cls(arr[i])
                    queue.append(current.left)
                i += 1

            if i < len(arr):
                if arr[i] is not None:
                    current.right = cls(arr[i])
                    queue.append(current.right)
                i += 1

        print("Отримане дерево:")
        def print_in_order(node):
            if node is None:
                return
            print_in_order(node.left)
            print(node.value, end=" ")
            print_in_order(node.right)

        print_in_order(root)
        print("\n\nСтруктура дерева:\n")

        def display(root_node):
            if not root_node:
                print("Дерево порожнє")
                return

            def get_h(node):
                if not node: return 0
                return max(get_h(node.left), get_h(node.right)) + 1

            h = get_h(root_node)
            col_width = 7
            width = (2 ** h) * col_width
            matrix = [[" " for _ in range(width)] for _ in range(h * 2)]

            def place(r, c, txt):
                s = str(txt)
                start_c = c - len(s) // 2
                for idx, char in enumerate(s):
                    if 0 <= start_c + idx < width:
                        matrix[r][start_c + idx] = char

            def fill(node, r, c, curr_h):
                if not node:
                    place(r, c, "nul")
                    return
                place(r, c, node.value)
                if curr_h > 1:
                    step = int(2 ** (curr_h - 2) * 2)
                    matrix[r + 1][c - step // 2] = "/"
                    fill(node.left, r + 2, c - step, curr_h - 1)
                    matrix[r + 1][c + step // 2] = "\\"
                    fill(node.right, r + 2, c + step, curr_h - 1)

            fill(root_node, 0, width // 2, h)

            for row in matrix:
                line = "".join(row).rstrip()
                if line:
                    print(line)

        display(root)

        print("\n")
        is_balanced = is_tree_balanced(root)
        print(f"Чи збалансоване дерево: {'Так' if is_balanced else 'Ні'}")
        return root

def is_tree_balanced(node: BinaryTree) -> bool:
    def check_height(current_node: BinaryTree) -> int:
        if current_node is None:
            return 0

        left_height = check_height(current_node.left)
        if left_height == -1:
            return -1

        right_height = check_height(current_node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
    return check_height(node) != -1


if __name__ == "__main__":
    BinaryTree.process_tree_from_txt('array1.txt')