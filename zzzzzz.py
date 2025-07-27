import pandas as pd    

# n = 500
# path = "/home/wp3/Domain-Kn/VVSDet/sourcescripts/storage/external/MegaVul_Java_Domain1.csv"

# df = pd.read_csv(path)
# vdf = df[df['vul'] == 1].sample(n)
# ndf = df[df['vul'] == 0].sample(n)

# df = pd.concat([vdf,ndf], ignore_index=True)

# df.to_csv("/home/wp3/Domain-Kn/VVSDet/sourcescripts/storage/external/MegaVul_Java_Domain.csv", index = False)


# from dgl import  load_graphs



# ph = "/home/wp3/Domain-Kn/VVSDet/sourcescripts/storage/cache/Dataset_Vvuldet_codebert_pdg+raw/45411"

# g = load_graphs(ph)[0][0]

# print(g)

from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score
import numpy as np          

pdd = "/home/wp3/Domain-Kn/VVSDet/sourcescripts/storage/outputs/function_level_predictions.csv"

df = pd.read_csv(pdd)
print(df.head(3))

node_pred = [item for sublist in df['node_pred'] for item in eval(sublist)]
node_label = [item for sublist in df['node_label'] for item in eval(sublist)]

# Optionally, print the results
# print("Node Predictions:", node_pred)
# print("Node Labels:", node_label)


node_pred = np.array(node_pred)
node_label = np.array(node_label)

# print(len(node_label) == len(node_pred))

# Compute metrics
precision = precision_score(node_label, node_pred, average='macro')
recall = recall_score(node_label, node_pred, average='macro')
f1 = f1_score(node_label, node_pred, average='macro')
pr_auc = average_precision_score(node_label, node_pred)

# Print the results
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"PR AUC: {pr_auc:.4f}")

