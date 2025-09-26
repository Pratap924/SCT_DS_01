import seaborn as sns
import matplotlib.pyplot as plt

# Load iris dataset
iris = sns.load_dataset("iris")

# Histogram for sepal length
plt.figure(figsize=(8,5))
sns.histplot(iris["sepal_length"], bins=20, kde=True, color="lightgreen")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Count")
plt.show()

# Bar chart for species count
plt.figure(figsize=(6,4))
sns.countplot(x="species", data=iris, palette="pastel")
plt.title("Distribution of Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()
