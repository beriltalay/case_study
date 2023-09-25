import joblib
import jsonschema
import pandas as pd
from flask import Flask, jsonify, request

from schema import RequestSchema

app = Flask(__name__)

model = joblib.load('RandomForestClassifier.pkl')
feature_cols = ['no_of_dependents','income_annum','loan_amount','loan_term','cibil_score','residential_assets_value','commercial_assets_value','luxury_assets_value','bank_asset_value','education_trans','self_employed_trans','loan_income_ratio','total_assets']

@app.route('/predict', methods=['POST']) 
def predict():
    try:
        query = request.json
        jsonschema.validate(query,RequestSchema)

        df_query = pd.DataFrame(query,index=[0])

        df_query['loan_income_ratio']= df_query['loan_amount']/df_query['income_annum']
        df_query['total_assets'] = df_query[['residential_assets_value','commercial_assets_value','luxury_assets_value','bank_asset_value']].T.sum()
        df_query['education_trans'] = 0 if df_query['education'].values[0]=='Graduated' else 1
        df_query['self_employed_trans'] = 0 if df_query['self_employed'].values[0]=='No' else 1

        prediction = 'Accepted' if model.predict(df_query[feature_cols])==0 else 'Rejected'

        return jsonify(
            {
                "prediction": prediction
            }
        )
    except jsonschema.exceptions.ValidationError as ve:
        return jsonify(
            {
                "responseCode":400,
                "responseMessage":f"{ve.message} at {list(ve.path)}.",
            }
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
