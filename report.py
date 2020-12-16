import pandas as pd
import sys


def load_data(file):
    """
    Load workout data file to dataframe.

    Args:
        file (csv): file to load and process
    """

    cols = ["date", "type", "time", "reps"]
    df = pd.read_csv(file, names=cols)
    df = df.astype({"type": "category"})

    return df


def report(df):
    """
    Aggregate workout data and print results.

    Args:
        df (df): df of workout data
    """
    cats = list(df["type"].unique())

    results = {}

    for c in cats:
        mask = df["type"] == c
        df_mask = df[mask]

        total = df_mask["time"].count()
        time = df_mask["time"].sum()
        reps = df_mask["reps"].sum()

        results[c] = [total, time, reps]

        if c == "kb":
            results[c].append("swings")
        elif c == "bike":
            results[c].append("miles")
        elif c == "yoga":
            results[c].append("flow")
        else:
            results[c].append("unknown")

    return results


def main():
    args = sys.argv
    args = [arg.lower() for arg in args]

    print(f"describe args: {args}")

    file = args[1]

    df = load_data(file)

    results = report(df)

    for k, v in results.items():
        print(k, v)


if __name__ == "__main__":
    main()
