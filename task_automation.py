from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import re

def scrape_and_save_title(url, output_file):
    print(f"Fetching data from {url}...")
    
    try:
        # 1. Download the webpage data
        headers = {'User-Agent': 'Mozilla/5.0'}
        request = Request(url, headers=headers)
        with urlopen(request) as response:
            html = response.read().decode(response.headers.get_content_charset() or 'utf-8')
        
        # 2. Use RegEx to search for the title tags in the HTML source code
        # re.IGNORECASE makes sure it catches <TITLE> or <title>
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        
        if title_match:
            # .group(1) gets the text *between* the tags
            page_title = title_match.group(1) 
            
            # 3. Save the result to a text file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(f"Website: {url}\n")
                file.write(f"Page Title: {page_title}\n")
                
            print(f"✅ Task complete! Saved title: '{page_title}' to '{output_file}'.")
        else:
            print("❌ Could not find a <title> tag on this webpage.")
            
    except (HTTPError, URLError, TimeoutError) as e:
        print(f"❌ Error fetching the webpage: {e}")

# --- Run the Script ---
scrape_and_save_title('https://en.wikipedia.org/wiki/Python_(programming_language)', 'website_title.txt')