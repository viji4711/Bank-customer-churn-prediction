import joblib

pre = joblib.load("models/preprocessor.pkl")

print("\nCATEGORICAL CATEGORIES FOUND IN PREPROCESSOR:\n")

for name, transformer, columns in pre.transformers_:
    if hasattr(transformer, "categories_"):
        print(columns, "=>", transformer.categories_)
