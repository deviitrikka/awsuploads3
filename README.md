# AWS S3 File Uploader

This project is a **Streamlit** web application that allows users to upload one
or more files to an AWS S3 bucket with automatic conflict handling and file size
validation.

---

## Features

- **Multiple File Upload:** Upload one or more files at once.
- **File Size Validation:** Files larger than 10MB are rejected.
- **Automatic Conflict Handling:** If a file with the same name exists, the app
  renames the new file to avoid overwriting.
- **Operation Logs:** All actions and errors are logged and displayed in the UI.
- **Secure AWS Credentials:** Uses Streamlit secrets for AWS credentials.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/deviitrikka/awsuploads3.git
cd awsupload
```

### 2. Install Dependencies

It is recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

Create a `.streamlit/secrets.toml` file in the project root with the following
content:

```toml
AWS_ACCESS_KEY_ID = "<your-access-key>"
AWS_SECRET_ACCESS_KEY = "<your-secret-key>"
AWS_DEFAULT_REGION = "<your-region>"
```

### 4. Set Your S3 Bucket Name

Edit `main1.py` and set the `BUCKET_NAME` constant to your S3 bucket name.

```
BUCKET_NAME = "your-bucket-name"
```

### 5. Run the App

```bash
streamlit run main1.py
```

---

## Usage

1. Open the app in your browser (the terminal will show the local URL).
2. Upload one or more files using the file uploader.
3. Click the **Upload** button.
4. View operation logs for upload status and any errors.

---

## Live Demo

**Live URL:** [https://awsuploads3.streamlit.app/]

---

## Project Structure

```
awsupload/
├── main1.py              # Streamlit app source code
├── requirements.txt      # Python dependencies
└── .streamlit/
    └── secrets.toml      # AWS credentials (not included in repo)
```

---

## Security Notes

- **Never commit your AWS credentials** to version control.
- Use Streamlit secrets or environment variables for sensitive information.

---

## License

[MIT License](LICENSE)

---

## Contact

For questions or support, please open an issue or contact the maintainer.
