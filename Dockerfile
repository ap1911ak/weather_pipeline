FROM python:3.9-slim

WORKDIR /app

# 1. จัดการ dependencies (ลบ  ออกแล้ว)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copy ไฟล์ทั้งหมดเข้าเครื่อง
COPY . .

# 3. ตั้งค่า PYTHONPATH ให้ชี้มาที่ /app เพื่อให้หา src เจอ
ENV PYTHONPATH=/app

# 4. รันด้วยคำสั่ง -m (Module) เพื่อให้จัดการ Path ให้อัตโนมัติ
CMD ["python", "-m", "src.main"]