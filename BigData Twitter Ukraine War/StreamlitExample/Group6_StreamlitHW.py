from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

df = pd.read_csv("/home/valentin_werner/de_en.csv").drop(columns = ["Unnamed: 0"])
st.set_page_config(layout="wide")
st.title("Wordcloud Ukraine Hashtags in English or German")
st.info("Sorry, the Wordcloud may take up to 60 seconds to load")

choice = st.sidebar.selectbox(label = "Language for Wordcloud", options = ("en", "de"))


wc = WordCloud(width = 1800, height = 400, background_color="white").generate(" ".join(target for target in df[df.language == choice].text))

fig = plt.figure()
plt.imshow(wc)
plt.axis("off")
st.pyplot(fig)

txt = st.sidebar.text_area(label = "Filter the dataframe by specific word(group)s from the Wordcloud", value = "")
st.text("Here are some example data rows for your input")
st.dataframe(df[df['text'].str.contains(txt)].head(25), width = 1800, height = 1300)