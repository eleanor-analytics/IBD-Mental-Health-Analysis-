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