"""
Master Pipeline Module

Executes the complete mutual fund analytics workflow including ingestion, cleaning, analysis, and reporting.
"""


from scripts.data_ingestion import *
from scripts.data_cleaning import *
from scripts.database_setup import *
from scripts.data_analysis import *
from scripts.data_visualization import *

print("Mutual Fund Analytics Pipeline Executed Successfully")