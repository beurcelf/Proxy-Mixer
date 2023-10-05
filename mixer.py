import requests

# Replace the following list with your own proxy subscription links
proxy_links = [
    "https://yebekhe.link/api/toClash/?url=https%3A%2F%2Fraw.githubusercontent.com%2Fyebekhe%2FTelegramV2rayCollector%2Fmain%2Fsub%2Fbase64%2Fmix&type=meta&process=full",
    "https://raw.githubusercontent.com/SnapdragonLee/SystemProxy/master/dist/clash_config_extra_US.yaml",
    "https://raw.githubusercontent.com/tbbatbb/Proxy/master/dist/clash.config.yaml"
]

# Initialize an empty list to store the proxies
proxies = []

# Loop through each proxy link and extract the proxies
for link in proxy_links:
    response = requests.get(link)
    proxies.extend(response.text.strip().split("\n"))

# Print the mixed proxies
print("\n".join(proxies))
