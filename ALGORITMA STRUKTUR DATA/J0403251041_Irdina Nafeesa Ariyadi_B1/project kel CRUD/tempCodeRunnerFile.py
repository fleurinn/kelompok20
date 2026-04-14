    for kategori, daftar_merk in buka_data.items():
                print(f"\n• {kategori}")
                for merk, daftar_series in daftar_merk.items():
                    print(f"   ├── {merk}")
                    for series in daftar_series:
                        print(f"   │    • {series}")
