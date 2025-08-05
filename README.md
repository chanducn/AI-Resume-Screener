# 📝 AI Resume Screener

An intelligent resume screening system that uses AI to match job descriptions with candidate resumes and provide relevancy scores.

## 🌟 Features

- **Job Description Input**: 
  - Paste directly or upload .txt file
  - Flexible input options for recruiters

- **Resume Processing**:
  - Bulk PDF resume upload
  - Automatic text extraction
  - Smart chunking and embedding

- **AI-Powered Analysis**:
  - Semantic matching using BERT embeddings
  - Intelligent scoring system (1-10)
  - Detailed reasoning for each score

- **User-Friendly Interface**:
  - Clean Gradio web interface
  - Real-time processing
  - Clear result display

## 🚀 Getting Started

### Prerequisites

```bash
python 3.8+
pip install -r requirements.txt
```

### Environment Setup

1. Create a `.env` file in the project root:
```properties
GROQ_API_KEY=your_groq_api_key_here
```

2. Install dependencies:
```bash
pip install gradio
pip install sentence-transformers
pip install pdfplumber
pip install groq
pip install faiss-cpu
pip install python-dotenv
```

### Running the App

```bash
python app.py
```

## 📂 Project Structure

```
AI_Resume_Screener/
├── app.py                    # Main Gradio web interface
├── job_desc.py              # Job description handling
├── extractor.py             # PDF parsing utilities
├── Chunking_and_Embedding.py # Text processing & embeddings
├── job_desc_emb.py          # Job description embedding
├── LLM_model.py             # Language model integration
└── main.py                  # CLI version of the tool
```

## 🛠️ How It Works

1. **Input Processing**:
   - Parse job descriptions from text/file
   - Extract text from PDF resumes

2. **Text Analysis**:
   - Chunk text into processable segments
   - Generate embeddings using BERT

3. **Matching**:
   - Compare job and resume embeddings
   - Retrieve most relevant sections

4. **Scoring**:
   - AI evaluation of candidate fit
   - Score generation with reasoning

## 🔑 API Keys

The project uses the Groq API for language model capabilities. You'll need to:
1. Get an API key from Groq
2. Add it to your `.env` file
3. Never commit the `.env` file (it's in .gitignore)

## 📚 Models Used

- **Embedding**: all-MiniLM-L6-v2
- **LLM**: Gemma 2B via Groq

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## ⚖️ License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- SentenceTransformers for embeddings
- Groq for LLM API
- Gradio for the web interface

## 📸 Project Screenshots
These are project screenshots that showcase key features and workflows:
![Homepage Screenshot](https://github.com/chanducn/AI-Resume-Screener/blob/0f964b2a2390cbd300174dc613ce7a968c3ed29a/Screenshot%202025-08-05%20120818.png)
![Dashboard View](https://github.com/chanducn/AI-Resume-Screener/blob/0f964b2a2390cbd300174dc613ce7a968c3ed29a/Screenshot%202025-08-05%20121020.png)


Replace images/homepage.png and images/dashboard.png with the actual paths or URLs to your screenshots.

If you'd like to resize or style them with HTML for more control, just let me know—I can help fine-tune it for a polished presentation.
