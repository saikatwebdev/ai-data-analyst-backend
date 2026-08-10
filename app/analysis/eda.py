import pandas as pd


from app.analysis.profiler import profile_dataset
from app.analysis.statistics import numerical_statistics
from app.analysis.outliers import detect_outliers
from app.analysis.correlations import correlation_analysis
from app.analysis.categorical import categorical_analysis
from app.analysis.numerical import numerical_summary

def run_eda(df: pd.DataFrame)->dict:
   summary = dataset_summary(df)
   profile =  profile_dataset(df)
   statistics = numerical_statistics(df)
   outliers = detect_outliers(df)
   correlations = correlation_analysis(df)
   categoricals = categorical_analysis(df)
   numerical = numerical_summary(df)

   return {
      "summary":summary,
      "profile": profile,
      "statistics": statistics,
      "numerical_summary":numerical,
      "outliers": outliers,
      "correlations": correlations,
      "categoricals": categoricals
   }


def dataset_summary(df:pd.DataFrame)->dict:
   return{
      "rows":len(df),
      "columns":len(df.columns),
      "memory_usage_mb": round(
         df.memory_usage(deep=True).sum() / (1024 ** 2),
         2
      ),
   }