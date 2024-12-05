
class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def add_at_beginning(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            print("Linked list kosong. Tidak ada elemen yang dapat dihapus.")
            return
        if self.head.value == value:
            self.head = self.head.next_node
            return
        current = self.head
        while current.next_node and current.next_node.value != value:
            current = current.next_node
        if current.next_node:
            current.next_node = current.next_node.next_node
        else:
            print(f"Elemen dengan nilai {value} tidak ditemukan.")

    def display(self):
        if not self.head:
            print("Linked list kosong.")
            return
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next_node
        print(" -> ".join(map(str, elements)))

def menu():
    ll = LinkedList()
    while True:
        print("\n=== Menu Linked List ===")
        print("1. Tambah elemen di akhir")
        print("2. Tambah elemen di awal")
        print("3. Hapus elemen")
        print("4. Tampilkan elemen")
        print("5. Keluar")
        choice = input("Pilih opsi (1-5): ")
        if choice == "1":
            value = input("Masukkan nilai: ")
            ll.add_at_end(value)
        elif choice == "2":
            value = input("Masukkan nilai: ")
            ll.add_at_beginning(value)
        elif choice == "3":
            value = input("Masukkan nilai yang ingin dihapus: ")
            ll.delete(value)
        elif choice == "4":
            print("Elemen dalam linked list:")
            ll.display()
        elif choice == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    menu()
