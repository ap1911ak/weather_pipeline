# ใช้ Python Image แบบเบา
FROM python:3.9-slim

# ตั้งค่า Working Directory
WORKDIR /app

# Copy ไฟล์ที่จำเป็น
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# สร้างโฟลเดอร์เก็บข้อมูล
RUN mkdir data

# รัน Script เมื่อสั่ง start container
CMD ["python", "src/main.py"]