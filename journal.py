import os


def load(name):
    """

    :param name: The basename of the journal file to load from.
    :return: Returns a journal data structure populated with data from the file.  List type.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    """

    :param name: The name of the journal file to save to.
    :param journal_data: Journal data passed in from the UI.
    :return: Does not return anything -- saves to a file and closes.
    """
    filename = get_full_pathname(name)
    print(f"Saving to: {filename}")

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.jrl'))
    return filename


def add_entry(text, journal_data):
    journal_data.append(text)
