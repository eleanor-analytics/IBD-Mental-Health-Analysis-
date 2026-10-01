"""
IBD Psychosocial Analysis
Author: Eleanor Bryan
Date: 2026
Purpose: Analyse longitudinal psychological outcomes in IBD patients
"""

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. LOAD DATA
# ----------------------------

# Load each CSV file
general_info = pd.read_csv('general_info.csv')
assessment = pd.read_csv('assessment.csv')
mapping = pd.read_csv('mapping.csv')
workshop = pd.read_csv('workshop.csv')

# Display basic information
print("=== GENERAL INFORMATION ===")
print(f"Shape: {general_info.shape}")
print("\nFirst 5 rows:")
print(general_info.head())

print("\nColumn names:")
print(general_info.columns.tolist())

print("\nMissing values:")
print(general_info.isnull().sum())

print("\n=== ASSESSMENT DATA ===")
print(f"Shape: {assessment.shape}")
print("\nFirst 5 rows:")
print(assessment.head())


# ----------------------------
# 2. CLEAN COLUMN NAMES
# ----------------------------

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(r'\s+', ' ', regex=True)
    )
    return df

general_info = clean_column_names(general_info)
assessment = clean_column_names(assessment)
workshop = clean_column_names(workshop)

general_info = general_info.rename(columns={
    'Clinical Activity ': 'Clinical_Activity',
    'Clinical Activity Code': 'Clinical_Activity_Code',
    'Number of flare-ups (last 12 months)': 'Flare_Ups_12m',
    'Number of hospitalizations (last 12 months)': 'Hospitalizations_12m',
    'Smoking Status': 'Smoking_Status',
    'Marital Status': 'Marital_Status',
    'Years since diagnosis': 'Years_Since_Diagnosis',
})

print("\n=== COLUMN NAMES CLEANED ===")


# ----------------------------
# 3. RECODE SEX & FIX ERRORS
# ----------------------------

# Sex: 1 = Female, 0 = Male
general_info['Sex'] = general_info['Sex'].map({1: 'Female', 0: 'Male'})

# Fix Spanish entry
general_info['HADS-D2: I can laugh and see the funny side of things'] = (
    general_info['HADS-D2: I can laugh and see the funny side of things']
    .replace('Actuamente, en absoluto', 'Not at all')
)

print("Sex recoded. Spanish entry fixed.")


# ----------------------------
# 4. SIMPLIFY MULTI-ANSWER RESPONSES
# ----------------------------

pss_cols = [col for col in general_info.columns if col.startswith('PSS-')]
for col in pss_cols:
    general_info[col] = general_info[col].astype(str).str.split(',').str[0].str.strip()

print("Multi-answer responses simplified.")


# ----------------------------
# 5. SCORE HADS
# ----------------------------

hads_scoring = {
    'HADS-A1: I feel tense or "wound up"': {
        'Not at all': 0, 'Occasionally': 1, 'Most of the time': 2, 'Nearly all the time': 3},
    'HADS-A2: I get a sort of frightened feeling, as if something awful is about to happen': {
        'Not at all': 0, 'A little, but it does not worry me': 1,
        'Yes, but not too badly': 2, 'Very definitely and quite badly': 3},
    'HADS-A3: Worrying thoughts go through my mind': {
        'Only occasionally': 0, 'From time to time, but not too often': 1,
        'A lot of the time': 2, 'A great deal of the time': 3},
    'HADS-A4: I can sit at ease and feel relaxed': {
        'Definitely': 0, 'Usually': 1, 'Not often': 2, 'Not at all': 3},
    'HADS-A5: I get a sort of frightened feeling, like "butterflies" in the stomach': {
        'Not at all': 0, 'Occasionally': 1, 'Quite often': 2, 'Very often': 3},
    'HADS-A6: I feel restless, as if I have to be on the move': {
        'Not at all': 0, 'Not very much': 1, 'Quite a lot': 2, 'Very much indeed': 3},
    'HADS-A7: I get sudden feelings of panic': {
        'Not at all': 0, 'Not very often': 1, 'Quite often': 2, 'Very often indeed': 3},
    'HADS-D1: I still enjoy the things I used to enjoy': {
        'Definitely as much': 0, 'Not quite so much': 1, 'Only a little': 2, 'Hardly at all': 3},
    'HADS-D2: I can laugh and see the funny side of things': {
        'As much as I always could': 0, 'Not quite so much now': 1,
        'Definitely not so much now': 2, 'Not at all': 3},
    'HADS-D3: I feel cheerful': {
        'Most of the time': 0, 'Sometimes': 1, 'Not often': 2, 'Not at all': 3},
    'HADS-D4: I feel as if I am slowed down': {
        'Not at all': 0, 'Sometimes': 1, 'Very often': 2, 'Nearly all the time': 3},
    'HADS-D5: I have lost interest in my appearance': {
        'I take just as much care as I always have': 0,
        'I may not be taking quite as much care as I should': 1,
        'I definitely do not take as much care as I should': 2,
        'I do not take any care at all': 3},
    'HADS-D6: I look forward to things with enjoyment': {
        'As much as I ever did': 0, 'Rather less than I used to': 1,
        'Definitely less than I used to': 2, 'Hardly at all': 3},
    'HADS-D7: I can enjoy a good book or radio or TV programme': {
        'Often': 0, 'Sometimes': 1, 'Not often': 2, 'Very seldom': 3},
}

for col, score_map in hads_scoring.items():
    if col in general_info.columns:
        general_info[col + '_score'] = general_info[col].map(score_map)

a_items = [c + '_score' for c in hads_scoring if c.startswith('HADS-A')]
d_items = [c + '_score' for c in hads_scoring if c.startswith('HADS-D')]

general_info['HADS_Anxiety_Total'] = general_info[a_items].sum(axis=1)
general_info['HADS_Depression_Total'] = general_info[d_items].sum(axis=1)

print("HADS scored.")


# ----------------------------
# 6. SCORE PSS
# ----------------------------

pss_map = {'Never': 0, 'Almost never': 1, 'Sometimes': 2, 'Often': 3, 'Very often': 4}

pss_items = [col for col in general_info.columns
             if col.startswith('PSS-') and not col.endswith('_score')]

for col in pss_items:
    general_info[col + '_score'] = general_info[col].map(pss_map)

# Reverse-score positive items
reverse = ['PSS-4', 'PSS-5', 'PSS-6', 'PSS-7', 'PSS-9', 'PSS-10', 'PSS-13']
for col in pss_items:
    if any(col.startswith(r) for r in reverse):
        general_info[col + '_score'] = 4 - general_info[col + '_score']

general_info['PSS_Total'] = general_info[[c + '_score' for c in pss_items]].sum(axis=1)

print("PSS scored.")


# ----------------------------
# 7. SCORE APGAR
# ----------------------------

apgar_map = {'Always': 2, 'Almost always': 2, 'Sometimes': 1,
             'Almost never': 0, 'Never': 0}

apgar_items = [col for col in general_info.columns
               if col.startswith('APGAR-') and not col.endswith('_score')]

for col in apgar_items:
    general_info[col + '_score'] = general_info[col].map(apgar_map)

general_info['APGAR_Total'] = general_info[[c + '_score' for c in apgar_items]].sum(axis=1)

print("APGAR scored.")


# ----------------------------
# 8. SAVE CLEANED DATA
# ----------------------------

general_info.to_csv('general_info_clean.csv', index=False)
assessment.to_csv('assessment_clean.csv', index=False)
workshop.to_csv('workshop_clean.csv', index=False)

print("\n=== CLEANED DATA SAVED ===")
print("  general_info_clean.csv")
print("  assessment_clean.csv")
print("  workshop_clean.csv")


# ----------------------------
# 9. SUMMARY STATISTICS
# ----------------------------

print("\n=== SUMMARY STATISTICS (Psychological Totals) ===")
print(general_info[['HADS_Anxiety_Total', 'HADS_Depression_Total',
                    'PSS_Total', 'APGAR_Total']].describe())
