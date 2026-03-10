Mulai
    Buat class Node
        data
        next ← NULL

    node1 ← Node(10)
    node2 ← Node(20)
    node3 ← Node(30)

    node1.next ← node2
    node2.next ← node3

    current ← node1

    Selama current ≠ NULL lakukan
        Tampilkan current.data
        current ← current.next
Selesai