import numpy as np

numberclass = 3

cm = np.array(
    [[23556, 4102, 1843],
     [5101, 22107, 2293],
     [3450, 4052, 21999]]
)


def metrics(TP, FP, FN, TN):
    precision = []
    sensitivity = []
    specificity = []
    F1 = []
    Accuracy = []
    for i in range(3):
        precision.append(TP[i] / (TP[i] + FP[i]))
        sensitivity.append(TP[i] / (TP[i] + FN[i]))
        specificity.append(TN[i] / (FP[i] + TN[i]))
        F1.append((2 * TP[i]) / (2 * TP[i] + FP[i] + FN[i]))
        Accuracy.append((TP[i] + TN[i]) / (TP[i] + TN[i] + FP[i] + FN[i]))
    return precision, sensitivity, specificity, F1, Accuracy
#
#
# print("label precision recall")
# for label in range(3):
#     print(f"{label:5d} {precision(label, cm):9.3f} {recall(label, cm):6.3f}")

TruePositive = np.diag(cm)
print(TruePositive)

FalsePositive = []
for i in range(numberclass):
    FalsePositive.append(sum(cm[:, i]) - cm[i, i])
print(FalsePositive)

FalseNegative = []
for i in range(numberclass):
    FalseNegative.append(sum(cm[i, :]) - cm[i, i])
print(FalseNegative)

TrueNegative = []
for i in range(numberclass):
    temp = np.delete(cm, i, 0)   # delete ith row
    temp = np.delete(temp, i, 1)  # delete ith column
    TrueNegative.append(sum(sum(temp)))
print(TrueNegative)

precision, sensitivity, specificity, F1, Accuracy = metrics(TruePositive, FalsePositive, FalseNegative, TrueNegative)
print("precision:", precision)
print("specificity:", specificity)
print("sensitivity:", sensitivity)
print("F1:", F1)
print("Accuracy:", Accuracy)
print("average_precision:", (precision[0] + precision[1] + precision[2])/3)
print("average_specificity:", (specificity[0] + specificity[1] + specificity[2])/3)
print("average_sensitivity:", (sensitivity[0] + sensitivity[1] + sensitivity[2])/3)
print("average_F1:", (F1[0] + F1[1] + F1[2])/3)
print("average_Accuracy:", (Accuracy[0] + Accuracy[1] + Accuracy[2])/3)

print("average_accuracy:", cm.trace() / cm.sum())

