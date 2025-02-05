🚀 Crypto Price Predictor - Backend Setup Guide

This guide will walk you through setting up the backend for the Crypto Price Predictor app, including installing Ollama and downloading the DeepSeek-R1-1.5B model.
🛠 Prerequisites

Before you start, ensure you have the following installed:

    Python 3.8+
    pip (Python package manager)
    Flask
    Ollama (For AI-powered predictions)

📌 1. Install Ollama

Ollama is required to run AI models locally.
Windows

    Download Ollama from the official website:
    👉 https://ollama.com/download
    Run the installer and follow the setup instructions.

Mac (Intel or Apple Silicon)

brew install ollama

Linux (Debian/Ubuntu)

curl -fsSL https://ollama.com/install.sh | sh

Once installed, verify by running:

ollama --version

📌 2. Download DeepSeek-R1-1.5B Model

To use AI predictions, you need to download the DeepSeek-R1-1.5B model.

Run the following command:

ollama pull deepseek-r1:1.5b

This will download and prepare the model for use.
📌 3. Install Python Dependencies

Make sure to install the required Python packages:

pip install flask flask-cors requests

📌 4. Run the Backend

After setting up Ollama and installing dependencies, start the Flask backend:

python backend.py

This will start a local server at http://127.0.0.1:5000/api/ada-data.
📌 5. Verify Everything Works

Once the backend is running, test it by opening your browser or using cURL:

curl http://127.0.0.1:5000/api/ada-data

You should receive JSON data containing real-time ADA/USDT prices from Binance, CoinGecko, and CoinMarketCap, along with an AI prediction.
✅ You're Ready to Go!

Your backend is now set up and running. You can now fetch live crypto data and AI-powered predictions. 🚀


This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
