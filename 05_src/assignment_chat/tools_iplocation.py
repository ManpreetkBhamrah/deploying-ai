import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv(".env")
load_dotenv(".secrets")

IPSTACK_API_KEY = os.getenv("IP_STACK_KEY")


def get_ipstack_from_service(ip: str):
    """
    Calls the IPStack API with the provided IP address and returns the raw response.
    """
    url = f"http://api.ipstack.com/{ip}"
    params = {"access_key": IPSTACK_API_KEY}
    response = requests.get(url, params=params)
    return response


def get_ipstack_from_response(ip: str, response: requests.Response) -> dict:
    """
    Extracts and formats the IPStack API response.
    """
    if response.status_code == 200:
        data = response.json()
        return {
            "ip": ip,
            "city": data.get("city"),
            "region": data.get("region_name"),
            "country": data.get("country_name"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
        }
    else:
        return {
            "ip": ip,
            "error": f"Failed to retrieve location. Status code: {response.status_code}",
        }


def get_ipstack_location(ip: str) -> dict:
    """
    Calls IPStack API and returns structured ip information.
    """
    response = get_ipstack_from_service(ip)
    return get_ipstack_from_response(ip, response)


@tool
def ipstack_chat(ip: str) -> dict:
    """
    Returns location information for the given IP address.
    """
    return get_ipstack_location(ip)

