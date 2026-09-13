import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Text Generator")

st.title("AI Text Generator")
st.write("Enter a sentence and AI will complete it.")

# Load the AI model
@st.cache_resource
def get_model():
    model = pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-125M"
    )
    return model

generator = get_model()

# Get input from user
text = st.text_area(
    "Enter your text:",
    placeholder="Artificial Intelligence is..."
)

if st.button("Generate Text"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:
        with st.spinner("Generating text..."):

            output = generator(
                text,
                max_new_tokens=50,
                do_sample=True,
                temperature=0.7
            )

        result = output[0]["generated_text"]

        st.subheader("Generated Text")
        st.write(result)

