import json
import argparse
import os
import subprocess
import re
import sys

# Ensure UTF-8 output encoding for Windows terminal
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

SURAH_INDEX = [
    {"name": "Introduction", "parts": [1, 2, 3, 4]},
    {"name": "Surah Al-Fatiha (Surah 1)", "parts": [5]},
    {"name": "Surah Al-Baqarah (Surah 2)", "parts": list(range(6, 16))},
    {"name": "Surah Aal-E-Imran (Surah 3)", "parts": list(range(16, 21))},
    {"name": "Surah An-Nisa (Surah 4)", "parts": list(range(21, 27))},
    {"name": "Surah Al-Ma'idah (Surah 5)", "parts": list(range(27, 32))},
    {"name": "Surah Al-An'am (Surah 6)", "parts": list(range(32, 37))},
    {"name": "Surah Al-A'raf (Surah 7)", "parts": list(range(37, 41))},
    {"name": "Surah Al-Anfal (Surah 8)", "parts": list(range(41, 43))},
    {"name": "Surah At-Tawbah (Surah 9)", "parts": list(range(43, 46))},
    {"name": "Surah Yunus (Surah 10)", "parts": [45]},
    {"name": "Surah Hud (Surah 11)", "parts": [45, 46]},
    {"name": "Surah Yusuf (Surah 12)", "parts": [46, 47]},
    {"name": "Surah Ibrahim (Surah 14)", "parts": [47, 48]},
    {"name": "Surah Al-Hijr (Surah 15)", "parts": [48, 49]},
    {"name": "Surah An-Nahl (Surah 16)", "parts": [50, 51]},
    {"name": "Surah Bani-Israeel / Al-Isra (Surah 17)", "parts": [52, 53, 54]},
    {"name": "Surah Al-Kahf (Surah 18)", "parts": [54, 55, 56]},
    {"name": "Surah Maryam (Surah 19)", "parts": [56, 57]},
    {"name": "Surah Taha (Surah 20)", "parts": [57, 58]},
    {"name": "Surah Al-Anbiya (Surah 21)", "parts": [58, 59, 60]},
    {"name": "Surah Al-Hajj (Surah 22)", "parts": [60, 61]},
    {"name": "Surah Al-Mu'minun (Surah 23)", "parts": [62, 63]},
    {"name": "Surah An-Nur (Surah 24)", "parts": [63, 64]},
    {"name": "Surah Al-Furqan (Surah 25)", "parts": [64, 65]},
    {"name": "Surah Ash-Shu'ara (Surah 26)", "parts": [65, 66]},
    {"name": "Surah An-Naml (Surah 27)", "parts": [66, 67]},
    {"name": "Surah Al-Qasas (Surah 28)", "parts": [67, 68, 69]},
    {"name": "Surah Al-Ankabut (Surah 29)", "parts": [69, 70]},
    {"name": "Surah Ar-Rum (Surah 30)", "parts": [70, 71]},
    {"name": "Surah Luqman (Surah 31)", "parts": [71, 72]},
    {"name": "Surah Al-Ahzab (Surah 33)", "parts": [72, 73, 74]},
    {"name": "Surah Saba (Surah 34)", "parts": [74, 75]},
    {"name": "Surah Fatir (Surah 35)", "parts": [75, 76]},
    {"name": "Surah Ya-Sin / As-Saffat (Surah 36-37)", "parts": [76, 77]},
    {"name": "Surah Sad / Az-Zumar (Surah 38-39)", "parts": [77, 78, 79, 80]},
    {"name": "Surah Ghafir / Al-Mu'min (Surah 40)", "parts": [80, 81]},
    {"name": "Surah Fussilat / Ash-Shura (Surah 41-42)", "parts": [81, 82, 83]},
    {"name": "Surah Az-Zukhruf / Ad-Dukhan (Surah 43-44)", "parts": [83, 84]},
    {"name": "Surah Al-Jathiyah / Al-Ahqaf (Surah 45-46)", "parts": [84, 85]},
    {"name": "Surah Muhammad / Al-Fath (Surah 47-48)", "parts": [85, 86, 87]},
    {"name": "Surah Al-Hujurat / Qaf (Surah 49-50)", "parts": [87, 88]},
    {"name": "Surah Az-Zariyat / At-Tur / An-Najm", "parts": [88, 89, 90]},
    {"name": "Surah Ar-Rahman / Al-Waqi'ah", "parts": [90, 91]},
    {"name": "Surah Al-Hadid / Al-Mujadila", "parts": [92, 93, 94]},
    {"name": "Surah Al-Hashr to Al-Jumu'ah", "parts": [94, 95, 96]},
    {"name": "Surah Al-Munafiqun to At-Tahrim", "parts": [97, 98]},
    {"name": "Surah Al-Mulk to Al-Muzzammil", "parts": [98, 99, 100]},
    {"name": "Surah Al-Muddaththir to Al-Mursalat", "parts": [101, 102]},
    {"name": "Juz 30 / Amma Para (Short Surahs)", "parts": list(range(103, 109))},
]

def main():
    parser = argparse.ArgumentParser(description="Download Bayan-ul-Quran Series (Dr. Israr Ahmad) - Surah-Wise or Episode-Wise")
    parser.add_argument("--surah", type=str, help="Name or keyword of Surah (e.g. Baqarah, Fatiha, Kahf, Yasin, 2)")
    parser.add_argument("--start", type=int, help="Start episode number (1-108)")
    parser.add_argument("--end", type=int, help="End episode number (1-108)")
    parser.add_argument("--all", action="store_true", help="Download all 108 episodes")
    parser.add_argument("--output-dir", type=str, default="Bayan_ul_Quran_Downloads", help="Directory to save downloads")
    parser.add_argument("--audio-only", action="store_true", help="Download MP3 audio only")
    parser.add_argument("--list-surahs", action="store_true", help="List all Surahs and their part numbers")

    args = parser.parse_args()

    if args.list_surahs:
        print("\n=== BAYAN-UL-QURAN SURAH INDEX ===")
        for s in SURAH_INDEX:
            parts_str = ", ".join(f"Part {p}" for p in s["parts"])
            print(f" • {s['name']:<42} -> {parts_str}")
        return

    json_file = "bayan_ul_quran_episodes_full.json"
    if not os.path.exists(json_file):
        print(f"Error: {json_file} not found.")
        return

    with open(json_file, "r", encoding="utf-8") as f:
        episodes = json.load(f)

    target_parts = set()

    if args.surah:
        query = args.surah.lower().strip()
        matched_surahs = []
        for s in SURAH_INDEX:
            if query in s["name"].lower():
                matched_surahs.append(s)
                target_parts.update(s["parts"])
        
        # Also check episode titles directly
        for ep in episodes:
            if query in ep["title"].lower():
                target_parts.add(ep["episode"])

        if matched_surahs:
            print(f"\n[+] Found Surah match for '{args.surah}':")
            for ms in matched_surahs:
                print(f"   • {ms['name']} -> Parts {ms['parts']}")
        elif target_parts:
            print(f"\n[+] Found title matches for '{args.surah}': Parts {sorted(target_parts)}")
        else:
            print(f"[-] No Surah or episode found matching '{args.surah}'.")
            print("Run with --list-surahs to see all available Surahs.")
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
        print("   python download_bayan.py --surah Fatiha         (Download Surah Al-Fatiha Part 5)")
        print("   python download_bayan.py --surah Kahf           (Download Surah Al-Kahf Parts 54 to 56)")
        print("   python download_bayan.py --start 6 --end 15     (Download Parts 6 to 15)")
        print("   python download_bayan.py --list-surahs          (Show full Surah index)")
        return

    selected_episodes = [ep for ep in episodes if ep["episode"] in target_parts]
    selected_episodes.sort(key=lambda x: x["episode"])

    print(f"\n[+] Selected {len(selected_episodes)} episodes: Parts {[e['episode'] for e in selected_episodes]}\n")

    os.makedirs(args.output_dir, exist_ok=True)

    # Check if yt-dlp is available
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
