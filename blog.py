import os
import random

COMMON_IMAGES = [
    "https://pawarta.github.io/img/bahasa-jawa.jpeg",
    "https://pawarta.github.io/img/ai.jpeg",
    "https://pawarta.github.io/img/3d.jpeg"
]

def generate_html_content(category, title_suffix, file_num):
    img_url = random.choice(COMMON_IMAGES)
    cat_upper = category.replace("/", " - ").upper()
    
    html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PAWARTA - {cat_upper} - Artikel {file_num}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
<nav class="navbar navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="https://pawarta.github.io/index.html">PAWARTA - {cat_upper}</a>
  </div>
</nav>
<div class="container my-5">
    <h1>Artikel {file_num} - {cat_upper}</h1>
    <p>Konten otomatis untuk kategori {category}.</p>
    <a href="index.html" class="btn btn-secondary">Kembali</a>
</div>
</body>
</html>
"""
    return html

def generate_index_content(category):
    cat_upper = category.replace("/", " - ").upper()
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>PAWARTA - Kategori {cat_upper}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
<div class="container my-5">
    <h1>Daftar Artikel: {cat_upper}</h1>
    <ul>
""" + "".join([f'        <li><a href="artikel{i}.html">Artikel {i}</a></li>\n' for i in range(1, 31)]) + f"""    </ul>
</div>
</body>
</html>
"""

def main():
    # 1. Buat file 'categories.txt' otomatis jika belum ada
    if not os.path.exists("categories.txt"):
        default_cats = [
            "market", "finance", "tech", "lifestyle", "zodiak", 
            "tools/ai", "tools/calendar", "tools/quran", "tools/tts", "tools/maps", "tools/qr"
        ]
        with open("categories.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(default_cats))
        print("File 'categories.txt' berhasil dibuat dengan kategori default.")

    # 2. Baca kategori dari file 'categories.txt' (Anda bisa tambah kategori kapan saja di file ini)
    with open("categories.txt", "r", encoding="utf-8") as f:
        categories = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for cat in categories:
        os.makedirs(cat, exist_ok=True)
        
        # Buat 30 artikel per kategori
        for i in range(1, 31):
            file_path = os.path.join(cat, f"artikel{i}.html")
            # Opsional: Jika ingin file yang sudah ada tidak tertimpa, beri kondisi (if not os.path.exists)
            with open(file_path, "w", encoding="utf-8") as pf:
                pf.write(generate_html_content(cat, f"Artikel {i}", i))
        
        # Buat index.html di dalam folder kategori
        with open(os.path.join(cat, "index.html"), "w", encoding="utf-8") as inf:
            inf.write(generate_index_content(cat))
            
        print(f"Folder & Artikel untuk '{cat}' berhasil diperbarui/ditambahkan.")

if __name__ == "__main__":
    main()
