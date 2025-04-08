PROJECT SETUP & DEVELOPMENT PLAN

🛠️ Step 1: Set Up the Project Structure
Create the directory structure:

mkdir -p feddit_sentiment_service/app
mkdir -p feddit_sentiment_service/tests
mkdir -p feddit_sentiment_service/.github/workflows

touch app/__init__.py app/main.py app/models.py app/routes.py app/sentiment.py app/feddit_client.py
touch tests/test_sentiment.py tests/test_routes.py
touch .github/workflows/ci.yml requirements.txt README.md run.sh

Step 2: Set Up a Virtual Environment

From inside feddit_sentiment_service:

python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
Install required packages: pip install -r requirements.txt


Step 4: Build the Application

main.py – FastAPI entry point

routes.py – API routes to fetch and analyze comments

feddit_client.py – Fetch recent comments from Feddit API

sentiment.py – Analyze polarity and classify text

models.py – Define response schemas (optional but clean)


✅ Step 5: Write Tests
Use pytest to test:

Sentiment classification

API responses (mocked if needed)

🤖 Step 6: Setup GitHub Actions CI
Define a workflow in .github/workflows/ci.yml:

Run linting (flake8)

Run tests (pytest)

▶️ Step 7: Run & Test Your API Locally

uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000/analyze/{subfeddit}

## To run the project at your disposal:
run the command: `./run.sh`