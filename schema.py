RequestSchema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "no_of_dependents": {
            "type": "number"
        },
        "income_annum": {
            "type": "number"
        },
        "loan_amount": {
            "type": "number"
        },
        "loan_term": {
            "type": "number"
        },
        "cibil_score": {
            "type": "number"
        },
        "residential_assets_value": {
            "type": "number"
        },
        "commercial_assets_value": {
            "type": "number"
        },
        "luxury_assets_value": {
            "type": "number"
        },
        "bank_asset_value": {
            "type": "number"
        },
        "education": {
            "type": "string"
        },
        "self_employed": {
            "type": "string"
        }
    },
    "required": [
        "no_of_dependents",
        "income_annum",
        "loan_amount",
        "loan_term",
        "cibil_score",
        "residential_assets_value",
        "commercial_assets_value",
        "luxury_assets_value",
        "bank_asset_value",
        "education",
        "self_employed"
    ]
}