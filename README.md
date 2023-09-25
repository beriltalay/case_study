Docker image can be build via following command with preferred tag (-t)

```
docker build -t ml_model .
```

Docker container that the trained model wil be served can be run by:

```
docker run -p 80:5000 -t -i ml_model
```

After successful run of the container with request to adress <http://127.0.0.1:80/predict> with following json body

```json
{
    "no_of_dependents":2.00000000e+00,
    "income_annum":9.60000000e+06,
    "loan_amount":2.99000000e+07,
    "loan_term":1.20000000e+01,
    "cibil_score":7.78000000e+02,
    "residential_assets_value":2.40000000e+06,
    "commercial_assets_value":1.76000000e+07,
    "luxury_assets_value":2.27000000e+07,
    "bank_asset_value":8.00000000e+06,
    "education":"Graduated",
    "self_employed":"No"
}
```

you can get the prediction of the model.

Json schema will be checked during prediction procedure so request body should satisfy the schema in __schema.py__ file.
