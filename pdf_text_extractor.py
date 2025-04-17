import os
import fitz  # PyMuPDF
import gradio as gr
import requests
from PIL import Image
import pytesseract

# DeepSeek API endpoint and headers
DEESEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.environ.get('DEEPSEEK_API_KEY')}",
    "Content-Type": "application/json"
}

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(pdf_file) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text if text.strip() else "No text found in the PDF."

def exetract_text_with_ocr(pdf_file):
    text = ""
    with fitz.open(pdf_file) as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=300)
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text += pytesseract.image_to_string(image) + "\n"
    return text if text.strip() else "No text found in scanned PDF."

def summarize_text(text):
    prompt = f"Summarize the following document text:\n\n{text}"
    payload = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 512
    }
    try:
        response = requests.post(DEESEEK_API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error summarizing: {e}"

def process_pdf(pdf_file, use_ocr):
    if use_ocr:
        extracted_text = exetract_text_with_ocr(pdf_file)
    else:
        extracted_text = extract_text_from_pdf(pdf_file)
    summary = summarize_text(extracted_text)
    return extracted_text, summary

interface = gr.Interface(
    fn=process_pdf,
    inputs=[
        gr.File(label="Upload PDF File"),
        gr.Checkbox(label="Use OCR for scanned PDFs", value=False)
    ],
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="AI Summary")
    ],
    title="📄 AI-Powered PDF Extractor with DeepSeek",
    description="Upload a scanned or digital PDF. This app extracts text and summarizes it using DeepSeek AI."
)
