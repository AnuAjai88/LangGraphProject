# Base image with Python
FROM python:3.9-slim

# Set environment variables
ENV HOME=/home/user
ENV STREAMLIT_HOME=$HOME/.streamlit
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Create streamlit config directory
RUN mkdir -p $STREAMLIT_HOME

# Copy your app code into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create minimal Streamlit config
RUN echo "\
[server]\n\
headless = true\n\
port = 7860\n\
enableCORS = false\n\
\n\
" > $STREAMLIT_HOME/config.toml

# Expose Streamlit port
EXPOSE 7860

# Run the app
CMD ["streamlit", "run", "app.py"]