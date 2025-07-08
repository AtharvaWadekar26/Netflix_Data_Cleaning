import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# === 1️⃣ Load the dataset ===
file_path = r"C:/Users/ASUS/Downloads/Netflix_data/netflix.csv"  # Update path if needed

try:
    data = pd.read_csv(file_path)
    print("✅ Data loaded successfully!")
except FileNotFoundError:
    print(f"❌ File not found at: {file_path}")
    exit()

print(data.head())
print(f"Shape of data: {data.shape}")

# === 2️⃣ Check data info ===
print(data.info())
print(data.describe())

# === 3️⃣ Data Cleaning ===
data = data.drop_duplicates()
print("Missing values before cleaning:")
print(data.isnull().sum())
data = data.dropna(subset=['director', 'country'])
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['genres'] = data['listed_in'].apply(lambda x: x.split(', ') if isinstance(x, str) else [])

# === 4️⃣ Exploratory Data Analysis ===
sns.countplot(data=data, x='type', hue='type', palette='Set2', legend=False)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

all_genres = sum(data['genres'], [])
genre_counts = pd.Series(all_genres).value_counts().head(10)
sns.barplot(x=genre_counts.values, y=genre_counts.index, hue=genre_counts.index, palette='Set3', legend=False)
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()

sns.countplot(data=data, x='year_added', hue='year_added', palette='coolwarm', legend=False)
plt.title("Content Added per Year")
plt.xlabel("Year Added")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

top_directors = data['director'].value_counts().head(10)
sns.barplot(x=top_directors.values, y=top_directors.index, hue=top_directors.index, palette='Blues_d', legend=False)
plt.title("Top 10 Directors on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.show()

movie_titles = data[data['type'] == 'Movie']['title'].dropna()
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(' '.join(movie_titles))
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Movie Titles")
plt.show()

sns.countplot(data=data, y='rating', order=data['rating'].value_counts().index, hue='rating', palette='magma', legend=False)
plt.title("Content Rating Distribution on Netflix")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.show()

top_countries = data['country'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, hue=top_countries.index, palette='viridis', legend=False)
plt.title("Top 10 Countries with Most Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.show()

print("🎉 Analysis completed without warnings!")
data.to_csv("C:/Users/ASUS/Downloads/Netflix_data/cleaned_netflix_data.csv", index=False)
print("✅ Cleaned data saved successfully!")
from sqlalchemy import create_engine

# Example for SQLite (no setup required)
engine = create_engine('sqlite:///C:/Users/ASUS/Downloads/Netflix_data/netflix.db')

data.to_sql('netflix_data', engine, if_exists='replace', index=False)

print("✅ Data exported to SQL database successfully!")
result = pd.read_sql("SELECT type, COUNT(*) AS count FROM netflix_data GROUP BY type", engine)
print(result)
