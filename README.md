<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Instagram Public Profile Data Scraper | Exact Followers Count</title>

<meta name="description" content="Python web scraping tool to fetch exact Instagram followers count and public profile data without login, cookies, or authentication.">
<meta name="keywords" content="instagram followers count, exact followers instagram, instagram public data, instagram analytics, web scraping python, instagram scraper, social media analytics">

<style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.8;
        max-width: 900px;
        margin: auto;
        padding: 24px;
        background-color: #f9f9f9;
        color: #333;
    }
    h1, h2, h3 {
        color: #2c3e50;
        margin-top: 30px;
    }
    p {
        margin-bottom: 16px;
    }
    ul {
        margin-bottom: 20px;
    }
    li {
        margin-bottom: 8px;
    }
    code {
        background: #ecf0f1;
        padding: 3px 6px;
        border-radius: 4px;
    }
    pre {
        background: #ecf0f1;
        padding: 14px;
        border-radius: 6px;
        overflow-x: auto;
    }
    .note {
        background: #eef6ff;
        padding: 14px;
        border-left: 4px solid #2980b9;
        margin: 24px 0;
    }
</style>
</head>

<body>

<h1>Instagram Public Profile Data Scraper</h1>

<p>
This project is a Python-based web scraping tool designed to retrieve
public Instagram profile data with a strong focus on accuracy and transparency.
Its main goal is to extract the exact follower count that Instagram does not
display clearly in its user interface.
</p>

<div class="note">
<p>
Instagram shows follower numbers in an abbreviated format.
For example, an account may appear as having 10K followers.
This tool retrieves the real numeric value behind that number.
</p>

<p>
Instagram display example: 10K followers<br>
Actual data returned by this tool: 10,436 followers
</p>
</div>

<h2>Project Overview</h2>

<p>
Instagram limits the visibility of exact numbers by rounding large values.
This project demonstrates how public Instagram data can be accessed
programmatically to retrieve precise numerical values.
It is intended as a practical example of web scraping using Python
and public endpoints.
</p>

<h2>Key Features</h2>

<ul>
    <li>Retrieves the exact Instagram followers count without rounding</li>
    <li>Fetches public Instagram profile data only</li>
    <li>Works without login or authentication</li>
    <li>No Instagram account required</li>
    <li>No cookies are stored or reused</li>
    <li>Simple usage through username or public profile URL</li>
</ul>

<h2>Public Data Collected</h2>

<ul>
    <li>Exact followers count</li>
    <li>Total number of posts</li>
    <li>Total reels or clips count if available</li>
    <li>Account privacy status</li>
    <li>Verification status</li>
    <li>Account type</li>
    <li>Profile biography and full name</li>
    <li>Profile picture URL</li>
</ul>

<h2>Authentication and Privacy</h2>

<p>
This tool operates without logging in to Instagram.
It does not require a username, password, session, or cookies.
</p>

<p>
The user only needs to provide one of the following:
</p>

<ul>
    <li>An Instagram username</li>
    <li>A public Instagram profile link</li>
</ul>

<p>
All retrieved data is publicly available and accessible without authentication.
</p>

<h2>How It Works</h2>

<p>
The script uses Python and standard HTTP requests to process
publicly available information exposed on Instagram public profile pages.
It extracts raw numeric values that are not fully visible through
the Instagram interface.
</p>

<p>
This makes the project useful for understanding how social media platforms
handle public data and how web scraping techniques can be applied responsibly.
</p>

<h2>Installation</h2>

<pre><code>git clone https://github.com/walieed122/instagram-public-metrics.git
cd instagram-public-metrics
pip install -r requirements.txt
</code></pre>

<h2>Usage</h2>

<pre><code>python main.py
</code></pre>

<p>
After running the script, enter an Instagram username or a public profile URL.
The script will print the extracted public profile data in a clear format.
</p>

<h2>Project Structure</h2>

<pre><code>main.py
requirements.txt
README.md
DISCLAIMER.md
</code></pre>

<h2>Use Cases</h2>

<ul>
    <li>Learning Python web scraping</li>
    <li>Instagram follower count analysis</li>
    <li>Comparing public Instagram accounts</li>
    <li>Educational and research projects</li>
    <li>Understanding public social media data</li>
</ul>

<h2>Disclaimer</h2>

<p>
This project accesses publicly available Instagram data only.
It is intended for educational and analytical purposes.
Please review the DISCLAIMER file before using this tool.
</p>

</body>
</html>
