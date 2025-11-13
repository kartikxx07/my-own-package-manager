from fetcher import fetch_metadata, download_package
import hashlib

def verify_hash(file_path, expected_sha256):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    computed_hash = sha256_hash.hexdigest()
    return computed_hash == expected_sha256


def prepare_and_verify(package_name):
    metadata = fetch_metadata(package_name)
    if not metadata:
        print("Failed to fetch metadata.")
        return False

    file_path = download_package(metadata["url"])
    if verify_hash(file_path, metadata["sha256"]):
        print("Hash verified successfully!")
        return True
    else:
        print("Hash verification failed.")
        return False
