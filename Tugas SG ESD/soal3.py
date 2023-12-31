# Urutan kedatangan teman-teman
urutan_kedatangan = ["Ningguang", "Hutao", "Xiao", "Childe"]

# Informasi kebiasaan teman-teman
kebiasaan = {
    "Ningguang": "memeriksa kue",
    "Hutao": "langsung memberikan kado",
    "Xiao": "memotret apa pun yang dilihat pertama kali",
    "Childe": "membawa air mineral dan meletakkan di meja"
}

# Menggabungkan informasi bahwa kue masih utuh di meja
kue_ada = True

# Memeriksa setiap teman
for teman in urutan_kedatangan:
    # Jika teman memiliki kebiasaan memeriksa kue dan kue masih utuh, maka dia yang mengambil
    if kebiasaan[teman] == "memeriksa kue" and kue_ada:
        print(f"{teman} adalah yang paling mungkin mengambil kue.")
        break
    # Jika teman memiliki kebiasaan lain, maka dia yang mungkin mengambil
    elif kebiasaan[teman] != "memeriksa kue":
        print(f"{teman} adalah yang paling mungkin mengambil kue.")
        break
else:
    print("Tidak dapat menentukan siapa yang mengambil kue.")
