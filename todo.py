import View

def main():
    while True:
        View.print_status()
        if View.print_menu():
            break

if __name__ == "__main__":
    main()