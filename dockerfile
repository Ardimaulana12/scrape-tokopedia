FROM python:3.11-slim-bullseye

WORKDIR /home/scraping

# Pastikan pip versi terbaru
RUN python -m ensurepip && python -m pip install --upgrade pip

# Install dependencies untuk Selenium
RUN apt-get update && apt-get install -y wget unzip && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean 

COPY . .

RUN apt-get update && apt-get install -y xvfb && \
    apt update && apt install -y psmisc


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt --index-url https://mirrors.aliyun.com/pypi/simple/

# # Tentukan volume jika ingin menyimpan hasil scraping di luar container
# VOLUME [ "/data/scraping" ]

# Direktori untuk menyimpan hasil scraping
RUN mkdir -p /home/scraping/output

CMD ["bash"]