# Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_true, y_pred)
# Accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_true, y_pred)
# Recall
from sklearn.metrics import recall_score
recall_score(y_true, y_pred, average=None)
# Precision
from sklearn.metrics import precision_score
precision_score(y_true, y_pred, average=None)
Hay tres formas de calcular la puntuación F1 en Python:

# Method 1: sklearn
from sklearn.metrics import f1_score
f1_score(y_true, y_pred, average=None)
# Method 2: Manual Calculation
F1 = 2 * (precision * recall) / (precision + recall)
# Method 3: Classification report [BONUS]
from sklearn.metrics import classification_report
print(classification_report(y_true, y_pred, target_names=target_names))