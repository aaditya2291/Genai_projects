import pandas as pd


class AnimeDataLoader:
    """
    Docstring for AnimeDataLoader
    this class gets data and process that data
    """
    def __init__(self, original_csv, processed_csv):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        """
        Docstring for load_and_process
        
        :param self: Description
        """
        df = pd.read_csv(
            self.original_csv, encoding="utf-8", error_bad_lines=False
        ).dropna(inplace=True)

        required_cols = {"Name", "Genres", "sypnopsis"}
        df = df[[required_cols]]

        df["combined_info"] = (
            "Title:"
            + df["Name"]
            + "Genres: "
            + df["Genres"]
            + "synopsis: "
            + df["sypnopsis"]
        )

        df[["combined_info"]].to_csv(self.processed_csv, encoding="utf-8", index=False)

        return self.processed_csv
