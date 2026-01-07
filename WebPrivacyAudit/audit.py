import requests
import pandas as pd
import time
from datetime import datetime

# ==========================================
# 1. CONFIGURATION (Your Specific Target List)
# ==========================================
target_urls = [
    "https://www.chaitanya.edu.in",
    "https://jntuh.ac.in",
    "https://www.kakatiya.ac.in",
    "https://sru.edu.in",
    "https://www.cbit.ac.in",
    "https://www.lpu.in",        # <--- Make sure there is a comma here!
    "https://www.amity.edu",
    "https://www.upgrad.com",
    "https://www.byjus.com",
    "https://www.coursera.org"
]
# ==========================================
# 2. THE CLASSIFIER LOGIC (The "Brain")
# ==========================================
def classify_cookie(cookie_name):
    """
    Analyzes a cookie name and determines its likely purpose.
    """
    name = cookie_name.lower()
    
    # Category A: Analytics (Tracking user behavior)
    if any(x in name for x in ['_ga', '_gid', '_gat', 'utma', 'utmb', 'hj', 'pk_', 'analytics']):
        return "Analytics (Tracking)"
        
    # Category B: Marketing (Ads, Facebook, retargeting)
    elif any(x in name for x in ['fbp', 'ads', 'gcl', 'doubleclick', 'pixel', 'yt-', 'test_cookie']):
        return "Marketing (Ad Tracking)"
        
    # Category C: Functional (Login, Security, Session)
    elif any(x in name for x in ['session', 'csrf', 'xsrf', 'token', 'auth', 'id', 'ci_session', 'phpsessid', 'asp.net', 'jsessionid']):
        return "Functional (Safe)"
        
    # Category D: Unknown
    else:
        return "Unknown"

# ==========================================
# 3. THE SCANNER (The "Spy")
# ==========================================
results = []
print(f"--- Starting Privacy Audit on {len(target_urls)} websites ---\n")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

for url in target_urls:
    try:
        print(f"Scanning: {url} ...", end=" ")
        
        # Send request (timeout set to 10 seconds)
        response = requests.get(url, headers=headers, timeout=10)
        
        # Get cookies
        cookies = response.cookies
        
        # Analyze each cookie
        cookie_details = []
        tracking_found = "No"
        
        for c in cookies:
            category = classify_cookie(c.name)
            cookie_details.append(f"{c.name} [{category}]")
            
            # Check if we found any tracking cookies
            if "Tracking" in category:
                tracking_found = "YES (Violation)"

        # Store data
        results.append({
            "Website": url,
            "Status": "Accessible",
            "Total_Cookies": len(cookies),
            "Has_Tracking_Cookies": tracking_found,
            "Detailed_List": ", ".join(cookie_details),
            "Scan_Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        print("Done.")

    except Exception as e:
        print("Failed.")
        results.append({
            "Website": url,
            "Status": "Failed/Timeout",
            "Total_Cookies": 0,
            "Has_Tracking_Cookies": "N/A",
            "Detailed_List": str(e),
            "Scan_Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    # Wait 1 second to be polite to servers
    time.sleep(1)

# ==========================================
# 4. EXPORT RESULTS
# ==========================================
# Convert to DataFrame
df = pd.DataFrame(results)

# Save to CSV
filename = "privacy_audit_report.csv"
df.to_csv(filename, index=False)

print(f"\n[SUCCESS] Report saved as '{filename}'. Open it in Excel/Sheets to see results.")