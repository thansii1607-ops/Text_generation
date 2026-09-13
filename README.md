# AI Text Generator

## Project Description

AI Text Generator is a simple web application built using Streamlit and Hugging Face Transformers. It allows users to enter a sentence or a few words, and the AI model generates text based on the given input.

The project uses the GPT-Neo 125M model from EleutherAI to generate text. The application provides a simple and user-friendly interface for experimenting with AI-based text generation.

## Features

* Simple Streamlit web interface
* AI-based text generation
* Uses GPT-Neo 125M model
* User can enter custom text
* Generates text based on the given prompt
* Displays the generated text directly on the webpage

## Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* GPT-Neo 125M

## How It Works

1. The user enters a sentence or starting text.
2. The application sends the input to the GPT-Neo model.
3. The model generates additional text based on the input.
4. The generated text is displayed on the Streamlit webpage.

## Installation

Install the required Python libraries using:

```bash
pip install streamlit transformers torch
```

## How to Run

Run the following command in the terminal:

```bash
streamlit run app.py
```

The application will open in the browser at:

```text
http://localhost:8501
```

## Conclusion

This project demonstrates how a pre-trained language model can be integrated with Streamlit to create a simple AI text generation application. It is useful for understanding basic Natural Language Processing and generative AI concepts.
