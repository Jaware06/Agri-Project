import os
import re
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "kisansetu")
COLLECTION_NAME = "farming_techniques"

_client: Optional[MongoClient] = None


def get_db():
    global _client
    if _client is None:
        if not MONGO_URI:
            raise ValueError("MONGO_URI is missing in .env")
        _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    return _client[DB_NAME]


def _slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _generate_variants(base_list: List[Dict], count: int) -> List[Dict]:
    variants = []
    modifiers = [
        "for Arid Regions", "for High Yield", "for Small Farms", "Best Practices",
        "for Vegetables", "for Cereals", "in Tropical Climates", "Advanced Techniques",
        "Fundamentals", "Case Study", "Implementation", "for Orchards", "for Pulses",
        "Cost-Effective", "for Sloping Lands", "in Monsoons", "Modern Approach",
        "for Export Quality", "Deep Dive", "Quick Guide", "for Beginners"
    ]
    idx = 0
    mod_idx = 0
    while len(variants) < count:
        base = base_list[idx % len(base_list)]
        mod = modifiers[mod_idx % len(modifiers)]
        
        # the first time we add a base item, we just use its normal name
        if len(variants) < len(base_list):
            title = base["title"]
        else:
            title = f"{base['title']} {mod}"
            
        variants.append({
            "title": title,
            "category": base["category"],
            "description": base["description"],
            "image": base["image"],
            "badge": base["badge"],
            "type": "image"
        })
        idx += 1
        if idx % len(base_list) == 0:
            mod_idx += 1
            
    return variants


def _seed_records() -> List[Dict[str, Any]]:
    traditional_base = [
        {"title": "Crop Rotation", "category": "Traditional Techniques", "badge": "Traditional", "description": "Benefits for soil fertility and pest control.", "image": "https://images.unsplash.com/photo-1595841696677-6489ff3f8cd1?auto=format&fit=crop&w=600&q=80"},
        {"title": "Mixed Cropping", "category": "Traditional Techniques", "badge": "Traditional", "description": "Growing multiple crops together.", "image": "https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?auto=format&fit=crop&w=600&q=80"},
        {"title": "Intercropping", "category": "Traditional Techniques", "badge": "Traditional", "description": "Improves yield and reduces pests.", "image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80"},
        {"title": "Terrace Farming", "category": "Traditional Techniques", "badge": "Traditional", "description": "Efficient on hilly terrains.", "image": "https://images.unsplash.com/photo-1500076656116-558758c991c1?auto=format&fit=crop&w=600&q=80"},
        {"title": "Shifting Cultivation", "category": "Traditional Techniques", "badge": "Traditional", "description": "Historical practice and adaptation.", "image": "https://images.unsplash.com/photo-1505501869818-471a4f0270a6?auto=format&fit=crop&w=600&q=80"},
    ]

    modern_base = [
        {"title": "Precision Farming", "category": "Modern & Mechanized", "badge": "Modern", "description": "Use of GPS, sensors, and drones.", "image": "https://images.unsplash.com/photo-1586771107445-d3ca888129ff?auto=format&fit=crop&w=600&q=80"},
        {"title": "Mechanization", "category": "Modern & Mechanized", "badge": "Modern", "description": "Tractors, harvesters & planters.", "image": "https://images.unsplash.com/photo-1592982537447-7440770cbfc9?auto=format&fit=crop&w=600&q=80"},
        {"title": "Laser Land Leveling", "category": "Modern & Mechanized", "badge": "Modern", "description": "Ensures uniform water distribution.", "image": "https://images.unsplash.com/photo-1628189874795-09bd2925b3ea?auto=format&fit=crop&w=600&q=80"},
        {"title": "Hydroponics", "category": "Modern & Mechanized", "badge": "Modern", "description": "Soilless farming in water.", "image": "https://images.unsplash.com/photo-1585860956976-58c0c05df756?auto=format&fit=crop&w=600&q=80"},
        {"title": "Aeroponics", "category": "Modern & Mechanized", "badge": "Modern", "description": "Plants grow in mist environment.", "image": "https://images.unsplash.com/photo-1530836369250-ef71a3f5e481?auto=format&fit=crop&w=600&q=80"},
    ]

    sustainable_base = [
        {"title": "Organic Farming", "category": "Sustainable & Eco-Friendly", "badge": "Sustainable", "description": "Avoids chemicals, uses natural inputs.", "image": "https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=600&q=80"},
        {"title": "Agroforestry", "category": "Sustainable & Eco-Friendly", "badge": "Sustainable", "description": "Trees + crops for biodiversity.", "image": "https://images.unsplash.com/photo-1501084817091-a4f3d1d19e07?auto=format&fit=crop&w=600&q=80"},
        {"title": "Conservation Tillage", "category": "Sustainable & Eco-Friendly", "badge": "Sustainable", "description": "Minimal soil disturbance.", "image": "https://images.unsplash.com/photo-1599839619722-39751411ea63?auto=format&fit=crop&w=600&q=80"},
        {"title": "Mulching", "category": "Sustainable & Eco-Friendly", "badge": "Sustainable", "description": "Retains moisture and controls weeds.", "image": "https://images.unsplash.com/photo-1582845663673-f963a8a3ee26?auto=format&fit=crop&w=600&q=80"},
        {"title": "Rainwater Harvesting", "category": "Sustainable & Eco-Friendly", "badge": "Sustainable", "description": "Collects rainwater for use.", "image": "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=600&q=80"},
    ]

    innovative_base = [
        {"title": "Vertical Farming", "category": "Innovative & Emerging", "badge": "Innovative", "description": "Grow crops in stacked layers.", "image": "https://images.unsplash.com/photo-1530836369250-ef71a3f5e481?auto=format&fit=crop&w=600&q=80"},
        {"title": "IoT in Farming", "category": "Innovative & Emerging", "badge": "Innovative", "description": "Smart sensors for real-time data.", "image": "https://images.unsplash.com/photo-1532629345422-7515f3d16bb0?auto=format&fit=crop&w=600&q=80"},
        {"title": "AI-based Advisory", "category": "Innovative & Emerging", "badge": "Innovative", "description": "AI insights for better decisions.", "image": "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=600&q=80"},
        {"title": "Drones for Spraying", "category": "Innovative & Emerging", "badge": "Innovative", "description": "Efficient and precise spraying.", "image": "https://images.unsplash.com/photo-1586771107445-d3ca888129ff?auto=format&fit=crop&w=600&q=80"},
        {"title": "Smart Irrigation", "category": "Innovative & Emerging", "badge": "Innovative", "description": "Automated irrigation systems.", "image": "https://images.unsplash.com/photo-1563514253381-e2e71887aeb4?auto=format&fit=crop&w=600&q=80"},
    ]

    techniques = []
    # 25 per category = 100 total
    techniques.extend(_generate_variants(traditional_base, 25))
    techniques.extend(_generate_variants(modern_base, 25))
    techniques.extend(_generate_variants(sustainable_base, 25))
    techniques.extend(_generate_variants(innovative_base, 25))

    records: List[Dict[str, Any]] = []
    for item in techniques:
        item["slug"] = _slugify(item["title"])
        records.append(item)

    return records


def seed_farming_data() -> None:
    db = get_db()
    collection = db[COLLECTION_NAME]

    records = _seed_records()
    operations = []
    valid_slugs = []
    for record in records:
        slug = record["slug"]
        valid_slugs.append(slug)
        operations.append(
            UpdateOne(
                {"slug": slug},
                {"$set": record},
                upsert=True,
            )
        )

    if operations:
        collection.bulk_write(operations, ordered=False)
    collection.delete_many({"slug": {"$nin": valid_slugs}})
    collection.create_index("slug", unique=True)
    collection.create_index("category")


def get_techniques() -> List[Dict[str, Any]]:
    db = get_db()
    collection = db[COLLECTION_NAME]
    
    cursor = collection.find({})
    items: List[Dict[str, Any]] = []
    for item in cursor:
        item["_id"] = str(item["_id"])
        items.append(item)

    return items
