from flask import Flask, request, render_template
# import numpy as np
# import pandas as pd
from sklearn.preprocessing import StandardScaler

from src.logger import logging
from src.pipeline.predict_pipeline import CustomData, PredictPipeline 


app= Flask(__name__)

# Route for homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for predict endpoint
@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("race_ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("reading_score")),
            writing_score=float(request.form.get("writing_score"))
        )
        data_df = data.get_data_as_dataframe()
        logging.info(f"Input data df: {data_df}")

        predict_pipeline = PredictPipeline()
        result = predict_pipeline.predict(data_df)
        return render_template("home.html", result=result[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
