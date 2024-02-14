FROM python:3.9.18-slim-bullseye
COPY . .
RUN pip install -r requirements.txt
# streamlit run your_app.py --server.port $PORT
ARG PORT
RUN echo $PORT
ENV PORT ${PORT}
EXPOSE ${PORT}

CMD streamlit run main.py --server.port ${PORT}

