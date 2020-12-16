import sys
import utils

from datetime import date


def main():
    args = sys.argv
    args = [arg.lower() for arg in args]
    file = "workout_data.csv"

    print(f"pt_tracker args: {args}")

    # parse time
    if args[1] == "now":
        time = date.today().strftime("%Y-%m-%d")
    else:
        time = args[1]

    row = [time, args[2], args[3], args[4]]

    print(f"row: {row}")

    utils.write(file, row)


if __name__ == "__main__":
    main()
