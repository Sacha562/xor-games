import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('results.csv')
data.columns = data.columns.str.strip()

pd.to_numeric(data['entangled_val'])
pd.to_numeric(data['classical_val'])
pd.to_numeric(data['entangled_val_toqito'])
pd.to_numeric(data['classical_val_toqito'])

# Row numbers for different plots
a = 5
b = 10
c = 14

subset_a = data.iloc[:a]
subset_b = data.iloc[a:b]
subset_c = data.iloc[b:c]
subset_d = data.iloc[c:]

# Plot for m = n = 1
sns.set(style='whitegrid')
ax = sns.barplot(data=subset_a, x='function_id', y='entangled_val', color='blue', label='Entangled Value')
sns.barplot(data=subset_a, x='function_id', y='classical_val', color='orange', label='Classical Value')

# Annotate each bar
for p in ax.patches[:len(subset_a)]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points', fontsize=8)

for p in ax.patches[len(subset_a):]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='top',
                xytext=(0, -10), textcoords='offset points', fontsize=8)

custom_labels = ['$f_1$', '$f_2$', '$f_3$', '$f_4$', '$f_5$']
ax.set_xticklabels(custom_labels)

plt.xlabel('Function')
plt.ylabel('Value')
plt.title('Entangled Value vs Classical Value for $m = n = 1$')
plt.legend(loc='lower right')

plt.show()

# Plot for m = n = 2
sns.set(style='whitegrid')
ax = sns.barplot(data=subset_b, x='function_id', y='entangled_val', color='blue', label='Entangled Value')
sns.barplot(data=subset_b, x='function_id', y='classical_val', color='orange', label='Classical Value')

# Annotate each bar
for p in ax.patches[:len(subset_b)]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points', fontsize=8)

for p in ax.patches[len(subset_b):]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='top',
                xytext=(0, -10), textcoords='offset points', fontsize=8)

custom_labels = ['$f_6$', '$f_7$', '$f_8$', '$f_9$', '$f_{10}$']
ax.set_xticklabels(custom_labels)

plt.xlabel('Function')
plt.ylabel('Value')
plt.title('Entangled Value vs Classical Value for $m = n = 2$')
plt.legend(loc='lower right')

plt.show()


# Plot for m != n
sns.set(style='whitegrid')
ax = sns.barplot(data=subset_c, x='function_id', y='entangled_val', color='blue', label='Entangled Value')
sns.barplot(data=subset_c, x='function_id', y='classical_val', color='orange', label='Classical Value')

# Annotate each bar
for p in ax.patches[:len(subset_c)]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points', fontsize=8)

for p in ax.patches[len(subset_c):]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='top',
                xytext=(0, -10), textcoords='offset points', fontsize=8)

custom_labels = ['$f_{11}$', '$f_{12}$', '$f_{13}$', '$f_{14}$']
ax.set_xticklabels(custom_labels)

plt.xlabel('Function')
plt.ylabel('Value')
plt.title('Entangled Value vs Classical Value for $m \\neq n$')
plt.legend(loc='lower right')

plt.show()

# Plot for non-uniform distribution functions
sns.set(style='whitegrid')
ax = sns.barplot(data=subset_d, x='function_id', y='entangled_val', color='blue', label='Entangled Value')
sns.barplot(data=subset_d, x='function_id', y='classical_val', color='orange', label='Classical Value')

# Annotate each bar
for p in ax.patches[:len(subset_d)]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom',
                xytext=(0, 5), textcoords='offset points', fontsize=8)

for p in ax.patches[len(subset_d):]:
    ax.annotate(f'{p.get_height():.4f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='top',
                xytext=(0, -10), textcoords='offset points', fontsize=8)

custom_labels = ['$f_{1}$ with $q_1$', '$f_{12}$ with $q_2$', '$f_{10}$ with $q_3$']
ax.set_xticklabels(custom_labels)

plt.xlabel('Function')
plt.ylabel('Value')
plt.title('Entangled Value vs Classical Value for non-uniform distribution functions')
plt.legend(loc='lower right')

plt.show()
