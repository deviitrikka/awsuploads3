import streamlit as st
import boto3
import os
import time
from botocore.exceptions import NoCredentialsError, ClientError

# --- Constants ---
BUCKET_NAME = "bucketforme9090"
MAX_FILE_SIZE_MB = 10

# Access secrets
aws_access_key = st.secrets["AWS_ACCESS_KEY_ID"]
aws_secret_key = st.secrets["AWS_SECRET_ACCESS_KEY"]
aws_region = st.secrets["AWS_DEFAULT_REGION"]

# Create S3 client using secrets
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Now you can use s3.upload_fileobj(), etc.


# --- Logger setup ---
log_messages = []

def log(msg):
    log_messages.append(msg)
    st.session_state.logs = log_messages

def check_file_size(file):
    size_mb = len(file.getvalue()) / (1024 * 1024)
    return size_mb <= MAX_FILE_SIZE_MB

def generate_unique_filename(original_name):
    base, ext = os.path.splitext(original_name)
    timestamp = int(time.time() * 1000)
    return f"{base}_{timestamp}{ext}"

def upload_to_s3(file, filename):
    try:
        s3.upload_fileobj(file, BUCKET_NAME, filename)
        log(f"Uploaded: `{filename}` to S3.")
    except NoCredentialsError:
        log("AWS credentials not found.")
    except ClientError as e:
        log(f" AWS error: {e}")

def file_exists(filename):
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=filename)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            return False
        raise

# --- Streamlit UI ---
st.title("Upload Two Files to S3 with Conflict Handling")
files = st.file_uploader("Upload one or more files", key="file1", accept_multiple_files=True)


if st.button("Upload"):
    if not files:
        st.warning("Please upload at least 1 file")
    else:
        for file in files:
            original_name = file.name
            # if not check_file_size(file):
            #     log(f"File too large: `{original_name}` exceeds {MAX_FILE_SIZE_MB}MB.")
            #     continue

            filename = original_name
            if file_exists(filename):
                filename = generate_unique_filename(original_name)
                log(f"File name conflict. Renamed to `{filename}`.")

            upload_to_s3(file, filename)

# --- Log Output ---
st.subheader("Operation Logs")
if "logs" not in st.session_state:
    st.session_state.logs = []

for msg in st.session_state.logs:
    st.write(msg)
