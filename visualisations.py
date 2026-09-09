"""
IBD Psychosocial Analysis - Visualisations
Author: Eleanor Bryan
Date: 2026
Purpose: Create visualisations for IBD dataset
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

print("=== DATA LOADED SUCCESSFULLY ===")
print(f"General Info: {general_info.shape}")
print(f"Assessment: {assessment.shape}")

# ----------------------------
# 2. DEMOGRAPHICS
# ----------------------------

# Age distribution
plt.figure(figsize=(10, 6))
sns.histplot(general_info['Age'].dropna(), bins=15, kde=True, color='blue')
plt.title('Distribution of Age in IBD Patients')
plt.xlabel('Age')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('age_distribution.png', dpi=300)
plt.show()

# Disease type distribution
disease_counts = general_info['Disease'].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=disease_counts.index, y=disease_counts.values, palette='Set2')
plt.title('Distribution of IBD Disease Type')
plt.xlabel('Disease Type')
plt.ylabel('Number of Patients')
plt.tight_layout()
plt.savefig('disease_distribution.png', dpi=300)
plt.show()

# ----------------------------
# 3. IBDQ (QUALITY OF LIFE)
# ----------------------------

# Select IBDQ columns
ibdq_cols = [col for col in general_info.columns if 'IBDQ-' in col]
print(f"\nIBDQ Columns found: {len(ibdq_cols)}")
print(ibdq_cols)

# Create a box plot for IBDQ questions by disease activity
if ibdq_cols:
    # Get unique Clinical Activity values (excluding NaN)
    activity_values = general_info['Clinical Activity '].dropna().unique()
    print(f"Clinical Activity values: {activity_values}")
    
    plt.figure(figsize=(14, 10))
    # Plot first 6 IBDQ questions
    for i, col in enumerate(ibdq_cols[:6]):
        plt.subplot(2, 3, i+1)
        # Use Clinical Activity Code for more consistent grouping
        sns.boxplot(x='Clinical Activity Code', y=col, data=general_info)
        plt.title(f'{col[:30]}...')
        plt.xticks(rotation=45, fontsize=8)
    plt.tight_layout()
    plt.savefig('ibdq_by_activity.png', dpi=300)
    plt.show()

# ----------------------------
# 4. HADS (ANXIETY & DEPRESSION)
# ----------------------------

# Select HADS columns
hads_a_cols = [col for col in general_info.columns if col.startswith('HADS-A')]
hads_d_cols = [col for col in general_info.columns if col.startswith('HADS-D')]

print(f"HADS-A Columns: {len(hads_a_cols)}")
print(f"HADS-D Columns: {len(hads_d_cols)}")

# Plot HADS-A (Anxiety) responses
if hads_a_cols:
    plt.figure(figsize=(16, 8))
    for i, col in enumerate(hads_a_cols[:4]):
        plt.subplot(1, 4, i+1)
        # Count the responses
        response_counts = general_info[col].value_counts().head(8)
        sns.barplot(x=response_counts.index, y=response_counts.values)
        plt.title(f'{col[:25]}')
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('hads_anxiety.png', dpi=300)
    plt.show()

# Plot HADS-D (Depression) responses
if hads_d_cols:
    plt.figure(figsize=(16, 8))
    for i, col in enumerate(hads_d_cols[:4]):
        plt.subplot(1, 4, i+1)
        response_counts = general_info[col].value_counts().head(8)
        sns.barplot(x=response_counts.index, y=response_counts.values)
        plt.title(f'{col[:25]}')
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('hads_depression.png', dpi=300)
    plt.show()

# ----------------------------
# 5. PSS (PERCEIVED STRESS)
# ----------------------------

# Select PSS columns
pss_cols = [col for col in general_info.columns if col.startswith('PSS-')]
print(f"PSS Columns: {len(pss_cols)}")

if pss_cols:
    plt.figure(figsize=(16, 12))
    for i, col in enumerate(pss_cols[:8]):
        plt.subplot(2, 4, i+1)
        response_counts = general_info[col].value_counts().head(8)
        sns.barplot(x=response_counts.index, y=response_counts.values)
        plt.title(f'{col[:25]}')
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('pss_distribution.png', dpi=300)
    plt.show()

# ----------------------------
# 6. APGAR (FAMILY SUPPORT)
# ----------------------------

# Select APGAR columns
apgar_cols = [col for col in general_info.columns if col.startswith('APGAR-')]
print(f"APGAR Columns: {len(apgar_cols)}")

if apgar_cols:
    plt.figure(figsize=(16, 10))
    for i, col in enumerate(apgar_cols):
        plt.subplot(2, 3, i+1)
        response_counts = general_info[col].value_counts().head(8)
        sns.barplot(x=response_counts.index, y=response_counts.values)
        plt.title(f'{col[:25]}')
        plt.xticks(rotation=45, fontsize=8)
        plt.xlabel('')
    plt.tight_layout()
    plt.savefig('apgar_distribution.png', dpi=300)
    plt.show()

# ----------------------------
# 7. LONGITUDINAL CHANGES (OVER TIME)
# ----------------------------

# Look at assessments over time
plt.figure(figsize=(10, 6))
sns.countplot(data=assessment, x='Assessment', hue='Diseases')
plt.title('Number of Patients Assessed Over Time by Disease Type')
plt.xlabel('Assessment Time Point')
plt.ylabel('Count')
plt.legend(title='Disease Type')
plt.tight_layout()
plt.savefig('longitudinal_assessment.png', dpi=300)
plt.show()

print("\n=== ANALYSIS COMPLETE ===")
print("Visualisations saved as PNG files in your project folder.")
print("Files created:")
print("  - age_distribution.png")
print("  - disease_distribution.png")
print("  - ibdq_by_activity.png")
print("  - hads_anxiety.png")
print("  - hads_depression.png")
print("  - pss_distribution.png")
print("  - apgar_distribution.png")
print("  - longitudinal_assessment.png")