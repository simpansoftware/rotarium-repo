import zipfile
import io

r = requests.get("https://github.com/fastfetch-cli/fastfetch/releases/download/2.61.0/fastfetch-linux-amd64.zip")

with zipfile.ZipFile(io.BytesIO(r.content)) as z:
    z.extractall("packages/linux/fastfetch")

register_package("fastfetch", "packages/linux/fastfetch/usr/bin/fastfetch")
