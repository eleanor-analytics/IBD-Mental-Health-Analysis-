"""
IBD Psychosocial Analysis - Visualisations
Author: Eleanor Bryan
Date: 2026
Purpose: Create visualisations for the cleaned IBD dataset

HOW TO USE:
1. Make sure analysis.py has been run at least once
   (so general_info_clean.csv exists).
2. Open this file in IDLE.
3. Press F5 to run it.
4. Check the folder for the new *.png charts.
"""

# ============================
# IMPORTS
# ============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100


# ============================
# STEP 1: LOAD CLEANED DATA
# ============================
print("=== LOADING CLEANED DATA ===")

general_info = pd.read_csv('general_info_clean.csv')
assessment   = pd.read_csv('assessment_clean.csv')

print(f"General Info: {general_info.shape}")
print(f"Assessment:   {assessment.shape}")


# ============================
# STEP 2: DEMOGRAPHICS
# ============================
print("\n=== DEMOGRAPHICS ===")

# Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(general_info['Age'].dropna(), bins=15, kde=True, color='steelblue')
plt.title('Distribution of Age in IBD Patients')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('age_distribution.png', dpi=300)
plt.close()
print("Saved: age_distribution.png")

# Disease type distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=general_info, x='Disease', palette='Set2')
plt.title('Distribution of IBD Disease Type')
plt.xlabel('Disease Type')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.savefig('disease_distribution.png', dpi=300)
plt.close()
print("Saved: disease_distribution.png")


# ============================
# STEP 3: IBDQ BY DISEASE ACTIVITY
# ============================
print("\n=== IBDQ BY DISEASE ACTIVITY ===")

ibdq_cols = [col for col in general_info.columns if 'IBDQ-' in col]
print(f"IBDQ Columns found: {len(ibdq_cols)}")

if ibdq_cols:
    plt.figure(figsize=(14, 10))
    for i, col in enumerate(ibdq_cols[:6]):
        plt.subplot(2, 3, i+1)
        sns.boxplot(x='Clinical_Activity_Code', y=col, data=general_info)
        plt.title(f'{col[:35]}...', fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()
    plt.savefig('ibdq_by_activity.png', dpi=300)
    plt.close()
    print("Saved: ibdq_by_activity.png")


# ============================
# STEP 4: HADS (ANXIETY & DEPRESSION)
# ============================
print("\n=== HADS ===")

# ---- 4a. Individual HADS-A responses ----
hads_a_cols = [col for col in general_info.columns
               if col.startswith('HADS-A') and not col.endswith('_score')]

if hads_a_cols:
    plt.figure(figsize=(16, 8))
    for i, col in enumerate(hads_a_cols[:4]):
        plt.subplot(1, 4, i+1)
        counts = general_info[col].value_counts().head(8)
        sns.barplot(x=counts.index, y=counts.values)
        plt.title(col[:25], fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('hads_anxiety_items.png', dpi=300)
    plt.close()
    print("Saved: hads_anxiety_items.png")

# ---- 4b. Individual HADS-D responses ----
hads_d_cols = [col for col in general_info.columns
               if col.startswith('HADS-D') and not col.endswith('_score')]

if hads_d_cols:
    plt.figure(figsize=(16, 8))
    for i, col in enumerate(hads_d_cols[:4]):
        plt.subplot(1, 4, i+1)
        counts = general_info[col].value_counts().head(8)
        sns.barplot(x=counts.index, y=counts.values)
        plt.title(col[:25], fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('hads_depression_items.png', dpi=300)
    plt.close()
    print("Saved: hads_depression_items.png")

# ---- 4c. HADS totals (anxiety + depression) ----
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(general_info['HADS_Anxiety_Total'].dropna(),
             bins=10, kde=True, color='coral', ax=axes[0])
axes[0].set_title('HADS Anxiety Total')
axes[0].set_xlabel('Score (0-21)')

sns.histplot(general_info['HADS_Depression_Total'].dropna(),
             bins=10, kde=True, color='mediumpurple', ax=axes[1])
axes[1].set_title('HADS Depression Total')
axes[1].set_xlabel('Score (0-21)')

plt.tight_layout()
plt.savefig('hads_totals.png', dpi=300)
plt.close()
print("Saved: hads_totals.png")


# ============================
# STEP 5: PSS (PERCEIVED STRESS)
# ============================
print("\n=== PSS ===")

# ---- 5a. First 8 individual PSS items ----
pss_cols = [col for col in general_info.columns
            if col.startswith('PSS-') and not col.endswith('_score')]

if pss_cols:
    plt.figure(figsize=(16, 12))
    for i, col in enumerate(pss_cols[:8]):
        plt.subplot(2, 4, i+1)
        counts = general_info[col].value_counts().head(8)
        sns.barplot(x=counts.index, y=counts.values)
        plt.title(col[:25], fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('pss_distribution.png', dpi=300)
    plt.close()
    print("Saved: pss_distribution.png")

# ---- 5b. PSS total ----
plt.figure(figsize=(8, 5))
sns.histplot(general_info['PSS_Total'].dropna(),
             bins=10, kde=True, color='seagreen')
plt.title('Perceived Stress (PSS Total)')
plt.xlabel('PSS Score (0-56)')
plt.tight_layout()
plt.savefig('pss_total.png', dpi=300)
plt.close()
print("Saved: pss_total.png")


# ============================
# STEP 6: APGAR (FAMILY SUPPORT)
# ============================
print("\n=== APGAR ===")

apgar_cols = [col for col in general_info.columns
              if col.startswith('APGAR-') and not col.endswith('_score')]

if apgar_cols:
    plt.figure(figsize=(16, 10))
    for i, col in enumerate(apgar_cols):
        plt.subplot(2, 3, i+1)
        counts = general_info[col].value_counts().head(8)
        sns.barplot(x=counts.index, y=counts.values)
        plt.title(col[:25], fontsize=9)
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('apgar_distribution.png', dpi=300)
    plt.close()
    print("Saved: apgar_distribution.png")

# APGAR total
plt.figure(figsize=(8, 5))
sns.histplot(general_info['APGAR_Total'].dropna(),
             bins=10, kde=True, color='goldenrod')
plt.title('Family Support (APGAR Total)')
plt.xlabel('APGAR Score (0-10)')
plt.tight_layout()
plt.savefig('apgar_total.png', dpi=300)
plt.close()
print("Saved: apgar_total.png")


# ============================
# STEP 7: CORRELATION HEATMAP
# ============================
print("\n=== CORRELATION HEATMAP ===")

corr = general_info[[
    'HADS_Anxiety_Total',
    'HADS_Depression_Total',
    'PSS_Total',
    'APGAR_Total'
]].corr()

plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt='.2f')
plt.title('Correlation Between Psychological Measures')
plt.tight_layout()
plt.savefig('correlation_heatmap.png', dpi=300)
plt.close()
print("Saved: correlation_heatmap.png")


# ============================
# STEP 8: LONGITUDINAL CHANGES
# ============================
print("\n=== LONGITUDINAL ASSESSMENTS ===")

plt.figure(figsize=(10, 6))
sns.countplot(data=assessment, x='Assessment', hue='Diseases')
plt.title('Number of Patients Assessed Over Time by Disease Type')
plt.xlabel('Assessment Time Point')
plt.ylabel('Count')
plt.legend(title='Disease Type')
plt.tight_layout()
plt.savefig('longitudinal_assessment.png', dpi=300)
plt.close()
print("Saved: longitudinal_assessment.png")


# ============================
# STEP 9: DONE
# ============================
print("\n=== VISUALISATIONS COMPLETE ===")
print("All PNG files saved in the project folder.")