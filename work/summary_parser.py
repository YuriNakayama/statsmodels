import pandas as pd
import re


class summary_parser:
    def __init__(self, summary):
        self.summary = summary
        self.summary_dfs = [pd.DataFrame(table.data) for table in summary.tables]
        self.summary_dfs[0] = self.summary02shaping(self.summary_dfs[0])
        self.summary_dfs[1] = self.summary1shaping(self.summary_dfs[1])
        self.summary_dfs[2] = self.summary02shaping(self.summary_dfs[2])

    def summary02shaping(self, summary):
        dfs = []
        dfs.append(summary.iloc[:, 0:2])
        dfs.append(summary.loc[:, 2:4])
        dfs[0].columns = ["index", "value"]
        dfs[1].columns = ["index", "value"]
        summary = pd.concat(dfs, axis=0)
        summary.set_index("index", drop=True, inplace=True)
        summary.index = [
            str(_index).replace("\t", "").replace(" ", "").replace(":", "")
            for _index in summary.index
        ]
        return summary[summary["value"] != " "]

    def summary1shaping(self, summary):
        columns = summary.iloc[0, :][1:]
        columns = [
            str(column).replace("[", "").replace("]", "").replace(" ", "")
            for column in columns
        ]
        index = summary.iloc[:, 0][1:]
        summary = summary.drop(0).drop(0, axis=1)
        summary.columns = columns
        summary.index = index
        summary.index = [
            str(_index).replace("\t", "").replace(" ", "").replace(":", "")
            for _index in summary.index
        ]
        return summary

    def make_df(self):
        summary_dfs = [_df.copy() for _df in self.summary_dfs]
        index = pd.MultiIndex.from_tuples(
            [(_index, "") for _index in summary_dfs[0].index]
        )
        summary_dfs[0].index = index
        index = pd.MultiIndex.from_tuples(
            [(_index, "") for _index in summary_dfs[2].index]
        )
        summary_dfs[2].index = index
        df = pd.concat(
            [
                summary_dfs[0],
                pd.DataFrame(summary_dfs[1].stack(), columns=["value"]),
                summary_dfs[2],
            ]
        )
        return df




