import requests

def resolve_dependencies(package_name, resolved=None, seen=None):
    """
    Recursively resolve all dependencies for a given package.
    Returns a list of package names in install order.
    """

    if resolved is None:
        resolved = []
    if seen is None:
        seen = set()
    if package_name in seen:
        return resolved
    seen.add(package_name)

    url = f"https://pypi.org/pypi/{package_name}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching metadata for {package_name}: {e}")
        return resolved

    info = data.get("info", {})
    requires_dist = info.get("requires_dist", [])
    dependencies = []
    for dep in requires_dist:
        dep_name = dep.split(" ")[0]
        dependencies.append(dep_name)

    for dep_name in dependencies:
        resolve_dependencies(dep_name, resolved, seen)

    if package_name not in resolved:
        resolved.append(package_name)

    return resolved
