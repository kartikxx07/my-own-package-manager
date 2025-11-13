def install_package():  
    downloads_dir = "/Users/kartikayluthra/Desktop/own-package-manager/downloads"
    install_dir = "/Users/kartikayluthra/Library/Mobile Documents/com~apple~CloudDocs"

    for file in os.listdir(downloads_dir):
        file_path = os.path.join(downloads_dir, file)

        if verifyhash(file_path):
            target_path = os.path.join(install_dir, file)
            os.makedirs(target_path, exist_ok=True)
            
            if file.endswith(".whl"):
                with zipfile.ZipFile(file_path, "r") as zf:
                    zf.extractall(target_path)

            print(f"✅ {file} installed successfully at {target_path}")
