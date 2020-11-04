FROM python:3
WORKDIR /ProjectPurpleCow
COPY ./ProjectPurpleCow /ProjectPurpleCow
COPY ./requirements.txt /ProjectPurpleCow
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
ENTRYPOINT ["python", "init.py"]
