"""
Precision and recall scores for our prompt:
Precision: 0.899
Recall: 0.943
"""
import pandas as pd 
import numpy as np

#function for percision and recall
def precision_recall(model_classification, ground_truth_classification):
    """takes in two dataframes, zips it and each boolean from the zip corresponds to g and s respectively 
    g and s is true if both g,s = true, true
    not g and s is true if g,s = false, true 
    g and not s is true if g,s = true, false"""
    TP = sum((g and s) for g,s in zip(ground_truth_classification, model_classification))
    FP = sum((not g and s) for g, s in zip(ground_truth_classification, model_classification))
    FN = sum((g and not s) for g,s in zip(ground_truth_classification, model_classification))
    precision = ((TP) / (FP + TP)) if (FN + FP) > 0 else 0
    recall = ((TP) / (FN + TP)) if (FN + TP ) > 0 else 0 
    standard_deviation = model_classification.std()
    print("standard deviation is", standard_deviation)
    return precision, recall  