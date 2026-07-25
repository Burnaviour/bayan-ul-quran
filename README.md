# ☪ Bayan-ul-Quran (Dr. Israr Ahmad) — Web App & Downloader

> Complete 108-Episode Video Player Web Application and Python Downloader CLI tool for the **Bayan-ul-Quran** Quranic Tafseer series by **Dr. Israr Ahmad**.

![Bayan-ul-Quran UI](https://img.shields.io/badge/Episodes-108%20Complete-10b981?style=for-the-badge)
![Surahs](https://img.shields.io/badge/Surahs-All%20114%20Mapped-f59e0b?style=for-the-badge)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Ready-059669?style=for-the-badge)
![Official Source](https://img.shields.io/badge/Official%20Site-drisrar.com-10b981?style=for-the-badge)

---

## 🌐 Live Web Application & Official Reference

- **🚀 Live Web Player (GitHub Pages)**: [https://burnaviour.github.io/bayan-ul-quran/](https://burnaviour.github.io/bayan-ul-quran/)
- **🏛️ Official Source & Reference Portal**: [https://www.drisrar.com](https://www.drisrar.com) *(Tanzeem-e-Islami Official Portal)*

---

## 🌟 Web Application Features

- **🌐 Single-Page GitHub Pages Compatible**: Pure HTML, CSS, and JS web app — zero build steps required!
- **⚡ Smart Search Engine**: Real-time instant filtering across episode titles, all 114 Surah names, Ayah ranges, or episode numbers.
- **📖 Complete 114 Surah Index Dropdown**: Jump directly to any Surah from `1. Surah Al-Fatiha` to `114. Surah An-Nas`.
- **✨ Next Video Recommendation Engine**:
  - **"Up Next" Hero Card**: Visual preview of the next episode in sequence.
  - **Surah-Related Parts Grid**: Smart recommendations showcasing remaining parts of the current Surah or adjacent Surahs.
- **↺ Progress Memory ("Continue Watching")**: Automatically saves your last played episode and watched status in `localStorage`.
- **🎨 Modern Dark Islamic Aesthetics**: High-contrast dark green & gold palette with responsive layout for desktop, tablet, and mobile devices.

---

## 📥 Python Downloader CLI (`download_bayan.py`)

The repository includes a Python CLI utility script `download_bayan.py` to download high-definition video or MP3 audio files directly to your computer.

### Prerequisites

```bash
pip install yt-dlp
```

### Usage Examples

1. **Download by Surah Name or Number**:
   ```bash
   python download_bayan.py --surah Baqarah
   python download_bayan.py --surah Kahf
   python download_bayan.py --surah 114
   ```

2. **Download Episode Ranges (e.g. Episodes 1 to 10)**:
   ```bash
   python download_bayan.py --start 1 --end 10
   ```

3. **Download Audio Only (MP3)**:
   ```bash
   python download_bayan.py --surah Fatiha --audio-only
   ```

4. **List All 114 Surahs & Part Mappings**:
   ```bash
   python download_bayan.py --list-surahs
   ```

5. **Download Entire 108 Episodes Series**:
   ```bash
   python download_bayan.py --all
   ```

---

## 🏷️ Search & Topic Tags

`bayan-ul-quran`, `dr-israr-ahmad`, `quran-tafseer`, `quran`, `islamic-lectures`, `tanzeem-e-islami`, `video-player`, `python-downloader`, `drisrar.com`, `surah-index`, `urdu-tafseer`, `quran-study`, `yt-dlp`

---

## 📜 License & Acknowledgments

This project is created for educational and community benefit. All lectures, video recordings, and Tafseer content belong to **Dr. Israr Ahmad (Tanzeem-e-Islami)**. Official website: [https://www.drisrar.com](https://www.drisrar.com).
