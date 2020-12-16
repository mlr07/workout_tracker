import os
import sys
import csv
import shutil
import operator


def write(file, row):
    """
    Enter a record of data to file in a+ mode.

    Args:
        file (csv): file to write to
        row (list): entry to write
    """
    with open(file, mode="a+", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerow(row)

    print(f"data wrote to {file}")


def copy(file):
    """
    Make copy of csv file in current working directory.

    Args:
        file (csv): file to copy
    """

    current_dir = os.getcwd()
    orig_file_path = os.path.join(current_dir, file)

    copy_file = "copy_"+file
    copy_file_path = os.path.join(current_dir, copy_file)

    shutil.copyfile(orig_file_path, copy_file_path)

    print(f"{file} copied to {copy_file}")


def sort(file):
    """
    Sort data in file alphabetically with first key.

    Args:
        file (csv): file to sort
    """

    with open(file, mode="r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)

    data = sorted(data, key=operator.itemgetter(0))

    with open(file, mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)

    print(f"{file} has been sorted by date")


def undo(file):
    """
    Undo last entry inserted in file.

    Args:
        file (csv): file to undo
    """

    with open(file, mode="r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        data = list(reader)

    data = data[:-1]

    with open(file, mode="w", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(data)

    print(f"last entry removed from {file}")


def main():
    args = sys.argv
    args = [arg.lower() for arg in args]

    print(f"utils args: {args}")

    action = args[1]
    file = args[2]

    if action == "copy":
        copy(file)

    elif action == "sort":
        sort(file)

    elif action == "undo":
        undo(file)


if __name__ == "__main__":
    main()
