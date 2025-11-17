import os
import re
import requests
import time
from datetime import datetime
from requests.auth import HTTPBasicAuth

def get_wakatime_projects(api_key):
    """Fetch WakaTime project stats for last 7 days with retry logic"""
    url = "https://wakatime.com/api/v1/users/current/stats/last_7_days"

    print(f"🔑 Using API key: {api_key[:15]}...")
    print(f"📡 Fetching from: {url}")

    # Retry logic with exponential backoff
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(
                url,
                auth=HTTPBasicAuth(api_key, ''),
                timeout=10
            )
            print(f"📊 Response status: {response.status_code}")

            if response.status_code == 200:
                data = response.json()
                projects = data.get('data', {}).get('projects', [])
                print(f"✅ Found {len(projects)} projects in API response")
                return projects
            elif response.status_code == 503:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt
                    print(f"⚠️ Service unavailable, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                    continue
                else:
                    raise Exception("WakaTime API is currently unavailable")
            else:
                response.raise_for_status()

        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
                print(f"⚠️ Request failed: {e}, retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise

    return []

def format_time(total_seconds):
    """Format seconds into hours and minutes"""
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)

    if hours > 0:
        return f"{hours} hrs {minutes} mins"
    else:
        return f"{minutes} mins"

def create_bar(percent):
    """Create a progress bar based on percentage"""
    filled = int(percent / 4)  # 25 blocks for 100%
    empty = 25 - filled
    return "█" * filled + "░" * empty

def update_readme(projects):
    """Update README with project stats"""
    readme_path = "README.md"

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Format projects section
    if not projects:
        projects_text = "```txt\nNo project data available\n```"
    else:
        projects_text = "```txt\n"
        for project in projects[:5]:  # Top 5 projects
            name = project.get('name', 'Unknown')
            time_str = format_time(project.get('total_seconds', 0))
            percent = project.get('percent', 0)
            bar = create_bar(percent)

            # Format with proper spacing (24 chars for name, 20 for time, 25 for bar, 8 for percent)
            projects_text += f"{name:<24} {time_str:<19} {bar}   {percent:05.2f} %\n"

        projects_text += "```"

    # Update the waka-projects section
    pattern = r'<!--START_SECTION:waka-projects-->.*?<!--END_SECTION:waka-projects-->'
    replacement = f'<!--START_SECTION:waka-projects-->\n\n{projects_text}\n\n<!--END_SECTION:waka-projects-->'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("✅ README updated successfully!")

if __name__ == "__main__":
    api_key = os.environ.get('WAKATIME_API_KEY')

    if not api_key:
        print("❌ WAKATIME_API_KEY not found in environment variables")
        exit(1)

    try:
        projects = get_wakatime_projects(api_key)

        if not projects:
            print("⚠️ No projects found")
            exit(0)

        print(f"📊 Found {len(projects)} projects")
        update_readme(projects)

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        exit(1)
