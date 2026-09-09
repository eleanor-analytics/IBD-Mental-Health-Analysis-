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

# Load the Excel file
file_path = 'Rivera-Sequeiros_et_al_2025_IBD_PsychosocialDataset.xlsx'

# Load each sheet
general_info = pd.read_excel(file_path, sheet_name='General Information')
assessment = pd.read_excel(file_path, sheet_name='Assessment V1-V5')
mapping = pd.read_excel(file_path, sheet_name='Question-Variable Mapping')

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