#!/usr/bin/env bash
#
# Install module related dependencies
#
set -e

echo "Installing Chrome Browser"
curl -fsSL https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --yes --dearmor -o /usr/share/keyrings/chrome.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/chrome.gpg] " \
        "http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list

apt-get update
apt-get install -y google-chrome-stable
