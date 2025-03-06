import json
import os
import sys

def fix_data_json():
    """Forcefully delete and recreate the data.json file with valid Islamic content."""
    
    print("Fixing data.json file...")
    
    # Sample Islamic content
    sample_data = [
        {
            "title": "Abdestte Unutarak Su Yutmak Orucu Bozar mı?",
            "url": "https://www.islamveihsan.com/abdestte-unutarak-su-yutmak-orucu-bozar-mi.html",
            "content": "Abdestte unutarak su yutmak orucu bozmaz. Çünkü Peygamber Efendimiz (s.a.v) şöyle buyurmuştur: 'Ümmetimden hata, unutma ve zorla yaptırılan şeylerin sorumluluğu kaldırılmıştır.' Bu hadis-i şerif, unutarak yapılan fiillerin orucu bozmayacağını göstermektedir.",
            "category": "Oruç"
        },
        {
            "title": "Ramazan'da Neler Yapılır?",
            "url": "https://www.islamveihsan.com/ramazanda-neler-yapilir.html",
            "content": "Ramazan ayında oruç tutulur, teravih namazı kılınır, Kur'an-ı Kerim okunur, sadaka verilir ve iftar sofraları kurulur. Ramazan, Müslümanlar için manevi arınma ve ibadet ayıdır. Bu ayda yapılan ibadetlerin sevabı diğer aylara göre daha fazladır.",
            "category": "Ramazan"
        },
        {
            "title": "İslam'da Dua Etmenin Önemi",
            "url": "https://www.islamveihsan.com/islamda-dua-etmenin-onemi.html",
            "content": "Dua, Allah Teâlâ ile irtibatta bulunmak; O'na gönülden yönelmek, meramını vâsıta kullanmadan arz etmek demektir. Hadisi şerifte 'Bir şey istediğin vakit Allah'tan iste! Yardım dilediğin vakit Allah'tan dile!' buyrulmuştur. Dua ibadetin özüdür ve Allah'a yakınlaşmanın en önemli yollarından biridir.",
            "category": "Dua"
        }
    ]
    
    # Get absolute path to data.json
    data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "data.json")
    
    # Create data directory if it doesn't exist
    data_dir = os.path.dirname(data_file)
    os.makedirs(data_dir, exist_ok=True)
    
    print(f"Target file: {data_file}")
    
    # Delete the file if it exists
    if os.path.exists(data_file):
        try:
            os.remove(data_file)
            print(f"✓ Deleted existing file")
        except Exception as e:
            print(f"✗ Error deleting file: {str(e)}")
            return False
    
    try:
        # Write the data to a new file
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)
        
        # Verify the file was created and is valid JSON
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                file_content = f.read()
                print(f"File content preview: {file_content[:100]}...")
                
                # Try to parse the JSON to verify it's valid
                test_data = json.loads(file_content)
                print(f"✓ Successfully created valid JSON file with {len(test_data)} Islamic articles")
                return True
        else:
            print(f"✗ Failed to create data file")
            return False
            
    except Exception as e:
        print(f"✗ Error creating file: {str(e)}")
        return False

if __name__ == "__main__":
    success = fix_data_json()
    if success:
        print("✓ data.json fixed successfully. You can now run the indexer.")
    else:
        print("✗ Failed to fix data.json. Please check the errors above.")
        sys.exit(1) 