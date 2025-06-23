import gradio as gr
from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

# Define function for summarization
def summarize_text(text):
    input_text = "summarize: " + text
    summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Create Gradio Interface
interface = gr.Interface(
    fn=summarize_text,
    inputs="text",
    outputs="text",
    title="Text Summarization App (T5)",
    description="A Data Science & Analytics Project by Harish M and Teammate"
)

interface.launch()
