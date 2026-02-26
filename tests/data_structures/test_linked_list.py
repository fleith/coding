from src.data_structures.linked_list import LinkedList


def test_linked_list_initialization():
    linked_list = LinkedList()
    assert len(linked_list) == 0
    assert str(linked_list) == "Empty"


def test_linked_list_append():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    assert len(linked_list) == 3
    assert linked_list.display() == [10, 20, 30]


def test_linked_list_prepend():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.prepend(5)
    linked_list.prepend(1)
    assert len(linked_list) == 3
    assert linked_list.display() == [1, 5, 10]


def test_linked_list_delete_existing_node():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    assert linked_list.delete(20) is True
    assert len(linked_list) == 2
    assert linked_list.display() == [10, 30]


def test_linked_list_delete_nonexistent_node():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    assert linked_list.delete(40) is False
    assert len(linked_list) == 2
    assert linked_list.display() == [10, 20]


def test_linked_list_find_existing_node():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    assert linked_list.find(20) is True
    assert linked_list.find(10) is True


def test_linked_list_find_nonexistent_node():
    linked_list = LinkedList()
    linked_list.append(10)
    assert linked_list.find(30) is False


def test_linked_list_str_representation():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    assert str(linked_list) == "10 -> 20 -> 30"
