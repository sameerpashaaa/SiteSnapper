# SiteSnapper

**SiteSnapper** is a Python script that clones the front-end of any publicly accessible website by downloading its HTML, CSS, JavaScript, images, and rendering dynamic content using a headless browser. All you need is the website's URL.

---

## 🚀 Features

* Downloads:

  * Fully rendered **HTML** (after JavaScript execution)
  * External **CSS** and **JavaScript**
  * **Images**
* Handles both absolute and relative URLs
* Organizes content into structured folders (`css/`, `js/`, `images/`)
* Uses **Selenium** for rendering JavaScript-heavy pages
* Simple CLI input — no coding knowledge needed

---

## 🛠️ How It Works

1. **Takes a URL input** from the user.
2. Uses **Selenium with headless Chrome** to load the webpage and execute JavaScript.
3. Extracts:

   * Final HTML content
   * Linked CSS and JS files
   * Images
4. Downloads these resources using `requests`.
5. Saves everything in a local folder named after the domain (e.g., `example_com`).

---

## 📁 Output Structure

```
cloned_website/
└── example_com/
    ├── index.html
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png
```

---

## ⚙️ Requirements

Install dependencies using `pip`:

```bash
pip install requests beautifulsoup4 selenium webdriver-manager
```

You also need **Google Chrome** installed (the script uses ChromeDriver).

---

## ▶️ Usage

```bash
python SiteSnapper.py
```

Then, when prompted:

```
Enter the website URL to clone (e.g., https://example.com):
```

After completion, check the `cloned_website` folder on your Desktop.

---

## 📌 Notes

* Only **publicly accessible** resources can be downloaded.
* **Videos**, fonts, or embedded resources like iframes are not included (yet).
* This tool is for **educational or research purposes**. Do not use it to infringe on copyrighted content.

---

