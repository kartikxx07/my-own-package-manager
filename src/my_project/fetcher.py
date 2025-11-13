import requests
import os

def fetch_metadata(package_name):
    res = {}
    url = f"https://pypi.org/pypi/{package_name}/json"
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    releases_dict = data.get('releases', {})
    if not releases_dict:
        print("No releases found for package.")
        return None

    last_release = list(releases_dict.keys())[-1]
    latest_release_info = releases_dict[last_release]

    for release_file in latest_release_info:
        if not isinstance(release_file, dict):
            continue

        download_url = release_file.get("url")
        python_version = release_file.get("python_version")
        requires_python = release_file.get("requires_python")
        digests = release_file.get("digests", {})

        sha256 = digests.get("sha256")

        if download_url and sha256:
            res["version"]: last_release
            res["url"] : download_url
            res["sha256"] : sha256
            res["python_version"] : python_version
            res["resquires_python"] : requires_python

    print("No valid file with SHA256 digest found.")
    return res



 def download_package(url):
    download_dir = "/Users/kartikayluthra/Desktop/own-package-manager/downloads"
    filename = url.split("/")[-1] 
    file_path = os.path.join(download_dir, filename)

    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

    return file_path







