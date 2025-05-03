
# 🛠️ Tech Job Scraper using SerpAPI

This Python script scrapes tech-related job postings from **Google Jobs** using the **SerpAPI** service. It collects relevant job information—such as titles, companies, locations, post dates, sources, descriptions, and application links—and saves everything to a structured CSV file for easy analysis.

---

## 📌 Features

- ✅ Scrapes jobs for **30+ tech roles** (e.g., frontend developer, data scientist, cybersecurity analyst)
- 🌍 Customizable **location** (default: Philippines)
- 🧠 Automatically avoids **duplicate job entries**
- 📝 Outputs results to a CSV file: `google_jobs_all_links.csv`
- 🔗 Collects **all available apply links** per job
- 📄 Console output with a quick summary of job details

---

## 📂 Output Format

Each row in the CSV includes:

| Column Name     | Description                            |
|----------------|----------------------------------------|
| Job Query      | The job title searched                 |
| Title          | Job title from the posting             |
| Company        | Company name                           |
| Location       | Job location                           |
| Posted         | How long ago the job was posted        |
| Source         | Where the listing was found (e.g., LinkedIn) |
| Apply Links    | Semicolon-separated links to apply     |
| Description    | Short job description text             |

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install requests
```

### 2. Get a SerpAPI Key

Sign up at [https://serpapi.com](https://serpapi.com) and get your API key.

Replace the placeholder in the code:

```python
API_KEY = "YOUR_SERPAPI_KEY"
```

### 3. Run the script

```bash
python job_scraper.py
```

By default, it searches for tech jobs in **Philippines**. You can change the location by modifying:

```python
run_multi_scraper("YourLocation")
```

---

## 📌 Notes

- The script will **append** new results to the existing CSV file while avoiding duplicates.
- Only basic job details are printed in the console. The full description is saved in the CSV.
- Make sure to respect API usage limits (free plans have request limits).

---

## 🧑‍💻 Author

Built by someone passionate about automation, data collection, and helping job seekers navigate the tech industry more efficiently.
