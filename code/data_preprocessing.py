import pandas as pd
import numpy as np

df = pd.read_csv('D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\data\\raw\\heart_failure_data.csv')

# Handle
missing_rows = df.isna().sum()
print('\n Data missing:')
print(missing_rows)

print(df.dtypes)

numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

df['Sex'] = df['Sex'].map({'M': 1, 'F': 0})

df = pd.get_dummies(df, columns=['ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope'], dtype=int)
print(df.isna().sum())
df = df.reset_index(drop=True)
print(df.columns)
#df.to_csv('D:\\Programer\\HMTK\\HeartFailureDiagnosis-LogisticRegression\\data\\processed\\processed_data.csv', index=False)
