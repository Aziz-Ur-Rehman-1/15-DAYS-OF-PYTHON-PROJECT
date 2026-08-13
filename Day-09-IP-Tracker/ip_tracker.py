import requests

BASE_URL = "http://ip-api.com/json/"

def get_ip_info(ip_or_domain=""):
    try:
        # http://ip-api.com/json/{ip_or_domain}
        response = requests.get(f"{BASE_URL}{ip_or_domain}", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                return data
            else:
                print(f"\nError: {data.get('message', 'Invalid IP or Domain')}\n")
                return None
        else:
            print(f"\nHTTP Error: Received status code {response.status_code}\n")
            return None
    except Exception as e:
        print(f"\nNetwork Error: {e}\n")
        return None

def display_info(data):
    print("\n" + "="*50)
    print(" IP GEOLOCATION & NETWORK DETAILS")
    print("="*50)
    print(f" Target IP / Host : {data.get('query')}")
    print(f" Country          : {data.get('country')} ({data.get('countryCode')})")
    print(f" Region / State   : {data.get('regionName')}")
    print(f" City             : {data.get('city')}")
    print(f" ZIP / Postal Code: {data.get('zip') or 'N/A'}")
    print(f" Timezone         : {data.get('timezone')}")
    print(f" ISP              : {data.get('isp')}")
    print(f" Organization     : {data.get('org')}")
    print(f" Latitude / Long  : {data.get('lat')}, {data.get('lon')}")
    print("="*50 + "\n")

def main():
    while True:
        print("Select an Option:")
        print("1. Track My Own Public IP")
        print("2. Track Any Custom IP or Domain Name")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == "1":
            print("\nFetching your public IP details...")
            data = get_ip_info()
            if data:
                display_info(data)
        elif choice == "2":
            target = input("Enter IP Address or Domain (e.g. google.com or 8.8.8.8): ").strip()
            if not target:
                print("\nInput cannot be empty!\n")
                continue
            print(f"\nFetching network details for '{target}'...")
            data = get_ip_info(target)
            if data:
                display_info(data)
        elif choice == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()