PROJECT SETUP & DEVELOPMENT PLAN
🛠️ Step 1: Set Up the Project Structure
Create the directory structure:

bash
Copy
Edit
mkdir -p feddit_sentiment_service/app
mkdir -p feddit_sentiment_service/tests
mkdir -p feddit_sentiment_service/.github/workflows
Add required files:

bash
Copy
Edit
touch app/__init__.py app/main.py app/models.py app/routes.py app/sentiment.py app/feddit_client.py
touch tests/test_sentiment.py tests/test_routes.py
touch .github/workflows/ci.yml requirements.txt README.md run.sh
🐍 Step 2: Set Up a Virtual Environment
From inside feddit_sentiment_service:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
📦 Step 3: Install Dependencies
Install required packages:

bash
Copy
Edit
pip3 install fastapi uvicorn requests textblob pytest flake8
Save to requirements.txt:

bash
Copy
Edit
pip freeze > requirements.txt
💬 Step 4: Build the Application
You’ll write code for:

main.py – FastAPI entry point

routes.py – API routes to fetch and analyze comments

feddit_client.py – Fetch recent comments from Feddit API

sentiment.py – Analyze polarity and classify text

models.py – Define response schemas (optional but clean)

⚙️ Step 5: Add Optional Features
Filter by time range

Sort by polarity score

✅ Step 6: Write Tests
Use pytest to test:

Sentiment classification

API responses (mocked if needed)

🤖 Step 7: Setup GitHub Actions CI
Define a workflow in .github/workflows/ci.yml:

Run linting (flake8)

Run tests (pytest)

▶️ Step 8: Run & Test Your API Locally
bash
Copy
Edit
uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000/analyze/{subfeddit}

📦 Step 9: Push to GitHub or Zip the Folder
Make sure your final repo includes:

All code

requirements.txt

README.md with clear instructions

