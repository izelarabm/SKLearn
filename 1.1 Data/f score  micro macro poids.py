from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support as score

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]


print(confusion_matrix(y_true, y_pred))



precision, recall, fscore, support = score(y_true, y_pred)

print('precision: {}'.format(precision))
print('recall: {}'.format(recall))
print('fscore: {}'.format(fscore))
print('support: {}'.format(support))












#fs=f1_score(y_true, y_pred, average='micro')
#fsm=f1_score(y_true, y_pred, average='macro')
#fsw=f1_score(y_true, y_pred, average='weighted')
#fsn=f1_score(y_true, y_pred, average=None)
#
#
#print(fs)
#print(fsm)
#print(fsw)
#print(fsn)


