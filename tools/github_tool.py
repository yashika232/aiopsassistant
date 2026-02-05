import os
import requests
import time

def search_github(query: str, limit: int = 3, retries: int = 2):
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }

    for attempt in range(retries):
        try:
            response = requests.get(
                "https://api.github.com/search/repositories",
                headers=headers,
                params={"q": query, "sort": "stars"}
            )
            response.raise_for_status()
            data = response.json()

            return [
                {
                    "name": repo["full_name"],
                    "stars": repo["stargazers_count"],
                    "url": repo["html_url"]
                }
                for repo in data["items"][:limit]
            ]

        except Exception as e:
            if attempt == retries - 1:
                return {"error": str(e)}
            time.sleep(1)
