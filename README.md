# How To Run Scraping

make sure you have python on your computer

## Run With Docker

Clone the project

```bash
  git clone https://github.com/Ardimaulana12/scrape-tokopedia.git
```

run docker compose

```bash
  docker compose up -d --build
```

sign to terminal

```bash
  docker container exec -it scraping-tokped bash
```

run script

```bash
  python main.py
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/Ardimaulana12/scrape-tokopedia.git
```

Go to the project directory

```bash
  cd scrape-tokopedia
```

Create Environment file

```bash
  python -m venv env
```

activating Environment file

```bash
  source env/scripts/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the scraping

```bash
  cd src/
  python main.py
```
