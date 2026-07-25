import json
import argparse
import os
import subprocess
import sys

# Ensure UTF-8 output encoding for Windows terminal
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Complete List of all 114 Surahs of the Holy Quran
ALL_114_SURAHS = [
    {"number": 1, "name": "Surah Al-Fatiha", "parts": [5]},
    {"number": 2, "name": "Surah Al-Baqarah", "parts": list(range(6, 16))},
    {"number": 3, "name": "Surah Aal-E-Imran", "parts": list(range(16, 21))},
    {"number": 4, "name": "Surah An-Nisa", "parts": list(range(21, 27))},
    {"number": 5, "name": "Surah Al-Ma'idah", "parts": list(range(27, 32))},
    {"number": 6, "name": "Surah Al-An'am", "parts": list(range(32, 37))},
    {"number": 7, "name": "Surah Al-A'raf", "parts": list(range(37, 41))},
    {"number": 8, "name": "Surah Al-Anfal", "parts": list(range(41, 43))},
    {"number": 9, "name": "Surah At-Tawbah", "parts": [43, 44, 45]},
    {"number": 10, "name": "Surah Yunus", "parts": [45]},
    {"number": 11, "name": "Surah Hud", "parts": [45, 46]},
    {"number": 12, "name": "Surah Yusuf", "parts": [46, 47]},
    {"number": 13, "name": "Surah Ar-Ra'd", "parts": [47]},
    {"number": 14, "name": "Surah Ibrahim", "parts": [47, 48]},
    {"number": 15, "name": "Surah Al-Hijr", "parts": [48, 49]},
    {"number": 16, "name": "Surah An-Nahl", "parts": [50, 51]},
    {"number": 17, "name": "Surah Al-Isra / Bani-Israeel", "parts": [52, 53, 54]},
    {"number": 18, "name": "Surah Al-Kahf", "parts": [54, 55, 56]},
    {"number": 19, "name": "Surah Maryam", "parts": [56, 57]},
    {"number": 20, "name": "Surah Taha", "parts": [57, 58]},
    {"number": 21, "name": "Surah Al-Anbiya", "parts": [58, 59, 60]},
    {"number": 22, "name": "Surah Al-Hajj", "parts": [60, 61]},
    {"number": 23, "name": "Surah Al-Mu'minun", "parts": [62, 63]},
    {"number": 24, "name": "Surah An-Nur", "parts": [63, 64]},
    {"number": 25, "name": "Surah Al-Furqan", "parts": [64, 65]},
    {"number": 26, "name": "Surah Ash-Shu'ara", "parts": [65, 66]},
    {"number": 27, "name": "Surah An-Naml", "parts": [66, 67]},
    {"number": 28, "name": "Surah Al-Qasas", "parts": [67, 68, 69]},
    {"number": 29, "name": "Surah Al-Ankabut", "parts": [69, 70]},
    {"number": 30, "name": "Surah Ar-Rum", "parts": [70, 71]},
    {"number": 31, "name": "Surah Luqman", "parts": [71, 72]},
    {"number": 32, "name": "Surah As-Sajdah", "parts": [72]},
    {"number": 33, "name": "Surah Al-Ahzab", "parts": [72, 73, 74]},
    {"number": 34, "name": "Surah Saba", "parts": [74, 75]},
    {"number": 35, "name": "Surah Fatir", "parts": [75, 76]},
    {"number": 36, "name": "Surah Ya-Sin", "parts": [76]},
    {"number": 37, "name": "Surah As-Saffat", "parts": [77]},
    {"number": 38, "name": "Surah Sad", "parts": [77]},
    {"number": 39, "name": "Surah Az-Zumar", "parts": [78, 79, 80]},
    {"number": 40, "name": "Surah Ghafir / Al-Mu'min", "parts": [80, 81]},
    {"number": 41, "name": "Surah Fussilat", "parts": [81]},
    {"number": 42, "name": "Surah Ash-Shura", "parts": [82, 83]},
    {"number": 43, "name": "Surah Az-Zukhruf", "parts": [83]},
    {"number": 44, "name": "Surah Ad-Dukhan", "parts": [84]},
    {"number": 45, "name": "Surah Al-Jathiyah", "parts": [84]},
    {"number": 46, "name": "Surah Al-Ahqaf", "parts": [85]},
    {"number": 47, "name": "Surah Muhammad", "parts": [85]},
    {"number": 48, "name": "Surah Al-Fath", "parts": [86, 87]},
    {"number": 49, "name": "Surah Al-Hujurat", "parts": [87]},
    {"number": 50, "name": "Surah Qaf", "parts": [88]},
    {"number": 51, "name": "Surah Az-Zariyat", "parts": [88]},
    {"number": 52, "name": "Surah At-Tur", "parts": [89]},
    {"number": 53, "name": "Surah An-Najm", "parts": [90]},
    {"number": 54, "name": "Surah Al-Qamar", "parts": [90]},
    {"number": 55, "name": "Surah Ar-Rahman", "parts": [90]},
    {"number": 56, "name": "Surah Al-Waqi'ah", "parts": [91]},
    {"number": 57, "name": "Surah Al-Hadid", "parts": [92]},
    {"number": 58, "name": "Surah Al-Mujadila", "parts": [93]},
    {"number": 59, "name": "Surah Al-Hashr", "parts": [94]},
    {"number": 60, "name": "Surah Al-Mumtahanah", "parts": [95]},
    {"number": 61, "name": "Surah As-Saff", "parts": [95]},
    {"number": 62, "name": "Surah Al-Jumu'ah", "parts": [96]},
    {"number": 63, "name": "Surah Al-Munafiqun", "parts": [97]},
    {"number": 64, "name": "Surah At-Taghabun", "parts": [97]},
    {"number": 65, "name": "Surah At-Talaq", "parts": [98]},
    {"number": 66, "name": "Surah At-Tahrim", "parts": [98]},
    {"number": 67, "name": "Surah Al-Mulk", "parts": [98]},
    {"number": 68, "name": "Surah Al-Qalam", "parts": [99]},
    {"number": 69, "name": "Surah Al-Haqqah", "parts": [99]},
    {"number": 70, "name": "Surah Al-Ma'arij", "parts": [100]},
    {"number": 71, "name": "Surah Nuh", "parts": [100]},
    {"number": 72, "name": "Surah Al-Jinn", "parts": [100]},
    {"number": 73, "name": "Surah Al-Muzzammil", "parts": [100]},
    {"number": 74, "name": "Surah Al-Muddaththir", "parts": [101]},
    {"number": 75, "name": "Surah Al-Qiyamah", "parts": [101]},
    {"number": 76, "name": "Surah Al-Insan", "parts": [102]},
    {"number": 77, "name": "Surah Al-Mursalat", "parts": [102]},
    {"number": 78, "name": "Surah An-Naba", "parts": [103]},
    {"number": 79, "name": "Surah An-Nazi'at", "parts": [103]},
    {"number": 80, "name": "Surah 'Abasa", "parts": [103]},
    {"number": 81, "name": "Surah At-Takwir", "parts": [103]},
    {"number": 82, "name": "Surah Al-Infitar", "parts": [103]},
    {"number": 83, "name": "Surah Al-Mutaffifin", "parts": [104]},
    {"number": 84, "name": "Surah Al-Inshiqaq", "parts": [104]},
    {"number": 85, "name": "Surah Al-Buruj", "parts": [104]},
    {"number": 86, "name": "Surah At-Tariq", "parts": [104]},
    {"number": 87, "name": "Surah Al-A'la", "parts": [104]},
    {"number": 88, "name": "Surah Al-Ghashiyah", "parts": [104]},
    {"number": 89, "name": "Surah Al-Fajr", "parts": [104]},
    {"number": 90, "name": "Surah Al-Balad", "parts": [105]},
    {"number": 91, "name": "Surah Ash-Shams", "parts": [105]},
    {"number": 92, "name": "Surah Al-Layl", "parts": [105]},
    {"number": 93, "name": "Surah Ad-Duha", "parts": [105]},
    {"number": 94, "name": "Surah Ash-Sharh", "parts": [105]},
    {"number": 95, "name": "Surah At-Tin", "parts": [105]},
    {"number": 96, "name": "Surah Al-'Alaq", "parts": [105]},
    {"number": 97, "name": "Surah Al-Qadr", "parts": [105]},
    {"number": 98, "name": "Surah Al-Bayyinah", "parts": [105]},
    {"number": 99, "name": "Surah Az-Zalzalah", "parts": [105]},
    {"number": 100, "name": "Surah Al-'Adiyat", "parts": [105]},
    {"number": 101, "name": "Surah Al-Qari'ah", "parts": [106]},
    {"number": 102, "name": "Surah At-Takathur", "parts": [106]},
    {"number": 103, "name": "Surah Al-'Asr", "parts": [106]},
    {"number": 104, "name": "Surah Al-Humazah", "parts": [106]},
    {"number": 105, "name": "Surah Al-Fil", "parts": [107]},
    {"number": 106, "name": "Surah Quraysh", "parts": [107]},
    {"number": 107, "name": "Surah Al-Ma'un", "parts": [107]},
    {"number": 108, "name": "Surah Al-Kawthar", "parts": [107]},
    {"number": 109, "name": "Surah Al-Kafirun", "parts": [107]},
    {"number": 110, "name": "Surah An-Nasr", "parts": [107]},
    {"number": 111, "name": "Surah Al-Masad", "parts": [108]},
    {"number": 112, "name": "Surah Al-Ikhlas", "parts": [108]},
    {"number": 113, "name": "Surah Al-Falaq", "parts": [108]},
    {"number": 114, "name": "Surah An-Nas", "parts": [108]},
]

def main():
    parser = argparse.ArgumentParser(description="Download Bayan-ul-Quran Series (Dr. Israr Ahmad) - All 114 Surahs Mapped")
    parser.add_argument("--surah", type=str, help="Name or number of Surah (e.g. Baqarah, Fatiha, Kahf, Mulk, 114)")
    parser.add_argument("--start", type=int, help="Start episode number (1-108)")
    parser.add_argument("--end", type=int, help="End episode number (1-108)")
    parser.add_argument("--all", action="store_true", help="Download all 108 episodes")
    parser.add_argument("--output-dir", type=str, default="Bayan_ul_Quran_Downloads", help="Directory to save downloads")
    parser.add_argument("--audio-only", action="store_true", help="Download MP3 audio only")
    parser.add_argument("--list-surahs", action="store_true", help="List all 114 Surahs and their part numbers")

    args = parser.parse_args()

    if args.list_surahs:
        print("\n=== BAYAN-UL-QURAN: ALL 114 SURAHS INDEX ===")
        for s in ALL_114_SURAHS:
            parts_str = ", ".join(f"Part {p}" for p in s["parts"])
            print(f" {s['number']:>3}. {s['name']:<38} -> {parts_str}")
        return

    json_file = "episodes.json"
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found.")
        return

    with open(json_file, "r", encoding="utf-8") as f:
        episodes = json.load(f)

    target_parts = set()

    if args.surah:
        query = args.surah.lower().strip()
        matched_surahs = []
        for s in ALL_114_SURAHS:
            if query in s["name"].lower() or query == str(s["number"]):
                matched_surahs.append(s)
                target_parts.update(s["parts"])
        
        # Also check episode titles directly
        for ep in episodes:
            if query in ep["title"].lower():
                target_parts.add(ep["episode"])

        if matched_surahs:
            print(f"\n[+] Found Surah match for '{args.surah}':")
            for ms in matched_surahs:
                print(f"   • Surah {ms['number']}. {ms['name']} -> Parts {ms['parts']}")
        elif target_parts:
            print(f"\n[+] Found title matches for '{args.surah}': Parts {sorted(target_parts)}")
        else:
            print(f"[-] No Surah or episode found matching '{args.surah}'.")
            print("Run with --list-surahs to see all 114 available Surahs.")
            return

    elif args.start or args.end:
        start_ep = args.start if args.start else 1
        end_ep = args.end if args.end else 108
        target_parts = set(range(start_ep, end_ep + 1))
    elif args.all:
        target_parts = set(range(1, 109))
    else:
        print("💡 Usage examples:")
        print("   python download_bayan.py --surah Baqarah        (Download Surah Al-Baqarah Parts 6 to 15)")
        print("   python download_bayan.py --surah 114            (Download Surah An-Nas Part 108)")
        print("   python download_bayan.py --surah Mulk           (Download Surah Al-Mulk Part 98)")
        print("   python download_bayan.py --start 1 --end 10     (Download Parts 1 to 10)")
        print("   python download_bayan.py --list-surahs          (Show all 114 Surahs index)")
        return

    selected_episodes = [ep for ep in episodes if ep["episode"] in target_parts]
    selected_episodes.sort(key=lambda x: x["episode"])

    print(f"\n[+] Selected {len(selected_episodes)} episodes: Parts {[e['episode'] for e in selected_episodes]}\n")

    os.makedirs(args.output_dir, exist_ok=True)

    try:
        subprocess.run(["yt-dlp", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        has_ytdlp = True
    except Exception:
        has_ytdlp = False
        print("💡 Tip: Install 'yt-dlp' via `pip install yt-dlp` for maximum download speeds.\n")

    for ep in selected_episodes:
        ep_num = ep['episode']
        title = ep['title']
        link = ep.get('embed_url') or ep['link']

        print(f"==================================================")
        print(f"Downloading Part {ep_num}/108: {title}")
        print(f"Link: {link}")
        print(f"==================================================")

        if has_ytdlp:
            out_template = os.path.join(args.output_dir, f"Part_{ep_num:03d}_%(title)s.%(ext)s")
            cmd = ["yt-dlp", link, "-o", out_template]
            if args.audio_only:
                cmd.extend(["-x", "--audio-format", "mp3"])
            try:
                subprocess.run(cmd, check=True)
            except subprocess.CalledProcessError as e:
                print(f"[-] Failed to download Part {ep_num} with yt-dlp: {e}")
        else:
            print(f"Direct web page for Part {ep_num}: {ep['link']}")

if __name__ == "__main__":
    main()
