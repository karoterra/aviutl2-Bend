# /// script
# requires-python = ">=3.13"
# ///

from pathlib import Path
import shutil


def insert_param(text: str, key: str, value: str) -> str:
    return text.replace(f"${{{key}}}", value)


def insert_dictionary(text: str, dictionary: dict) -> str:
    for key, value in dictionary.items():
        text = insert_param(text, key, value)
    return text


def main():
    AUTHOR = "karoterra"
    VERSION = "v1.0.0"

    build_dir = Path("build")
    build_dir.mkdir(exist_ok=True)

    script_texts = []
    with open("script/@曲げKR.in.anm2", "r", encoding="utf-8") as f:
        text = f.read()
        text = insert_dictionary(text, {
            "INFO": "曲げKR for AviUtl2",
            "VERSION": VERSION,
            "AUTHOR": AUTHOR
        })
        script_texts.append(text)
    with open("script/@曲げKR_円弧.in.anm2", "r", encoding="utf-8") as f:
        text = f.read()
        text = insert_dictionary(text, {
            "INFO": "曲げKR (円弧) for AviUtl2",
            "VERSION": VERSION,
            "AUTHOR": AUTHOR
        })
        script_texts.append("@円弧")
        script_texts.append(text)
    with open("script/@曲げKR_ベジェ曲線.in.anm2", "r", encoding="utf-8") as f:
        text = f.read()
        text = insert_dictionary(text, {
            "INFO": "曲げKR (ベジェ曲線) for AviUtl2",
            "VERSION": VERSION,
            "AUTHOR": AUTHOR
        })
        script_texts.append("@ベジェ曲線")
        script_texts.append(text)

    with open("build/@曲げKR.anm2", "w", encoding="utf-8", newline="\r\n") as f:
        f.write("\n".join(script_texts))

    shutil.copy("script/KaroterraBend.lua", build_dir / "KaroterraBend.lua")


if __name__ == "__main__":
    main()
