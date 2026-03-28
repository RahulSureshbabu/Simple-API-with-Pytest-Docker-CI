# Simple API with Pytest, Docker, and CI

A beginner-friendly project that demonstrates:

- A Node.js API (`GET /hello`, `PUT /hello`)
- Automated API tests with Python + `pytest`
- Docker/Docker Compose test execution
- Allure test reporting (`allure-results` + HTML `allure-report`)

---

## Quick Start (5 Commands)

Run these from the project root:

```bash
docker compose up --build --abort-on-container-exit
docker compose down
cd allure-report
python -m http.server 8000
# open http://localhost:8000
```

What you get:

- API runs in container
- Tests execute automatically
- Allure report is generated in `allure-report/`
- Report is viewable at `http://localhost:8000`

---

## 1) Project Structure

- `my-api/` → Express API code
- `tests/` → Pytest API tests
- `docker-compose.yml` → Runs API + test container together
- `run-tests.sh` → Installs tools in the test container, runs tests, builds Allure report
- `requirements.txt` → Python test dependencies

---

## 2) What Is Used in This Framework

### API Layer
- Node.js + Express
- Swagger UI for API docs (`/api-docs`)

### Test Layer
- Python 3
- `pytest`
- `requests`
- `allure-pytest`

### Execution Layer
- Docker + Docker Compose

### Reporting Layer
- Allure CLI (installed inside test container during run)
- Output folders:
	- `allure-results/` (raw test result files)
	- `allure-report/` (generated HTML report)

---

## 3) Prerequisites (Beginner Checklist)

Install these before running anything:

1. **Docker Desktop** (must be running)
2. **Git**
3. **Node.js 20+** (for local API run without Docker)
4. **Python 3.11+** (for local test run without Docker)

Optional but useful:
- VS Code
- Python extension

---

## 4) Clone and Open the Project

```bash
git clone <your-repo-url>
cd Simple-API-with-Pytest-Docker-CI
```

If using VS Code:

```bash
code .
```

---

## 5) Run API Locally (Without Docker)

### Step 1: Install API dependencies

```bash
cd my-api
npm install
```

### Step 2: Start the API

```bash
npm start
```

API is available at:

- `http://localhost:3000/hello`
- `http://localhost:3000/api-docs`

Expected sample response from GET:

```json
{"message":"Hello World!"}
```

---

## 6) Run Tests Locally (Without Docker)

Open a **new terminal** at the project root.

### Step 1: Create and activate virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 2: Install test dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Point tests to your local API

Windows PowerShell:

```powershell
$env:API_BASE="http://localhost:3000"
```

macOS/Linux:

```bash
export API_BASE="http://localhost:3000"
```

### Step 4: Run tests

```bash
pytest
```

### Optional: generate local Allure raw results

```bash
pytest --alluredir=allure-results
```

---

## 7) Run Tests in Container (Recommended)

From project root:

```bash
docker compose up --build --abort-on-container-exit
```

What this does:

1. Builds API image from `my-api/`
2. Starts API container
3. Starts test container (`python:3.13`)
4. Test container runs `run-tests.sh`
5. Script installs Python/system dependencies
6. Script runs `pytest --alluredir=allure-results`
7. Script generates Allure HTML report into `allure-report/`

When complete, stop and clean containers:

```bash
docker compose down
```

---

## 8) How to Gather and Read Test Results

After test execution, check these outputs in project root:

### 1. Raw Allure data
- Folder: `allure-results/`
- Contains JSON result artifacts from each test

### 2. Allure HTML report
- Folder: `allure-report/`
- Open `allure-report/index.html` in a browser

If browser shows loading forever when opened directly from file explorer, serve it with a local HTTP server:

```bash
cd allure-report
python -m http.server 8000
```

Then open:

- `http://localhost:8000`

### 3. Optional JUnit XML
- File: `results.xml` (if generated in your flow)
- Useful for CI systems and test dashboards

---

## 9) Useful Commands

Run full container flow:

```bash
docker compose up --build --abort-on-container-exit
```

Stop and remove containers:

```bash
docker compose down
```

Re-run tests cleanly (remove old result artifacts first):

```bash
rm -rf allure-results allure-report
docker compose up --build --abort-on-container-exit
```

On Windows PowerShell (clean artifacts):

```powershell
Remove-Item -Recurse -Force allure-results, allure-report
docker compose up --build --abort-on-container-exit
```

---

## 10) Troubleshooting (Beginner Friendly)

### Issue: `openjdk-17-jre-headless` not found
- Fix already applied: project uses `openjdk-21-jre-headless`

### Issue: Allure report is blank or stuck on loading
- Serve report over HTTP:
	- `cd allure-report`
	- `python -m http.server 8000`
	- open `http://localhost:8000`

### Issue: API tests fail with connection error
- Ensure API container is healthy in Docker logs
- For local runs, ensure API is running on `http://localhost:3000`

### Issue: Docker command not found
- Install Docker Desktop and restart terminal

---

## 11) Expected Test Status

Current suite has 7 tests total.

- 6 tests are expected to pass.
- 1 test is intentionally failing as an example: `tests/api_test.py::test_put_missing_message`
	- Purpose: demonstrates how a negative validation failure appears in pytest/Allure.
	- Current behavior: API returns `200` for `PUT /hello` with an empty body (`{}`).
	- Test expectation: should return `400` for missing `message`.

---

## 12) Next Improvements (Optional)

- Add GitHub Actions workflow steps to publish Allure artifacts
- Add Makefile or task shortcuts for one-command local runs
- Add API negative test cases and schema validation tests
