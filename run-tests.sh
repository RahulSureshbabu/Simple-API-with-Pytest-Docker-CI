#!/bin/sh

echo "Installing Python dependencies..."
pip install -r requirements.txt
echo "Python deps installed."

echo "Updating apt..."
apt update
echo "Apt updated."

echo "Installing system packages..."
dpkg --configure -a || echo "dpkg configure failed"
apt install -y wget || echo "wget install failed"
apt install -y unzip || echo "unzip install failed"
apt install -y openjdk-21-jre-headless || echo "java install failed"
echo "System packages installed."

echo "Downloading Allure..."
curl -L -o allure.zip "https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.zip"
echo "Allure downloaded."

echo "Unzipping Allure..."
unzip allure.zip
chmod +x /app/allure-2.24.0/bin/allure
echo "Allure unzipped and executable."

echo "Setting PATH..."
export PATH=$PATH:/app/allure-2.24.0/bin
echo "PATH set: $PATH"

echo "Running pytest..."
pytest --alluredir=allure-results
echo "Pytest completed."

echo "Generating Allure report..."
/app/allure-2.24.0/bin/allure generate allure-results --clean -o allure-report
echo "Allure report generated."

echo "Checking results..."
ls -la allure-results/
ls -la allure-report/