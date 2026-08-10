import io
from fastapi import APIRouter,  UploadFile, File, HTTPException
import pandas as pd


from app.analysis.eda import run_eda
from app.analysis.validation import validate_dataframe
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

    # now I will add some validation while we are getting data with zero rows or columns
    errors = validate_dataframe(df)

    if errors:
        raise HTTPException(
            status_code=400,
            detail=errors
        )



    # removed the one by one different analysis
    # to manage the eda whole part into one file rather make this file heavy
    # we have created one separate eda.py file in the analysis folder to handle the whole analysis part in one file 
    # and then we added this run_eda() function to get all the analysis from the eda file and show it to the user using json file
    eda_result = run_eda(df) # everything working fine



    return {
        "filename":file.filename,
        "analysis":eda_result,
    }