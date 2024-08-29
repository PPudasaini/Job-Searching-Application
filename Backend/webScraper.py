import os
from dotenv import load_dotenv
from pathlib import Path
from serpapi import GoogleSearch


dotenv_path = Path("../.env")
load_dotenv(dotenv_path=dotenv_path)

SERP_API_KEY = os.getenv("SERP-API-KEY")


def get_jobs_24h():
    params = {
        "engine": "google_jobs",
        "q": "Junior Web Developer",
        "hl": "en",
        "location": "London,England,United Kingdom",
        "chips": "date_posted:day",
        "api_key": SERP_API_KEY
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    jobs_results = results["jobs_results"]
    print(jobs_results)


if __name__ == '__main__':
    get_jobs_24h()
