FROM python:3.9-slim
WORKDIR /app
RUN pip install pandas
COPY process_telemetry.py .
CMD ["python", "process_telemetry.py"]