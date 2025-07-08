import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load cleaned data
data = pd.read_csv("C:/Users/ASUS/Downloads/Netflix_data/cleaned_netflix_data.csv")

st.title("📺 Netflix Data Dashboard")
st.write("Explore Netflix's catalog by content type, genre, rating, and country.")

# Movies vs TV Shows
st.subheader("Movies vs TV Shows")
fig1, ax1 = plt.subplots()
sns.countplot(data=data, x='type', palette='Set2', ax=ax1)
st.pyplot(fig1)

# Top 10 Genres
st.subheader("Top 10 Genres")
all_genres = data['genres'].dropna().apply(lambda x: x.split(', '))
all_genres = sum(all_genres, [])
genre_counts = pd.Series(all_genres).value_counts().head(10)
fig2, ax2 = plt.subplots()
sns.barplot(x=genre_counts.values, y=genre_counts.index, palette='Set3', ax=ax2)
ax2.set_xlabel("Count")
ax2.set_ylabel("Genre")
st.pyplot(fig2)

# Content Added per Year
st.subheader("Content Added per Year")
fig3, ax3 = plt.subplots()
sns.countplot(data=data, x='year_added', palette='coolwarm', ax=ax3)
plt.xticks(rotation=45)
st.pyplot(fig3)

# Top 10 Countries
st.subheader("Top 10 Countries with Most Content")
top_countries = data['country'].value_counts().head(10)
st.bar_chart(top_countries)

# Ratings distribution
st.subheader("Ratings Distribution")
fig4, ax4 = plt.subplots()
sns.countplot(data=data, y='rating', order=data['rating'].value_counts().index, palette='magma', ax=ax4)
st.pyplot(fig4)

st.success("🎉 Dashboard loaded successfully!")
