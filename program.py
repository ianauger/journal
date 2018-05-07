import journal


def print_header():
    print('-'*20)
    print('Journal App'.center(20))
    print('-'*20)


def run_event_loop():
    print('What would you like to do with your journal?')
    cmd = 'EMPTY'
    journal_name = input("Enter the name of the journal you'd like to edit > ")
    journal_data = journal.load(journal_name)

    while cmd != "x" and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, or E[x]it? > ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print(f"{cmd} isn't a valid imput.")

    print("Exiting, goodbye.")
    journal.save(journal_name, journal_data)


def list_entries(data):
    print("Journal entries: ")
    for i, entry in enumerate(data):
        print(f"{i+1}. {entry}")


def add_entry(data):
    text = input('Type your entry, <enter> to finalize > ')
    journal.add_entry(text, data)
    # data.append(text)


def main():
    print_header()
    run_event_loop()


if __name__ == "__main__":
    main()
