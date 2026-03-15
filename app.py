import streamlit as st
import pandas as pd
from openai import OpenAI

st.title("Groww App Review → Weekly Product Pulse")

st.write("This prototype converts recent app reviews into a weekly product pulse.")

client = OpenAI()

df = pd.read_csv("reviews.csv")

st.subheader("Imported Reviews")
st.dataframe(df)

reviews_text = "\n".join(df["text"].tolist())

if st.button("Generate Weekly Pulse"):

    prompt = f"""
You are a product analyst summarizing mobile app reviews.

Create a weekly product pulse using these rules:

- Max 250 words
- Identify top 3 themes
- Include 3 representative user quotes
- Suggest 3 product action ideas
- Do NOT include personal information

Reviews:
{reviews_text}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    weekly_note = response.choices[0].message.content

    st.subheader("Weekly Pulse")
    st.write(weekly_note)

    email_prompt = f"""
Convert the following weekly product pulse into a short internal email summary.

{weekly_note}
"""

    email_response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": email_prompt}]
    )

    email_text = email_response.choices[0].message.content

    st.subheader("Email Draft")
    st.write(email_text)
