from duckduckgo_search import DDGS
from urllib.parse import urlparse
from google import genai
import time
import random
import os

AI_API_KEY = "" #use ur api key here

def banner():
    print("=" * 50)
    print("🖥️  Simple Search Engine".center(50))
    print("=" * 50)

def AI_summary(search):
    if not search.strip():
        return None

    prompt = f"""
    Kamu adalah asisten peneliti yang cerdas. Berikut adalah hasil pencarian web dari sebuah topik. 
    Tolong buatkan kesimpulan/rangkuman yang padat, jelas, dan informatif dalam bahasa Indonesia (maksimal 3-4 paragraf) berdasarkan informasi di bawah ini saja.
    
    Informasi Hasil Pencarian:
    {search}
    
    Kesimpulan:
    """

    try:
        client = genai.Client(api_key=AI_API_KEY)
        response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)
        return response.text
    except Exception:
        return "\n😫 AI Couldn't Find Your Request"   

def search_enginee(word_input):
    word = word_input.split('.')[0]
    key_word = " ".join(word.split()[:8])

    print("\n🔍Searching.......\n")
    print("-" * 50)

    try:
        with DDGS() as ddgs:
            time.sleep(random.uniform(1.5 ,3.0))
            search_result = ddgs.news(key_word, region="id-id", max_results=3)

            kumpulan_text = ""
            nomor_sumber = 1
            
            if not search_result:
                print("❌ Hasil Tidak Ditemukan")

            if search_result:
                print("✅ Berikut Hasil Yang Relevan\n")

                for result in search_result:
                    title = result.get("title", "None")
                    url = result.get("url", "None")
                    source = result.get("source") or urlparse(url).netloc
                    body = result.get('body') or result.get('snippet', "")
                    
                    print("-" * 50)
                    print(f"📖 Title \t: {title}")
                    print(f"🔗 URL \t\t: {url}")
                    print(f"📰 Source \t: {source}")

                    if body:
                        kumpulan_text += f"Sumber: {nomor_sumber}:\nJudul: {title}\nIsi: {body}\n\n"
                        nomor_sumber += 1

            if kumpulan_text.strip():
                kesimpulan = AI_summary(kumpulan_text)
                if kesimpulan:
                    print("\n" + "=" * 50)
                    print("🤖 KESIMPULAN AI ".center(50))
                    print("=" * 50)
                    print(kesimpulan)
                    print("=" * 50 + "\n")        

    except Exception as e:
        print("-" * 50)
        print(f"\n😫 Something Wrong {e}")
        print("Try Again for a few minutes")

def main():
    os.system('cls')

    banner()

    while True:
        print("[+] Search Here")
        text_input = input(">> ")

        if text_input:
            search_enginee(text_input)
            break
        else:
            print("\n❌ ERROR INPUT")
            continue    

if __name__ == '__main__':
    main()