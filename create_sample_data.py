import json
import os
import sys

def create_sample_data():
    """Create a sample data.json file with Islamic content for testing."""
    
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
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    # Path to data.json
    data_file = os.path.join(data_dir, "data.json")
    
    try:
        # Write the data to file with proper encoding
        with open(data_file, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, ensure_ascii=False, indent=2)
        
        # Verify the file was created and is valid JSON
        if os.path.exists(data_file):
            with open(data_file, 'r', encoding='utf-8') as f:
                # Try to parse the JSON to verify it's valid
                test_data = json.load(f)
                print(f"✓ Successfully created sample data file at: {data_file}")
                print(f"✓ File contains {len(test_data)} Islamic articles")
                return True
        else:
            print(f"✗ Failed to create data file at: {data_file}")
            return False
            
    except Exception as e:
        print(f"✗ Error creating sample data: {str(e)}")
        return False

if __name__ == "__main__":
    success = create_sample_data()
    if success:
        print("Sample data created successfully. You can now run the indexer.")
    else:
        print("Failed to create sample data. Please check the errors above.")
        sys.exit(1) 