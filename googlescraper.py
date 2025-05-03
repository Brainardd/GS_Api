import requests
import csv
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Your SerpAPI key
API_KEY = "934b6bde4b70e1c8e4e631e822fef605fec4e1f6b9f6cf34fd3ad133784f481e"

# Tech-related job titles
job_titles = [
    "software developer", "frontend developer", "backend developer", "full stack developer", "web developer",
    "mobile app developer", "UI/UX designer", "web designer", "QA tester", "game developer", "DevOps engineer",
    "data analyst", "data scientist", "data engineer", "machine learning engineer", "AI specialist",
    "cloud engineer", "cloud architect", "network administrator", "system administrator",
    "cybersecurity analyst", "penetration tester", "IT support specialist", "product manager",
    "blockchain developer", "AR/VR developer", "robotics engineer", "technical support engineer"
]

def scrape_google_jobs_with_all_links(job_query, location, seen_jobs):
    params = {
        "engine": "google_jobs",
        "q": f"{job_query} in {location}",
        "hl": "en",
        "api_key": API_KEY
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    jobs = data.get("jobs_results", [])
    new_jobs = []

    for job in jobs:
        title = job.get('title', 'N/A')
        company = job.get('company_name', 'N/A')
        unique_key = f"{title}|{company}"

        if unique_key in seen_jobs:
            continue

        seen_jobs.add(unique_key)
        location = job.get('location', 'N/A')
        posted = job.get('detected_extensions', {}).get('posted_at', 'N/A')
        description = job.get('description', '')
        source = job.get('via', 'N/A')

        apply_links = []
        if "apply_options" in job:
            for option in job["apply_options"]:
                link = option.get("link")
                if link and link not in apply_links:
                    apply_links.append(link)

        new_jobs.append([job_query, title, company, location, posted, source, "; ".join(apply_links), description])


        # Optional console output
        print(f"\n{title} @ {company}")
        print(f"• Location : {location}")
        print(f"• Posted   : {posted}")
        print(f"• Source   : {source}")
        print(f"• Links:")
        for l in apply_links:
            print(f"   - {l}")
        print(f"• Description: {description[:150]}...")

    return new_jobs


def run_multi_scraper(location="Philippines"):
    file_path = "google_jobs_all_links.csv"
    file_exists = os.path.isfile(file_path)

    seen_jobs = set()

    if file_exists:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                if len(row) >= 2:
                    seen_jobs.add(f"{row[0]}|{row[1]}")

    with open(file_path, "a", newline='', encoding="utf-8-sig") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["Job Query", "Title", "Company", "Location", "Posted", "Source", "Apply Links", "Description"])


        for job_query in job_titles:
            print(f"\nSearching: {job_query}")
            new_entries = scrape_google_jobs_with_all_links(job_query, location, seen_jobs)
            writer.writerows(new_entries)

    print("\nAll job results saved/appended to google_jobs_all_links.csv")

# Run the script
run_multi_scraper("Philippines")
