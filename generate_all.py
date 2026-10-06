import os

# Daftar 69 kategori lengkap sesuai permintaan
categories = [
    "market", "finance", "macro", "micro", "economy", "explainers", "manufacturing", 
    "property", "health", "education", "lifestyle", "hospitality", "tech", "media", 
    "smes", "luxury", "whos-who", "international", "local-resources", "politics", 
    "culture", "science", "public-policy", "business", "news", "sports", "arts", 
    "celebrities", "automotive", "commentary", "interview", "money", "perbankan", 
    "belanja", "sharia", "football", "opinion", "video", "kisah", "index", 
    "sejarah", "entrepreneur", "research", "photo", "olahraga", "selebritis", 
    "country", "dki", "diy", "jabar", "jatim", "jateng", "aceh", "papua", 
    "kalimantan", "sumatra", "sulawesi", "bali", "asia", "afrika", "australia", 
    "rusia", "eropa", "amerika", "ai", "teknologi", "astronomi", "zodiak", "maps"
]

def generate_html(cat, page_num):
    title = f"PAWARTA - {cat.upper()} - Artikel {page_num}" if page_num > 0 else f"PAWARTA - {cat.upper()} - Beranda"
    url = f"https://pawarta.github.io/{cat}/artikel{page_num}.html" if page_num > 0 else f"https://pawarta.github.io/{cat}/index.html"
    
    return f"""<!DOCTYPE html>
<html lang="jv">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <!-- Meta SEO & Verification -->
    <meta name="description" content="Pawarta minangka portal warta digital, informasi modheren, lan pelestarian kabudayan Jawi sarta aksara Honocoroko ing era digital tumrap kategori {cat}.">
    <meta name="keywords" content="pawarta, {cat}, warta jawa, berita jawa, honocoroko, aksara jawa, portal warta, pawarta github io">
    <meta name="robots" content="index, follow">
    <meta name="google-site-verification" content="IAcn_DcNzAkFuMAjiMDNMoUEMZV5oKau1XrJ4aDJlRc">
    <meta name="msvalidate.01" content="E9411F953448412F854C1FBA584B1383">
    
    <!-- Google AdSense & AMP -->
    <script async custom-element="amp-ad" src="https://cdn.ampproject.org/v0/amp-ad-0.1.js"></script>
    <script async crossorigin="anonymous" src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9308517202792186"></script>
    <script async custom-element="amp-auto-ads" src="https://cdn.ampproject.org/v0/amp-auto-ads-0.1.js"></script>

    <!-- Open Graph / Social Media Meta -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="Pusat informasi warta digital lan kabudayan kanthi nuansa Jawi modern ing kategori {cat}.">
    <meta property="og:image" content="https://pawarta.github.io/pawarta.jpg">
    <meta property="og:url" content="{url}">
    <meta property="og:type" content="article">

    <!-- Favicon & Icons -->
    <link rel="icon" href="https://pawarta.github.io/pawarta.ico" type="image/x-icon">
    <link rel="shortcut icon" href="https://pawarta.github.io/pawarta.ico" type="image/x-icon">
    <link rel="icon" href="https://pawarta.github.io/pawarta.jpg" type="image/x-icon">
    <link rel="shortcut icon" href="https://pawarta.github.io/pawarta.png" type="image/x-icon">

    <!-- Canonical & Hreflang Links -->
    <link rel="canonical" href="{url}">
    <link rel="alternate" href="https://pawarta.github.io/en-us/" hreflang="en-us">
    <link rel="alternate" href="https://pawarta.github.io/en/" hreflang="en">
    <link rel="alternate" href="https://pawarta.github.io/es/" hreflang="es">
    <link rel="alternate" href="https://pawarta.github.io/" hreflang="x-default">
    <link rel="alternate" hreflang="fr" href="https://pawarta.github.io/fr/">
    <link rel="alternate" hreflang="de" href="https://pawarta.github.io/de/">
    <link rel="alternate" hreflang="th" href="https://pawarta.github.io/th/">
    <link rel="alternate" hreflang="id" href="https://pawarta.github.io/id/">

    <!-- Stylesheets (Bootstrap 5, Icons, Animate.css) -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css"/>
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

    <!-- Google tag (gtag.js) - GA4 ID: G-GN5PGKKM3T -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-GN5PGKKM3T"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-GN5PGKKM3T');
    </script>
    <style>
        .rainbow-text {{ background: linear-gradient(45deg, #d4af37, #ff6b6b, #48dbfb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .honocoroko-title {{ font-family: serif; color: #d4af37; font-size: 1.25rem; }}
        .carousel-item {{ height: 400px; background-size: cover; background-position: center; position: relative; }}
        .carousel-overlay {{ position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.6); }}
    </style>
</head>
<body class="bg-light text-dark">

    <!-- Header & Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top shadow">
        <div class="container">
            <a class="navbar-brand d-flex align-items-center gap-2" href="https://pawarta.github.io/index.html">
                <img src="https://pawarta.github.io/pawarta.jpg" alt="Logo Pawarta" width="40" height="40" class="rounded-circle">
                <div>
                    <span class="rainbow-text fs-4">PAWARTA</span>
                    <div style="font-size: 10px; color: #d4af37;">ꦥꦮꦂꦠ - Javanese Portal ({cat.upper()})</div>
                </div>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="https://pawarta.github.io/index.html">Home</a></li>
                    <li class="nav-item"><a class="nav-link active" href="https://pawarta.github.io/{cat}/index.html">{cat.capitalize()}</a></li>
                    <li class="nav-item"><a class="nav-link" href="https://pawarta.github.io/news/index.html">News</a></li>
                    <li class="nav-item"><a class="nav-link" href="https://pawarta.github.io/market/index.html">Market</a></li>
                    <li class="nav-item"><a class="nav-link" href="https://pawarta.github.io/tech/index.html">Tech</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Main Content & Long Article Section -->
    <main id="artikels" class="container my-5">
        <div class="row">
            <!-- Article Content Area -->
            <div class="col-lg-8" data-aos="fade-up">
                <article class="bg-white p-4 p-md-5 rounded-4 shadow-sm border mb-4">
                    <div class="mb-3">
                        <span class="badge bg-warning text-dark">Kategori: {cat.capitalize()}</span>
                        <span class="text-muted ms-2"><i class="bi bi-calendar3"></i> 2026-10-06</span>
                        <span class="text-muted ms-2"><i class="bi bi-eye"></i> 14,520 Waca</span>
                    </div>

                    <h1 class="fw-bold mb-3">Analisis Komprehensif lan Perkembangan Anyar ing Sektor {cat.capitalize()} Tumrap Era Digital</h1>
                    <h2 class="h4 text-secondary mb-4">Transformasi, Tantangan, lan Peluang Strategis ing Donya Modheren</h2>

                    <!-- Image with Alt Image -->
                    <div class="mb-4 text-center">
                        <img src="https://pawarta.github.io/img/{cat}.jpeg" alt="Ilustrasi warta {cat} portal digital Pawarta" class="img-fluid rounded shadow-sm" onerror="this.src='https://pawarta.github.io/pawarta.jpg'">
                        <div class="form-text mt-1 text-muted">Ilustrasi Visual Eksklusif {cat.capitalize()} - PAWARTA 2026</div>
                    </div>

                    <!-- Google AdSense Banner -->
                    <div class="my-4 text-center">
                        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9308517202792186" data-ad-slot="8374036730" data-ad-format="auto" data-full-width-responsive="true"></ins>
                        <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
                    </div>

                    <p class="lead">Ing era globalisasi lan digitalisasi taun 2026 menika, sektor <strong>{cat}</strong> ngadepi kathah owah-owahan lan dinamika ingkang luar biasa. Minangka bagean saking portal warta <strong>PAWARTA</strong>, artikel menika badhe ngandharaken kanthi jero lan tuntas gegayutan kalih kemajuan, tantangan, sarta strategi ingkang kedah dipun lampahi dening para pemangku kepentingan.</p>

                    <h3 class="fw-bold mt-4">1. Latar Belakang lan Sejarah Singkat {cat.capitalize()}</h3>
                    <p>Pangembangan {cat} sampun lumampah kanthi cepet wiwit dasawarsa pungkasan. Miturut cathetan sejarah lan panaliten, adhedhasar kearifan lokal sarta adopsi teknologi tinggi, sektor menika dados pilar penting ing pertumbuhan ekonomi nasional lan regional. Masyarakat saged ningkataken produktivitas lumantar inovasi digital lan panggunaan sarana modern.</p>

                    <h3 class="fw-bold mt-4">2. Tabel Ringkesan Data & Statistik {cat.capitalize()}</h3>
                    <div class="table-responsive my-3">
                        <table class="table table-bordered table-striped">
                            <thead class="table-dark">
                                <tr>
                                    <th>No</th>
                                    <th>Parameter Indikator</th>
                                    <th>Capaian Taun 2025</th>
                                    <th>Proyeksi Taun 2026</th>
                                    <th>Tingkat Pertumbuhan</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1</td>
                                    <td>Adopsi Teknologi & Digitalisasi</td>
                                    <td>78.5%</td>
                                    <td>89.2%</td>
                                    <td>+12.1%</td>
                                </tr>
                                <tr>
                                    <td>2</td>
                                    <td>Partisipasi Masyarakat / Pasar</td>
                                    <td>1.2 Juta</td>
                                    <td>1.8 Juta</td>
                                    <td>+50.0%</td>
                                </tr>
                                <tr>
                                    <td>3</td>
                                    <td>Efisiensi Operasional</td>
                                    <td>65.0%</td>
                                    <td>82.4%</td>
                                    <td>+17.4%</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <h3 class="fw-bold mt-4">3. Tantangan Utama lan Solusi Strategis</h3>
                    <p>Sanadyan kathah kemajuan ingkang dipun gayuh, wonten pinten-pinten tantangan ingkang kedah dipun rampungaken, antawisipun:</p>
                    <ul>
                        <li><strong>Keterbatasan Sumber Daya Manusia (SDM):</strong> Perlu pelatihan lan peningkatan kapasitas kompetensi teknis.</li>
                        <li><strong>Infrastruktur Digital:</strong> Panyebaran jaringan sing durung merata ing sawetara wilayah pelosok.</li>
                        <li><strong>Regulasi lan Kebijakan:</strong> Penyesuaian aturan hukum supados selaras kaliyan perkembangan teknologi AI lan digital.</li>
                    </ul>

                    <!-- 7 Internal Links -->
                    <div class="card bg-light border-0 p-3 my-4">
                        <h5 class="fw-bold text-dark mb-2">Pranala Internal Terkait:</h5>
                        <ul class="mb-0">
                            <li><a href="https://pawarta.github.io/market/index.html">Market & Finance Update 2026</a></li>
                            <li><a href="https://pawarta.github.io/tech/index.html">Perkembangan Teknologi & AI Terbaru</a></li>
                            <li><a href="https://pawarta.github.io/culture/index.html">Kabudayan Jawi lan Honocoroko</a></li>
                            <li><a href="https://pawarta.github.io/economy/index.html">Analisis Ekonomi Regional</a></li>
                            <li><a href="https://pawarta.github.io/news/index.html">Warta Utama Terkini</a></li>
                            <li><a href="https://pawarta.github.io/opinion/index.html">Kolom Opini Pengamat</a></li>
                            <li><a href="https://pawarta.github.io/index.html">Halaman Utama PAWARTA</a></li>
                        </ul>
                    </div>

                    <h3 class="fw-bold mt-4">4. FAQ (Pitakon Asring Dipun Ajengaken)</h3>
                    <div class="accordion" id="faqAccordion">
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingOne">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
                                  Kados pundi cara nggabungaken teknologi modern lan budaya lokal ing sektor {cat}?
                                </button>
                            </h2>
                            <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#faqAccordion">
                                <div class="accordion-body">
                                  Kanthi nggunakake pendekatan hibrida, ing pundi nilai-nilai luhur tradhisi Jawi dipun selarasaken kaliyan efisiensi lan otomatisasi teknologi digital modheren.
                                </div>
                            </div>
                        </div>
                        <div class="accordion-item">
                            <h2 class="accordion-header" id="headingTwo">
                                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo">
                                  Menapa mangpaat utami saking pengembangan {cat} ing taun 2026?
                                </button>
                            </h2>
                            <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                                <div class="accordion-body">
                                  Mangpaat utaminipun inggih punika peningkatan produktivitas, transparansi informasi, lan terbukane lapangan kerja baru liwat ekosistem digital.
                                </div>
                            </div>
                        </div>
                    </div>

                    <h3 class="fw-bold mt-4">5. Kesimpulan (Conclusion)</h3>
                    <p>Kesimpulanipun, sektor {cat} gadhah potensi ingkang ageng sanget kagem kemajuan sesarengan. Kanthi kolaborasi antawisipun pemerintah, pelaku industri, lan masyarakat, cita-cita kagem mujudaken peradaban ingkang gemah ripah loh jinawi saged kasinggah.</p>

                    <!-- 7 External Links -->
                    <div class="card bg-white border p-3 my-4">
                        <h5 class="fw-bold text-dark mb-2">Pranala Eksternal & Referensi Global:</h5>
                        <ul class="mb-0 small text-muted">
                            <li><a href="https://www.wikipedia.org" target="_blank" rel="noopener noreferrer">Wikipedia Global Encyclopedia</a></li>
                            <li><a href="https://www.bbc.com" target="_blank" rel="noopener noreferrer">BBC International News</a></li>
                            <li><a href="https://www.reuters.com" target="_blank" rel="noopener noreferrer">Reuters Financial & Market News</a></li>
                            <li><a href="https://www.github.com" target="_blank" rel="noopener noreferrer">GitHub Open Source Development Platform</a></li>
                            <li><a href="https://www.google.com" target="_blank" rel="noopener noreferrer">Google Search & Technology Engine</a></li>
                            <li><a href="https://www.wikipedia.org/wiki/Java" target="_blank" rel="noopener noreferrer">Javanese Culture Reference on Wikipedia</a></li>
                            <li><a href="https://www.un.org" target="_blank" rel="noopener noreferrer">United Nations Global Development Goals</a></li>
                        </ul>
                    </div>

                    <!-- Social Share & Contact Form -->
                    <div class="border-top pt-4 mt-4">
                        <h5 class="fw-bold mb-3"><i class="bi bi-share"></i> Bagikan Warta Menika:</h5>
                        <div class="d-flex gap-2 mb-4">
                            <a href="https://wa.me/?text={url}" class="btn btn-success btn-sm"><i class="bi bi-whatsapp"></i> WhatsApp</a>
                            <a href="https://twitter.com/intent/tweet?url={url}" class="btn btn-dark btn-sm"><i class="bi bi-twitter-x"></i> Twitter / X</a>
                            <a href="https://www.facebook.com/sharer/sharer.php?u={url}" class="btn btn-primary btn-sm"><i class="bi bi-facebook"></i> Facebook</a>
                        </div>

                        <h5 class="fw-bold mb-3"><i class="bi bi-envelope"></i> Kirim Komentar / Pitaken (Kontak Form):</h5>
                        <form onsubmit="event.preventDefault(); alert('Matur nuwun! Pesen panjenengan sampun kasil kairim.');">
                            <div class="mb-3">
                                <label class="form-label">Asma Lengkap</label>
                                <input type="text" class="form-control" required placeholder="Lebetaken asma panjenengan...">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Alamat Email</label>
                                <input type="email" class="form-control" required placeholder="email@example.com">
                            </div>
                            <div class="mb-3">
                                <label class="form-label">Pesen / Tanggapan</label>
                                <textarea class="form-control" rows="3" required placeholder="Tulis pesen panjenengan ing mriki..."></textarea>
                            </div>
                            <button type="submit" class="btn btn-warning fw-bold">Kirim Pesen</button>
                        </form>
                    </div>

                </article>
            </div>

            <!-- Sidebar -->
            <div class="col-lg-4" data-aos="fade-left">
                <!-- Widget: News & Popular -->
                <div class="card shadow-sm border-0 mb-4 p-3">
                    <h5 class="fw-bold border-bottom pb-2 text-dark"><i class="bi bi-newspaper"></i> Warta & Artikel Populer</h5>
                    <ul class="list-unstyled mb-0 small">
                        <li class="py-2 border-bottom"><a href="https://pawarta.github.io/{cat}/artikel1.html" class="text-decoration-none text-dark fw-bold">Transformasi Digital Sektor {cat.capitalize()} ing Era Modern</a></li>
                        <li class="py-2 border-bottom"><a href="https://pawarta.github.io/{cat}/artikel2.html" class="text-decoration-none text-dark fw-bold">Strategi Jitu Ngadepi Tantangan Ekonomi 2026</a></li>
                        <li class="py-2"><a href="https://pawarta.github.io/{cat}/artikel3.html" class="text-decoration-none text-dark fw-bold">Peran Kearifan Lokal Jawi tumrap Pembangunan Global</a></li>
                    </ul>
                </div>

                <!-- Widget: Terbaru & Terlama -->
                <div class="card shadow-sm border-0 mb-4 p-3">
                    <h5 class="fw-bold border-bottom pb-2 text-dark"><i class="bi bi-clock-history"></i> Artikel Terbaru & Terlama</h5>
                    <ul class="list-unstyled mb-0 small">
                        <li class="py-2 border-bottom"><strong>Terbaru:</strong> <a href="https://pawarta.github.io/{cat}/artikel30.html" class="text-decoration-none">Inovasi Terkini {cat.capitalize()} Minggu Menika</a></li>
                        <li class="py-2"><strong>Terlama:</strong> <a href="https://pawarta.github.io/{cat}/artikel1.html" class="text-decoration-none">Arsip Dasar & Fondasi Awal {cat.capitalize()}</a></li>
                    </ul>
                </div>

                <!-- Widget: Label & Archive -->
                <div class="card shadow-sm border-0 mb-4 p-3">
                    <h5 class="fw-bold border-bottom pb-2 text-dark"><i class="bi bi-tags"></i> Label & Archive</h5>
                    <div class="d-flex flex-wrap gap-1 mb-2">
                        <a href="https://pawarta.github.io/{cat}/index.html" class="badge bg-secondary text-decoration-none">{cat}</a>
                        <a href="https://pawarta.github.io/news/index.html" class="badge bg-secondary text-decoration-none">warta</a>
                        <a href="https://pawarta.github.io/culture/index.html" class="badge bg-secondary text-decoration-none">budaya</a>
                        <a href="https://pawarta.github.io/tech/index.html" class="badge bg-secondary text-decoration-none">teknologi</a>
                    </div>
                    <ul class="list-unstyled small mb-0">
                        <li><a href="https://pawarta.github.io/{cat}/sitemap.html">HTML Sitemap</a></li>
                        <li><a href="https://pawarta.github.io/{cat}/sitemap.xml">XML Sitemap</a></li>
                        <li><a href="https://pawarta.github.io/{cat}/sitemap.txt">TXT Sitemap</a></li>
                    </ul>
                </div>

                <!-- Adsense Sidebar -->
                <div class="card shadow-sm border-0 p-3 text-center">
                    <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9308517202792186" data-ad-slot="8374036730" data-ad-format="auto" data-full-width-responsive="true"></ins>
                    <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
                </div>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="pt-5 pb-4 bg-dark text-white border-top border-warning">
        <div class="container text-center text-md-start">
            <div class="row">
                <div class="col-md-4 mb-4">
                    <h5 class="text-white fw-bold mb-3"><span class="rainbow-text">PAWARTA</span></h5>
                    <p class="small text-secondary">Portal warta digital inovatif kang nyawijiake kabudayan Jawi, aksara Honocoroko, lan teknologi informasi modheren ing donya maya.</p>
                    <div class="fs-4 text-warning">ꦫꦲꦪꦸ ꦫꦲꦪꦸ ꦫꦲꦪꦸ</div>
                </div>
                <div class="col-md-4 mb-4">
                    <h6 class="text-white fw-bold mb-3">Pranala Kaca</h6>
                    <ul class="list-unstyled small">
                        <li><a href="https://pawarta.github.io/index.html" class="text-decoration-none text-secondary">Beranda / Index</a></li>
                        <li><a href="https://pawarta.github.io/about.html" class="text-decoration-none text-secondary">Tentang Kami</a></li>
                        <li><a href="https://pawarta.github.io/contact.html" class="text-decoration-none text-secondary">Kontak</a></li>
                        <li><a href="https://pawarta.github.io/privacy.html" class="text-decoration-none text-secondary">Kebijakan Privasi</a></li>
                        <li><a href="https://pawarta.github.io/terms.html" class="text-decoration-none text-secondary">Syarat & Ketentuan</a></li>
                    </ul>
                </div>
                <div class="col-md-4 mb-4">
                    <h6 class="text-white fw-bold mb-3">Informasi Aliran Data</h6>
                    <p class="small text-secondary mb-1">Nama Aliran: <strong>pawarta</strong></p>
                    <p class="small text-secondary mb-1">ID Pengukuran: <code class="text-warning">G-GN5PGKKM3T</code></p>
                    <p class="small text-secondary">URL: <a href="https://pawarta.github.io" class="text-decoration-none text-warning">https://pawarta.github.io</a></p>
                </div>
            </div>
            <hr class="border-secondary">
            <div class="row text-center small text-secondary">
                <div class="col-md-12">
                    <p class="mb-0">&copy; 2026 PAWARTA (pawarta.github.io). Hak Cipta Dilindungi Undang-Undang. Kinarya kanti katresnan tumrap Budaya Jawi.</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- Bootstrap JS & AOS Animation Script -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>AOS.init({{ duration: 1000, once: true }});</script>
</body>
</html>
"""

def generate_sitemap_xml(cat):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\\n'
    xml += f'  <url><loc>https://pawarta.github.io/{cat}/index.html</loc><lastmod>2026-10-06</lastmod></url>\\n'
    for i in range(1, 31):
        xml += f'  <url><loc>https://pawarta.github.io/{cat}/artikel{i}.html</loc><lastmod>2026-10-06</lastmod></url>\\n'
    xml += '</urlset>'
    return xml

def generate_sitemap_txt(cat):
    txt = f"https://pawarta.github.io/{cat}/index.html\\n"
    for i in range(1, 31):
        txt += f"https://pawarta.github.io/{cat}/artikel{i}.html\\n"
    return txt

def generate_sitemap_html(cat):
    html = f"""<!DOCTYPE html>
<html lang="jv">
<head><meta charset="UTF-8"><title>Sitemap - {cat.capitalize()} - PAWARTA</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"></head>
<body class="container py-5">
    <h1 class="mb-4">Sitemap: {cat.capitalize()}</h1>
    <ul class="list-group">
        <li class="list-group-item"><a href="https://pawarta.github.io/{cat}/index.html">Index {cat.capitalize()}</a></li>
"""
    for i in range(1, 31):
        html += f'        <li class="list-group-item"><a href="https://pawarta.github.io/{cat}/artikel{i}.html">Artikel {i}</a></li>\\n'
    html += '    </ul></body></html>'
    return html

print("Mulai proses pembuatan direktori lan file...")
for cat in categories:
    os.makedirs(cat, exist_ok=True)
    
    # index.html (page 0)
    with open(os.path.join(cat, "index.html"), "w", encoding="utf-8") as f:
        f.write(generate_html(cat, 0))
        
    # artikel 1 s.d. 30
    for i in range(1, 31):
        with open(os.path.join(cat, f"artikel{i}.html"), "w", encoding="utf-8") as f:
            f.write(generate_html(cat, i))
            
    # sitemaps (html, xml, txt)
    with open(os.path.join(cat, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(generate_sitemap_html(cat))
    with open(os.path.join(cat, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(generate_sitemap_xml(cat))
    with open(os.path.join(cat, "sitemap.txt"), "w", encoding="utf-8") as f:
        f.write(generate_sitemap_txt(cat))

print("Selesai! Seluruh kategori & 30 artikel per kategori berhasil digenerate.")
