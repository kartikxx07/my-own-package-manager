from resolver import resolve_dependencies
from installer import install_package, remove_package
from fetcher import fetch_metadata, dowload_package
from utils import print_info, print_error
import argparse

def main():
    parser = argparse.Argumentparser(prog = "my_project", description = "my own package manager")
    parser.add_argument("command", choices = ["install", "remove", "seeAll"])
    parser.add_argument("package", nargs="?", help="Package name")
    args = parser.parse_args()

    if(args.command = "install"):
        deps = resolve_dependencies(args.package)
        for dep in deps:
            metadata = fetch_metadata(dep)
            file = download_package(metadata)
            install_package(file)

    if(args.command = "remove"):
        remove_package(args.package)
        print("Removing....")
    