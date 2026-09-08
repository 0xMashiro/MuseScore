"""Inspect saved page-lock endpoints in the supplied desktop evidence."""
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET


def inspect(file_path):
    with ZipFile(file_path) as archive:
        score = ET.fromstring(archive.read(next(name for name in archive.namelist() if name.endswith(".mscx"))))
        style = ET.fromstring(archive.read("score_style.mss"))
    ids = {element.text for element in score.iter("eid")}
    locks = score.findall(".//pageLock")
    missing = [endpoint.text for lock in locks for endpoint in lock if endpoint.text not in ids]
    return style.findtext(".//createMultiMeasureRests"), len(locks), missing


if __name__ == "__main__":
    for file_path in sorted(Path(__file__).parent.glob("*.mscz")):
        print(file_path.name, inspect(file_path))
