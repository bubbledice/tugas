
from graphviz import Digraph

# Membuat diagram use case
diagram = Digraph(format='png', engine='dot')
diagram.attr(rankdir='LR', size='8,5')

# Menambahkan node aktor dan sistem
diagram.node('User', 'Pengguna', shape='actor', fontsize='12')
diagram.node('System', 'Sistem Aplikasi', shape='rectangle', fontsize='12')
diagram.node('Payment', 'Payment Gateway', shape='rectangle', fontsize='12')
diagram.node('Admin', 'Admin Bioskop', shape='actor', fontsize='12')

# Menambahkan use case
use_cases = [
    ("UC1", "Membuka Aplikasi"),
    ("UC2", "Memilih Film"),
    ("UC3", "Memilih Jadwal dan Kursi"),
    ("UC4", "Melakukan Pembayaran"),
    ("UC5", "Menerima Tiket Digital")
]

for uc_id, uc_label in use_cases:
    diagram.node(uc_id, uc_label, shape='ellipse', fontsize='12')

# Menghubungkan aktor dan use case
diagram.edges([
    ('User', 'UC1'),  # Pengguna membuka aplikasi
    ('User', 'UC2'),  # Pengguna memilih film
    ('User', 'UC3'),  # Pengguna memilih jadwal dan kursi
    ('User', 'UC4'),  # Pengguna melakukan pembayaran
    ('User', 'UC5'),  # Pengguna menerima tiket digital
    ('UC4', 'Payment'),  # Sistem terhubung ke Payment Gateway
    ('Admin', 'System')  # Admin mengelola sistem
])

# Menghubungkan sistem dengan use case
diagram.edges([
    ('System', 'UC1'),
    ('System', 'UC2'),
    ('System', 'UC3'),
    ('System', 'UC4'),
    ('System', 'UC5')
])

# Menyimpan diagram ke file
output_path = r"D:\Belajar Hehe\Project\test lagi\output\res"
diagram.render(output_path, format='png', cleanup=True)

