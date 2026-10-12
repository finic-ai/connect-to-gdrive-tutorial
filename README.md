> **This is a legacy tutorial from Psychic, the company now called Finic, and is no longer maintained. The Psychic service it depends on is no longer available, so the code will not run as written.** Finic now builds AI to stop fraud, abuse and financial crimes: [Finic Grayson](https://docs.finic.ai), a decision model API for real-time fraud and risk decisions, and agents for fraud investigations. See [finic.ai](https://finic.ai).

# connect-to-gdrive-tutorial
This is the code for the tutorial [here](www.psychic.dev/post/how-to-connect-the-gdrive-api-to-langchain), showing how to connect files from a Google Drive account to LLMs using Psychic, Chroma, and LangChain.

## Running
1. Create an account at https://dashboard.psychic.dev/ (it's free) and connect a Google Drive account.
2. Rename `rename.env` to `.env` and fill in your own OPENAI_API_KEY and PSYCHIC_SECRET_KEY.
3. Replace `account_id` in `main.py` with the Account ID you used to connect to Google Drive in step 1.
4. [Install poetry](https://python-poetry.org/docs/) to run this project in a virtual environment.
5. Run the following in order:
    ```bash
    poetry install
    poetry shell
    python main.py
    ```