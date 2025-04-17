---
title: AI PDF Extractor with DeepSeek
emoji: 📄
colorFrom: indigo
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
---

# 📄 AI-Powered PDF Extractor with DeepSeek AI

This app extracts and summarizes content from both text-based and scanned PDFs using DeepSeek AI.

## 🚀 Features
- 🔍 Text Extraction from native PDFs using PyMuPDF
- 🧠 OCR Extraction from scanned PDFs using Tesseract
- ✨ Summarization using DeepSeek's LLM

## 📎 Usage
1. Upload a .pdf file
2. Enable OCR if it's a scanned PDF
3. Get extracted text + summarized content via DeepSeek

## 📜 API Key Setup
Add your API key on Render under environment variables:
```
DEEPSEEK_API_KEY = your_key_here
```

## 📝 License
MIT License. Built for demo and educational purposes.
