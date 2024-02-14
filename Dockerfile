FROM python:3.9.18-slim-bullseye
COPY . .
RUN pip install -r requirements.txt
# streamlit run your_app.py --server.port $PORT
EXPOSE 3000
ARG PORT
RUN echo $PORT
CMD ["streamlit", "run", "app.py", "--server.port", "$PORT"]

