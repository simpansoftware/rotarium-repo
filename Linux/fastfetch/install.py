import zipfile
import io
import os

r = requests.get("https://simpansoftware.cc/rotarium-repo/Linux/fastfetch/fastfetch-linux-amd64.zip")

with zipfile.ZipFile(io.BytesIO(r.content)) as z:
    z.extractall("packages/linux/fastfetch")

os.chmod("packages/linux/fastfetch/fastfetch-linux-amd64/usr/bin/fastfetch", 0o755)
register_package("fastfetch", "packages/linux/fastfetch/fastfetch-linux-amd64/usr/bin/fastfetch", manifest["version"], manifest["info"], "packages/linux/fastfetch")
