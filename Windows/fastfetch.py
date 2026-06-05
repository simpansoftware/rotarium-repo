import zipfile
import io

r = requests.get("https://simpansoftware.cc/rotarium-repo/Windows/fastfetch-windows-amd64.zip")

with zipfile.ZipFile(io.BytesIO(r.content)) as z:
    z.extractall("packages/windows/fastfetch")

register_package("fastfetch", "packages/windows/fastfetch/fastfetch.exe", "packages/windows/fastfetch")
