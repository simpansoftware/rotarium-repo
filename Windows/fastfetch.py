import zipfile
import io

r = requests.get("https://github.com/fastfetch-cli/fastfetch/releases/download/2.61.0/fastfetch-windows-amd64.zip")

with zipfile.ZipFile(io.BytesIO(r.content)) as z:
    z.extractall("packages/windows/fastfetch")

register_package("fastfetch", "packages/windows/fastfetch/fastfetch.exe", "packages/windows/fastfetch")
