import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


class OrchestraSeason():

    def __init__(self, orchestra_csv: str) -> None:
        self.season = pd.read_csv(orchestra_csv, na_values=999)

    def reformat(self):
        '''Reformats column names, replaces empty entries as np.nan'''
        self.season.columns = self.season.columns.str.strip().str.lower()
        self.season.replace(' ', np.nan, inplace=True)
        return self

    def split_composer_arranger(self):
        '''Splits entry of composer/arranger into separate columns'''
        comp_arr = self.season['composer'].str.split('/', expand=True)
        self.season[['composer', 'arranger']] = comp_arr
        return self

    def unknown_as_nan(self):
        '''Unknown composers are marked as np.nan in comp.code'''
        self.season.loc[self.season['comp.code'].isna() | self.season['composer'].str.contains('Unknown'),
                        ['comp.code', 'comp.live']] = np.nan
        return self


class GeneralAnalysis():

    @staticmethod
    def count_nan(season: pd.DataFrame):
        '''Counts number of nan per column'''
        return season.isna().sum()

    @staticmethod
    def count_of_performances(season: pd.DataFrame, plot=True, **plt_kwargs):
        '''Shows stats of counts of performances, and plots distribution'''
        if 'ensemble' not in season:
            raise KeyError('DataFrame does not have column "ensemble"')
        counts = season['ensemble'].value_counts()
        if plot:
            counts.plot.hist(**plt_kwargs)
        return counts.describe()

    @staticmethod
    def most_performed_composer(season: pd.DataFrame, n=10):
        '''Plots counts of performances vs. composer (top n)'''
        if 'composer' not in season:
            raise KeyError('DataFrame does not have column "composer"')
        (season['composer']
         .value_counts()
         .head(n)
         .plot.barh())

    @staticmethod
    def most_performed_type_of_work(season: pd.DataFrame, n=20, figsize=(8, 6)):
        '''Proxy (inferred from title of work). Plots counts of occurrence vs. word.'''
        if 'work' not in season:
            raise KeyError('DataFrame does not have column "work"')
        (season['work'].str.lower().str.split(expand=True)
         .stack()
         .value_counts()
         .head(n)
         .plot.barh(figsize=figsize))

    @staticmethod
    def composer_arranger_demographics(season: pd.DataFrame, figsize=(12, 8)):
        '''Plots normalized counts of performances vs. composer and arranger demographics (codes).'''
        _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=figsize)

        for col, ax in zip(['comp.code', 'comp.live', 'arr.code', 'arr.live'], [ax1, ax2, ax3, ax4]):
            if col not in season:
                raise KeyError(f'DataFrame does not have column "{col}"')
            season[col].value_counts(normalize=True).plot.bar(ax=ax)
            ax.set_title(col)

    @staticmethod
    def lao_group(season: pd.DataFrame):
        '''Plots counts of performances vs. LAO group represented in the dataset.'''
        if 'lao.group' not in season:
            raise KeyError('DataFrame does not have column "lao.group"')
        (season['lao.group']
         .value_counts()
         .sort_index()
         .plot.bar())

    @staticmethod
    def _():
        pass
