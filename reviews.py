import pandas as pd
from statistics import mean

INPUT_PATH = "data/winemag-data-130k-v2.csv.zip"
OUTPUT_PATH = "data/reviews-per-country.csv"

def wrangle(datapath) -> pd.DataFrame:
    # import data
    reviews = pd.read_csv(datapath)
    # get relevant information
    out = reviews.groupby("country").points.agg([len, mean])
    # clean up dataframe/ format it as expected
    out = out.rename(columns={"len":"count", "mean":"points"})
    out.points = out.points.apply(lambda x: round(x, ndigits=1))

    return out


def main():
    # wrangle that data
    df = wrangle(INPUT_PATH)
    # output to CSV file
    df.to_csv(OUTPUT_PATH)

if __name__ == "__main__":
    main()

