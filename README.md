# Instagram Public Profile Data Scraper  
### Exact Followers Count & Public Instagram Data

A Python-based web scraping tool designed to retrieve **exact Instagram followers count**
and other **public profile data** without login, authentication, or cookies.

Instagram displays follower numbers in an abbreviated format such as **10K** or **1M**.  
This tool retrieves the **real numeric value** behind those numbers.

**Example:**
- Instagram display: `10K followers`
- Actual value returned by this tool: `10,436 followers`

---

## Project Overview

Instagram limits the visibility of precise metrics by rounding large numbers.
This project demonstrates how **public Instagram profile data**
can be accessed programmatically to extract **accurate numerical values**.

The main focus of this project is **data accuracy and transparency**,
making it a practical example of responsible **Python web scraping**
using public endpoints.

---

## Key Features

- Retrieves the **exact Instagram followers count** (no rounding)
- Fetches **public Instagram profile data only**
- Works **without login or authentication**
- No Instagram account required
- No cookies are stored or reused
- Simple input: username or public profile URL

---

## Public Data Collected

- Exact followers count
- Total number of posts
- Total reels or clips count (if available)
- Account privacy status
- Verification status
- Account type
- Profile biography and full name
- Profile picture URL

---

## Authentication & Privacy

This tool operates **without logging in** to Instagram.

It does **not** require:
- Username or password
- Session tokens
- Stored or reused cookies

The user only needs to provide:
- An Instagram username  
**or**
- A public Instagram profile URL

All retrieved data is **publicly accessible** without authentication.

---

## How It Works

The script uses Python and standard HTTP requests to interact with
Instagram public GraphQL endpoints.

It extracts **raw numeric values** that are not fully visible
through Instagram’s user interface.

This makes the project useful for:
- Understanding how social media platforms expose public data
- Learning real-world web scraping techniques
- Analyzing public Instagram metrics accurately

---

## Installation

```bash
git clone https://github.com/walieed122/Instagram-Follower-Count-Public-Profile-Data-Scraper.git
cd Instagram-Follower-Count-Public-Profile-Data-Scraper
pip install -r requirements.txt