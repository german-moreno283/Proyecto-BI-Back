from joblib import load
import pandas as pd


def predict_data():
  #open("./fitted_pipeline.joblib")
  pipe_loaded = load("./fitted_pipeline.joblib")
"""  ods_df_unlabeled = pd.read_csv("../data/SinEtiquetatest_cat_6716.csv")
  #Predict the labels of the unlabeled data
  y_unlabeled_predict = pipe_loaded.best_estimator_.predict(ods_df_unlabeled["Textos_espanol"])
  #Add the predicted labels to the unlabeled data
  ods_df_unlabeled["sdg"] = y_unlabeled_predict
  #Save the labeled data
  ods_df_unlabeled.to_csv("../data/Predicted.csv", index=False)
"""