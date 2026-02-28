from tabulate import tabulate
import kurs as kurs_file
import konverter as konvert

def tampilkan_tabel():
    items = kurs_file.kurs.items()
    data = [[k, f"{v:,.0f}".replace(",",".")] for k, v in items]
    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=['Kode', 'Kurs'], tablefmt="pretty"))

def main():
    tampilkan_tabel()
    konvert.konversi()

if __name__ == "__main__":
    main()