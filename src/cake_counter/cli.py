import argparse

def main():
    parser = argparse.ArgumentParser(description="Cake Counter CLI")
    parser.add_argument('--add', type=int, help='Add cakes to the counter')
    parser.add_argument('--remove', type=int, help='Remove cakes from the counter')
    parser.add_argument('--show', action='store_true', help='Show current cake count')

    args = parser.parse_args()
    count = 0

    try:
        with open('cake_count.txt', 'r') as f:
            count = int(f.read())
    except (FileNotFoundError, ValueError):
        count = 0

    if args.add is not None:
        count += args.add
        print(f"Added {args.add} cakes.")
    if args.remove is not None:
        count -= args.remove
        print(f"Removed {args.remove} cakes.")
    if args.show or (args.add is None and args.remove is None):
        print(f"Current cake count: {count}")

    with open('cake_count.txt', 'w') as f:
        f.write(str(count))

if __name__ == "__main__":
    main()
