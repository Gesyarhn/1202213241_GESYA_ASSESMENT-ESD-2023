def analyze_reviews(ratings):
    if not ratings:
        return None

    # Menghitung rating terendah, rating tertinggi, dan rata-rata rating
    min_rating = min(ratings)
    max_rating = max(ratings)
    avg_rating = sum(ratings) / len(ratings)

    # Mengembalikan hasil dalam bentuk list
    return [min_rating, max_rating, avg_rating]

# Inisialisasi array kosong untuk data input pengguna
user_reviews = []

# Meminta input dari pengguna sebanyak 10 kali
for i in range(10):
    user_input = float(input(f"Masukkan nilai review aplikasi ke-{i+1}: "))
    user_reviews.append(user_input)

# Menganalisis review yang dimasukkan pengguna
user_output = analyze_reviews(user_reviews)
print(user_output)
