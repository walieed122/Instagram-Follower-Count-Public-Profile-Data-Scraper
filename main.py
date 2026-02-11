import requests, json, re
from rich import print
from rich.console import Console
from rich.panel import Panel


console = Console()

def show_banner():
    console.print(Panel.fit(
        "[bold blue]Instagram Public Profile Data Scraper[/bold blue]\n"
        "[green]Exact Followers Count - No Rounding[/green]\n"
        "Created by Walid Elfeky",
        border_style="bright_blue"
    ))


def profile_data():
    """
    Fetches and prints Instagram profile data from a username or profile URL.
    """
    show_banner()
    url = input("Enter your username or account link: ")
    # get username from link or username
    match = re.search(r'instagram\.com/([A-Za-z0-9._]+)', url)
    if match:
        username = match.group(1)
    else:
        username = url

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'priority': 'u=1, i',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-full-version-list': '"Not(A:Brand";v="8.0.0.0", "Chromium";v="144.0.7559.110", "Google Chrome";v="144.0.7559.110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"19.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        'x-asbd-id': '359341',
        'x-fb-friendly-name': 'PolarisProfilePageContentQuery',
        'x-fb-lsd': 'AdSTDkUAbspS2Jnabqqu6CAEEzA',
        'x-root-field-name': 'fetch__XDTUserDict',
    }

    # create session
    session = requests.Session()
    ress = session.get(f"https://www.instagram.com/{url}", headers=headers)
    cookie = ress.cookies.get_dict()
    headers['x-csrftoken'] = cookie.get('csrftoken')

    # get user id
    match = re.search(r'"props":\s*{[^}]*"id":\s*"(\d+)"', ress.text)
    if match:
        user_id = match.group(1)
    else:
        print("id not found")
        exit()

    variables_dict = {
        "enable_integrity_filters": True,
        "id": user_id,
        "render_surface": "PROFILE",
        "__relay_internal__pv__PolarisCannesGuardianExperienceEnabledrelayprovider": True,
        "__relay_internal__pv__PolarisCASB976ProfileEnabledrelayprovider": False,
        "__relay_internal__pv__PolarisRepostsConsumptionEnabledrelayprovider": False
    }

    data = {
        'av': '0',
        '__d': 'www',
        '__user': '0',
        '__a': '1',
        '__req': '1',
        '__hs': '20488.HYP:instagram_web_pkg.2.1...0',
        'dpr': '1',
        '__ccg': 'GOOD',
        '__rev': '1032903352',
        '__s': 'g5y5b8:7dwnb3:it63og',
        '__hsi': '7602988767555643171',
        '__dyn': '7xe5WwlEnwn8K2Wmh0no6u5U4e1ZyUW3qi2K360O81nEhw2nVE4W0qa0FE2awgo9o1vohwGwQwoEcE2ygao1aU2swlo6qU2zxe2GewGw9a361qw8W5U4q08OwLyES1Twoob82ZwrUdUbE5N0bK1Iwqo5p0qZ6goK10xKi2K7E5y4U158KmUhw4rwhEcE2Qw',
        '__csr': 'jNcdM87ezjqbhhbdlIgyIQWAV39CAWhpdrGmJ5Djzah_G8J6LGmhrYGVqhHFVFvAByFQqF26DDyKEy9J9oXBUmxaEVa9XheUyfCGmKWzF98zjDxivVemiqimVS5eQmm-498y4USmjyVqVm9Ku8gkBC_UlKu54bUiyuipeHWDxfBx6qi4UKu8KnLy44E-axicxu2i00n7mq4UG2i1swKwf20jm0IA0Jo4204LoK1Oy8B7_AUW1tCw2rEx2U0kKAw15jw4rwaalwahwbUE7W6okxi2FoaVkao2kQ4EV7S0AC0ki1JN05m0vKtm4E9mq12xqIE0Q27Nkg6o9ogAxN0mEm5m03kG025a010iw0Auw7pU1X81XU',
        '__hsdp': 'lmxREa4ImR9u8LBh2A60BwNSDFuJF2v8pfiteh5hmphj8npC2u222snXO8K58eo3Zwl8bo25wlIm5e8CDxu226UC0JU1LolDw2houw0AlwbC0UFU1lU3cw3vA0m60LE3cwio',
        '__hblp': '0dO1dwtonwywqU39wOxu3umfxuGzU611O1IKiWyWCzosK4VUC261HDx6fxGmi5qyKfDxKdyUC5EuyUoxZ5Axebx-2mhzGyoB1inBBxm0TA8xd0wyo-m2Gi1Lwh9ooAwOwXwaa2u0gi0lu0VE1gU1BE5y3Z0Uyolxy1AwIxC0wouDx23m3h0oE3tw9m0P86y090xPwbl0Kxu19wd218wzyQ2HBgGm6oqDxiezEQw4K543e7o2Qxq',
        '__sjsp': 'lmxREa4ImR9u8LBh2A60BwNSDFuJF2v8pfiuih5CpB5cxtCo9U889NvL8yUkw2BYm5e',
        '__comet_req': '7',
        'lsd': 'AdSTDkUAbspS2Jnabqqu6CAEEzA',
        'jazoest': '22348',
        '__spin_r': '1032903352',
        '__spin_b': 'trunk',
        '__spin_t': '1770208768',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'PolarisProfilePageContentQuery',
        'server_timestamps': 'true',
        'doc_id': '26762473490008061',
        "variables": json.dumps(variables_dict)
    }

    session.headers.update(headers)

    try:
        response = session.post('https://www.instagram.com/graphql/query', data=data)

        user = response.json()['data']['user']

        print("Username:", user['username'])
        print("Full Name:", user['full_name'])
        print("Verified:", user['is_verified'])
        print("Private Account:", user['is_private'])
        print("Followers:", user['follower_count'])
        print("Following:", user['following_count'])
        print("Posts:", user.get('media_count', 'N/A'))
        print("Total Clips:", user.get('total_clips_count', 'N/A'))
        print("Biography:", user.get('biography', ''))
        print("Professional Account:", user.get('is_professional_account', False))
        print("Account Type:", user['account_type'])
        print("Business Account:", user['is_business'])
        print("ID:", user['id'])
        print("Profile Picture URL:", user['profile_pic_url'])
    except Exception as Ex:
        print("An error occurred; please verify your username or your IP address may have been blocked.")

profile_data()