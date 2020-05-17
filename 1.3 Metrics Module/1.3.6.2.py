
from sklearn import metrics
from sklearn.metrics import f1_score
y_pred = [0, 2, 1, 0, 0, 1]
y_true = [0, 1, 2, 0, 1, 2]

print('*************************************************')
print('*************************************************')
fs=f1_score(y_true, y_pred, average='micro')
fsm=f1_score(y_true, y_pred, average='macro')
fsw=f1_score(y_true, y_pred, average='weighted')
fsn=f1_score(y_true, y_pred, average=None)

print('La Matrice de confusion')
print(metrics.confusion_matrix(y_true, y_pred))


print('*************************************************')
print('*************************************************')

# Print the precision and recall, among other metrics
print(metrics.classification_report(y_true, y_pred, digits=3))





print(fs)
print(fsm)
print(fsw)
print(fsn)