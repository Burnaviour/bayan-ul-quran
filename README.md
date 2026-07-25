# ☪ Bayan-ul-Quran (Dr. Israr Ahmad) — Web App & Downloader

> Complete 108-Episode Video Player Web Application and Python Downloader CLI tool for the **Bayan-ul-Quran** Quranic Tafseer series by **Dr. Israr Ahmad**.

![Bayan-ul-Quran UI](https://img.shields.io/badge/Episodes-108%20Complete-10b981?style=for-the-badge)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Ready-f59e0b?style=for-the-badge)
![Python Downloader](https://img.shields.io/badge/CLI-Python%20%2B%20yt--dlp-059669?style=for-the-badge)

---

## 🌟 Web Application Features

- **🌐 Single-Page GitHub Pages Compatible**: Pure HTML, CSS, and JS web app — zero build steps required!
- **⚡ Smart Search Engine**: Real-time instant filtering across episode titles, Surah names, Ayah ranges, or episode numbers.
- **📖 Complete Surah Index Dropdown**: Jump directly to any of the 114 Surahs / 63 Surah groups across the 108 episodes.
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

1. **Download by Surah Name**:
   ```bash
   python download_bayan.py --surah Baqarah
   python download_bayan.py --surah Kahf
   python download_bayan.py --surah Yasin
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

## 🚀 How to Host on GitHub Pages

1. Go to your repository settings on GitHub (`Settings` tab).
2. Navigate to **Pages** (under Code and automation).
3. Under **Build and deployment**:
   - **Source**: Select `Deploy from a branch`.
   - **Branch**: Select `main` / `root`.
4. Click **Save**. Your site will be published at: `https://<your-username>.github.io/bayan-ul-quran/`

---

## 📂 Project Structure

```
bayan-ul-quran/
├── index.html            # Main Single-Page Web Application
├── download_bayan.py     # Python CLI Downloader Tool
├── episodes.json         # Structured dataset of all 108 episodes
├── .gitignore            # Git ignore configuration
└── README.md             # Project documentation
```

---

## 📜 License & Acknowledgments

This project is created for educational and community benefit. All lectures and Tafseer recordings belong to **Dr. Israr Ahmad (Tanzeem-e-Islami)**.
