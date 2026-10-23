from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def run_menu(structure, kind):
    while True:
        print("\n1. Insert (Push/Enqueue)")
        print("2. Remove (Pop/Dequeue)")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Display")
        print("0. Back")

        choice = input("Choose operation: ")

        try:
            if choice == "1":
                value = input("Enter value: ")
                structure.push(value) if kind == "stack" \
                    else structure.enqueue(value)
                print("Value inserted successfully.")

            elif choice == "2":
                value = structure.pop() if kind == "stack" \
                    else structure.dequeue()
                print("Removed:", value)

            elif choice == "3":
                value = structure.peek() if kind == "stack" \
                    else structure.peek_front()
                print("Top/Front:", value)

            elif choice == "4":
                print("Is empty:", structure.is_empty())

            elif choice == "5":
                print("Is full:", structure.is_full())

            elif choice == "6":
                structure.display()

            elif choice == "0":
                break

            else:
                print("Invalid choice.")

            structure.display()

        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)


def balanced_parentheses(expression):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def print_queue_simulation():
    from collections import deque

    jobs = deque()

    while True:
        print("\n1. Add print job")
        print("2. Process next job")
        print("3. Display waiting jobs")
        print("0. Back")

        choice = input("Choose: ")

        if choice == "1":
            job_id = input("Enter job ID: ")
            pages = int(input("Enter number of pages: "))

            if pages <= 0:
                print("Page count must be positive.")
                continue

            jobs.append({"id": job_id, "pages": pages})
            print("Job added. Position in queue:", len(jobs))

        elif choice == "2":
            if not jobs:
                print("Queue underflow: no print jobs.")
            else:
                job = jobs.popleft()
                print(
                    "Printing job:", job["id"],
                    "| Pages:", job["pages"]
                )

        elif choice == "3":
            if not jobs:
                print("No waiting jobs.")
            else:
                print("Waiting order:")
                for position, job in enumerate(jobs, start=1):
                    print(
                        position, "-", job["id"],
                        "| Pages:", job["pages"]
                    )

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n=== STACKS AND QUEUES ===")
        print("1. Array Stack")
        print("2. Linked Stack")
        print("3. Circular Array Queue")
        print("4. Linked Queue")
        print("5. Balanced Parentheses")
        print("6. Print Queue Simulation")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            run_menu(ArrayStack(3), "stack")

        elif choice == "2":
            run_menu(LinkedStack(), "stack")

        elif choice == "3":
            run_menu(ArrayQueue(3), "queue")

        elif choice == "4":
            run_menu(LinkedQueue(), "queue")

        elif choice == "5":
            expression = input("Enter an expression: ")
            if balanced_parentheses(expression):
                print("The parentheses are balanced.")
            else:
                print("The parentheses are not balanced.")

        elif choice == "6":
            print_queue_simulation()

        elif choice == "0":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()