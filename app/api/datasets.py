import io
from fastapi import APIRouter,  UploadFile, File, HTTPException
import pandas as pd

from app.analysis.profiler import profile_dataset
from app.analysis.statistics import numerical_statistics
from app.analysis.outliers import detect_outliers
from app.analysis.correlations import correlation_analysis

router = APIRouter(
    prefix = "/datasets",
    tags = ["Datasets"]
)

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file provided"
        )
    contents = await file.read() # if there is any file uploaded then save it into contents

    if file.filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(contents))
    elif file.filename.endswith((".xlsx", ".xls")):
        df = pd.read_excel(io.BytesIO(contents))
    else:

        raise HTTPException(
            status_code=400,
            detail="Only CSV and Excel files are supported"
        )

    profile = profile_dataset(df)  # connect to the profiler to get the all analytics
    statistics = numerical_statistics(df) # for numerical analysis
    outliers = detect_outliers(df) # detects outliers using iqr
    correlations = correlation_analysis(df) # extract the correlation analysis btw the numerical values within data

    return {
        "filename":file.filename,
        "profile": profile,
        "statistics":statistics,
        "outliers": outliers,
        "correlations":correlations
    }