import zipfile
import io
import os

r = requests.get("https://github.com/fastfetch-cli/fastfetch/releases/download/2.61.0/fastfetch-linux-amd64.zip")

with zipfile.ZipFile(io.BytesIO(r.content)) as z:
    z.extractall("packages/linux/fastfetch")

os.chmod("packages/linux/fastfetch/fastfetch-linux-amd64/usr/bin/fastfetch", 0o755)
register_package("fastfetch", "packages/linux/fastfetch/fastfetch-linux-amd64/usr/bin/fastfetch", "packages/linux/fastfetch")
