import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
zip_path = root / "data" / "Point cloud LIDAR (Toronto 3D).zip"
extract_path = root / "data" / "LIDAR data"

extract_path.mkdir(parents=True, exist_ok=True)

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)
