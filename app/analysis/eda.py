import pandas as pd


from app.analysis.profiler import profile_dataset
from app.analysis.statistics import numerical_statistics
from app.analysis.outliers import detect_outliers
from app.analysis.correlations import correlation_analysis
from app.analysis.categorical import categorical_analysis


def run_eda(df: pd.DataFrame)->dict:
   profile =  profile_dataset(df)
   statistics = numerical_statistics(df)
   outliers = detect_outliers(df)
   correlations = correlation_analysis(df)
   categoricals = categorical_analysis(df)


   return {
      "profile": profile,
      "statistics": statistics,
      "outliers": outliers,
      "correlations": correlations,
      "categoricals": categoricals
   }
