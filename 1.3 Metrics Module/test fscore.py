

from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
#from sklearn.metrics import f1_scorey_true = ["cat", "ant", "cat", "cat", "ant", "bird"]

y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]
print(confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"]))

fs=f1_score(y_true, y_pred, average='micro')
fsm=f1_score(y_true, y_pred, average='macro')

print(fs)
print(fsm)