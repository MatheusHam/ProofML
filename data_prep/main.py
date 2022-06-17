from functools import cached_property
import pandas as pd


MIN_ROWS: 1000
MAX_ROWS: 100000
NATYPES_PERCENT_LIMIT: 70


class EventsDataFrame():
    version = 1.0
    """ 

    ::Params::
    
    df : pd.Dataframe = Master table containing all past observations of your target

    must have cols:
    y = Your target
    entity = ID related observation
    
    could have cols:
    sample_weight = categorize how important such observation is to your target
    date = Relate your target observation to a periodicity.

    """
    def __init__(
        self,
        df: pd.DataFrame, 
        y_col: str = "y", 
        entity_col: str = "entity", 
        sample_weight_col: str = None,
        date_col: str = None,
    ):
        self.df = df
        self.y_col =  y_col
        self.entity_col = entity_col
        self.sample_weight_col = sample_weight_col
        self.date_col = date_col
        print("Setting up your master table")
        """ 
        Standard checks
        NATypes for columns
        Existence of sample weight, date_col
        Reliable sample weight and date_col
        Grouped Entities
        CV Method for estimator on defined for target
        Correlation Check between each feature and target
        Set Up vectorizer gateway for nans and vectorizer for high_cat, low_cat and numerical
        Set up n_candidates and grid


        Modeling attrs:
        X = Features
        y = Columns
        groups = Set observation group e.g entity
        sample_weight = Column containing weight for each row

        X, y, groups, sample_weight _HOLDOUT split 20% of DataFrame sampled by target
        to cross validate properly

        cv: Split Method e.g GroupKFold
        params_grid:
        number_candidates = based on params_grid
        fit_params: fit kwarg dict type + value


        sorted:bool = sorted by date_col

        """
        # @TODO Sort events by date when it's up
        # @TODO Add Sample weight as fit params when it's up
        # @TODO Set Up Y and X with holdout set
        # @TODO Assert prepared columns to be fitter are easily accessible
        # @TODO Set Fit Params for the table itself


    # Using cached property secures heavy loads are done just once.
    @cached_property
    def df_sorted(self):
        if self.date_col:
            return self.df.sort_values(by=
            self.date_col).copy()
    
    @cached_property
    def split_holdout_set(self):
        # @TODO save 20% balanced fractioned part to cross validate later
        return None

    @cached_property
    def n_rows(self):
        n_rows = len(self.df)
        if n_rows > MIN_ROWS:
            raise ValueError(f"Table must have > 1.000 rows!")
        return n_rows
    
    @cached_property
    def columns(self):
        return self.df_sorted.columns

    @cached_property
    def y(self):
        return self.df_sorted[self.y_col].copy()

    @cached_property
    def X(self):
        return self.df_sorted.drop(columns=[self.y_col]).copy()

    @cached_property
    def fit_params(self):
        return None
    
    @cached_property
    def estimator_type(self):
        # Check Cardinality
        return None
