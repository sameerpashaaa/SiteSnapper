import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import shutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_directory(directory):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_file(url, local_path):
    """Download a file from URL to local path"""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(local_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def clone_website(url, output_dir):
    """Clone a website using Selenium for JavaScript rendering"""
    # Setup output directory
    create_directory(output_dir)
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        print(f"Fetching {url}...")
        driver.get(url)
        
        # Wait for JavaScript to load
        time.sleep(5)
        
        # Get the page source after JavaScript execution
        html_content = driver.page_source
        
        # Parse HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Save the HTML
        with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as file:
            file.write(html_content)
        
        # Download CSS files
        css_files = soup.find_all('link', rel='stylesheet')
        for css in css_files:
            css_url = css.get('href')
            if css_url and not css_url.startswith(('http://', 'https://')):
                css_url = urllib.parse.urljoin(url, css_url)
            
            if css_url:
                css_filename = os.path.basename(urllib.parse.urlparse(css_url).path)
                css_local_path = os.path.join(output_dir, 'css', css_filename)
                create_directory(os.path.join(output_dir, 'css'))
                
                if download_file(css_url, css_local_path):
                    print(f"Downloaded CSS: {css_filename}")
        
        # Download JavaScript files
        js_files = soup.find_all('script', src=True)
        for js in js_files:
            js_url = js.get('src')
            if js_url and not js_url.startswith(('http://', 'https://')):
                js_url = urllib.parse.urljoin(url, js_url)
            
            if js_url:
                js_filename = os.path.basename(urllib.parse.urlparse(js_url).path)
                js_local_path = os.path.join(output_dir, 'js', js_filename)
                create_directory(os.path.join(output_dir, 'js'))
                
                if download_file(js_url, js_local_path):
                    print(f"Downloaded JS: {js_filename}")
        
        # Download images
        img_files = soup.find_all('img')
        for img in img_files:
            img_url = img.get('src')
            if img_url and not img_url.startswith(('http://', 'https://')):
                img_url = urllib.parse.urljoin(url, img_url)
            
            if img_url:
                img_filename = os.path.basename(urllib.parse.urlparse(img_url).path)
                img_local_path = os.path.join(output_dir, 'images', img_filename)
                create_directory(os.path.join(output_dir, 'images'))
                
                if download_file(img_url, img_local_path):
                    print(f"Downloaded Image: {img_filename}")
        
        print(f"Website cloned successfully to {output_dir}")
    
    except Exception as e:
        print(f"Error cloning website: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    # Ask for the website URL
    target_url = input("Enter the website URL to clone (e.g., https://example.com): ")
    
    # Validate URL format
    if not target_url.startswith(('http://', 'https://')):
        target_url = 'https://' + target_url
    
    # Create a folder name based on the domain
    domain = urllib.parse.urlparse(target_url).netloc
    folder_name = domain.replace('.', '_')
    
    # Set output directory
    output_directory = os.path.join(r"c:\Users\Sameer\OneDrive\Desktop\python projects\cloned_website", folder_name)
    
    print(f"Cloning {target_url} to {output_directory}...")
    clone_website(target_url, output_directory)
    print("Website cloning process completed!")