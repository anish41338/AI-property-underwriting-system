# AI-Powered Property Underwriting System

An advanced backend API for automated property risk assessment—leveraging AI document analysis, computer vision, natural language processing (NLP), and business rule automation. Upload property documents and photos, and receive real-time underwriting decisions.

## 🚀 Features

- **File Upload:** Upload property appraisal PDFs and images via API.
- **AI Document Processing:** Automatically extracts structured info from reports using OCR and NLP.
- **Computer Vision:** Analyzes images to detect property attributes and visible hazards.
- **Automated Risk Assessment:** Scores property risk based on file contents, analysis models, and business rules.
- **Compliance Checking:** Ensures all assessments comply with customizable underwriting guidelines.
- **Modern API Docs:** Fully interactive API documentation via FastAPI Swagger UI.

## 🏗️ Project Structure

```
property-underwriting-system/
├── src/
│   ├── core/
│   ├── data/
│   ├── models/
│   ├── rules/
│   ├── api/
│   ├── services/
│   └── utils/
├── tests/
├── config/
├── data/
├── docs/
├── scripts/
├── docker/
├── requirements.txt
├── setup.py
├── main.py
└── .env.example
```

## ⚡ Quickstart

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/property-underwriting-system.git
cd property-underwriting-system
```

### 2. Install Dependencies

(Recommended: use a Python 3.11+ virtual environment)
```bash
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL & Tesseract

- **PostgreSQL:** Install and create the `underwriting_db` database.
- **Tesseract OCR:** Install from [UB Mannheim's Tesseract Releases](https://github.com/UB-Mannheim/tesseract/releases).
  - Add Tesseract path to your `.env`

### 4. Configure Environment

- Copy `.env.example` to `.env` and fill out details for:
  - `DATABASE_URL`
  - `SECRET_KEY`
  - `TESSERACT_PATH`
  - Other settings as needed

### 5. Run Database Setup

```bash
python scripts/setup_database.py
```

### 6. Download spaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 7. Start the Server

```bash
python main.py
```

Browse to http://localhost:8000/docs for interactive testing.

## 🧩 API Overview

- **POST `/api/v1/upload`** : Upload files for assessment
- **POST `/api/v1/analyze`** : Trigger analysis on given files
- **GET `/api/v1/analysis/{analysis_id}`** : Check analysis status/result
- **GET `/health`** : Health check endpoint

View all endpoints with schemas at `/docs`.

## 🔐 Security

- Uses JWT tokens for API authentication (if enabled).
- Environment variables for all sensitive keys and path configurations.
- Supports file size and type validation.

## 📝 Customization

- Add your business rules to `src/rules/underwriting_rules.py`
- Enhance document analysis with real ML/NLP in `src/models/document_analysis/`
- Add more computer vision/AI models in `src/models/computer_vision/`

## 💡 Example Usage

1. Upload property files via API using Swagger or tools like Postman.
2. Use returned file info to invoke `/api/v1/analyze`.
3. See risk scores, extracted entities, and the automated decision in the response.

## 🧪 Testing

- Run unit/integration tests with:
  ```bash
  pytest
  ```

## 📦 Deployment

- Supports Docker deployment (see `docker` folder)
- Can be deployed to any modern cloud platform (AWS/GCP/Azure) or on-premises

## 🙋‍♂️ Questions & Contributions

Feel free to open issues or submit PRs. For questions or feature requests, open a GitHub issue.

## 🏁 License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
