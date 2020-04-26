from data_structures.doubly_linked_list import LinkedList2, Node

import pytest


@pytest.fixture
def setup_nodes():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    return [n1, n2, n3, n4]


@pytest.fixture
def setup_linked_list(setup_nodes):
    n1, n2, n3, n4 = setup_nodes

    linkedList = LinkedList2()
    linkedList.add_in_tail(n1)
    linkedList.add_in_tail(n2)
    linkedList.add_in_tail(n3)
    linkedList.add_in_tail(n4)

    return linkedList


def test_len_and_clean_and_is_empty_methods(setup_nodes):
    n1, n2, n3, n4 = setup_nodes

    myLinkedList = LinkedList2()
    assert myLinkedList.len() == 0
    assert myLinkedList.is_empty() is True

    myLinkedList.add_in_tail(n1)
    assert myLinkedList.len() == 1
    assert myLinkedList.is_empty() is False

    myLinkedList.add_in_tail(n2)
    myLinkedList.add_in_tail(n3)
    myLinkedList.add_in_tail(n4)
    assert myLinkedList.len() == 4
    assert myLinkedList.is_empty() is False

    myLinkedList.clean()
    assert myLinkedList.len() == 0
    assert myLinkedList.is_empty() is True


def test_find_all_method(setup_linked_list, setup_nodes):
    n1, n2, n3, n4 = setup_nodes
    emptyLinkedList = LinkedList2()

    assert emptyLinkedList.find_all('non-existent value') == []
    assert setup_linked_list.find_all('non-existent value') == []

    assert setup_linked_list.find_all(1) == [n1]
    assert setup_linked_list.find_all(4) == [n4]

    sameAsN1 = Node(1)
    sameAsN4 = Node(4)
    setup_linked_list.add_in_tail(sameAsN1)
    setup_linked_list.add_in_tail(sameAsN4)
    assert setup_linked_list.find_all(1) == [n1, sameAsN1]
    assert setup_linked_list.find_all(4) == [n4, sameAsN4]


def test_delete_method(setup_linked_list, setup_nodes):
    n1, n2, n3, n4 = setup_nodes

    deletedN1 = setup_linked_list.delete(1)
    assert setup_linked_list.len() == 3
    assert deletedN1 == n1

    assert setup_linked_list.head == n2
    assert setup_linked_list.tail == n4

    deletedN2 = setup_linked_list.delete(2)
    assert setup_linked_list.len() == 2
    assert deletedN2 == n2

    assert setup_linked_list.head == n3
    assert setup_linked_list.tail == n4

    deletedN3 = setup_linked_list.delete(3)
    assert setup_linked_list.len() == 1
    assert deletedN3 == n3

    assert setup_linked_list.head == n4
    assert setup_linked_list.tail == n4
    assert n4.next is None
    assert n4.prev is None

    deletedN4 = setup_linked_list.delete(4)
    assert setup_linked_list.len() == 0
    assert deletedN4 == n4

    assert setup_linked_list.head is None
    assert setup_linked_list.tail is None


def test_delete_method_delete_all_case(setup_linked_list, setup_nodes):
    n1, n2, n3, n4 = setup_nodes

    n2_01 = Node(2)
    n2_02 = Node(2)
    n2_03 = Node(2)
    n2_04 = Node(2)
    setup_linked_list.add_in_tail(n2_01)
    setup_linked_list.add_in_tail(n2_02)
    setup_linked_list.add_in_tail(n2_03)
    setup_linked_list.add_in_tail(n2_04)
    deletedN2Nodes = setup_linked_list.delete(2, True)
    assert deletedN2Nodes == [n2, n2_01, n2_02, n2_03, n2_04]
    assert setup_linked_list.len() == 3
    assert setup_linked_list.head == n1
    assert setup_linked_list.tail == n4

    n3_01 = Node(3)
    setup_linked_list.add_in_tail(n3_01)
    deletedN3Nodes = setup_linked_list.delete(3, True)
    assert deletedN3Nodes == [n3, n3_01]
    assert setup_linked_list.len() == 2
    assert setup_linked_list.head == n1
    assert setup_linked_list.tail == n4
    deletedN1Nodes = setup_linked_list.delete(1, True)
    assert deletedN1Nodes == [n1]
    deletedN4Nodes = setup_linked_list.delete(4, True)
    assert deletedN4Nodes == [n4]
    assert setup_linked_list.head is None
    assert setup_linked_list.tail is None


def test_delete_method_delete_all_case_additional(
    setup_linked_list,
    setup_nodes,
):
    n1, n2, n3, n4 = setup_nodes

    n2_01 = Node(2)
    n2_02 = Node(2)
    n2_03 = Node(2)
    n2_04 = Node(2)
    setup_linked_list.delete(1, True)
    setup_linked_list.delete(4, True)
    assert setup_linked_list.len() == 2
    setup_linked_list.add_in_tail(n2_01)
    setup_linked_list.add_in_tail(n2_02)
    setup_linked_list.add_in_tail(n2_03)
    setup_linked_list.add_in_tail(n2_04)
    assert setup_linked_list.len() == 6
    deletedN2Nodes = setup_linked_list.delete(2, True)
    assert deletedN2Nodes == [n2, n2_01, n2_02, n2_03, n2_04]
    assert setup_linked_list.len() == 1
    assert setup_linked_list.head == n3
    assert setup_linked_list.tail == n3
    assert n3.next is None
    assert n3.prev is None
    deletedN3Nodes = setup_linked_list.delete(3, True)
    assert deletedN3Nodes == [n3]
    assert setup_linked_list.len() == 0
    assert setup_linked_list.head is None
    assert setup_linked_list.tail is None


def test_insert_method(setup_linked_list, setup_nodes):
    n1, n2, n3, n4 = setup_nodes
    myLinkedList = LinkedList2()

    n5 = Node(5)
    n6 = Node(6)
    myLinkedList.insert(None, n5)
    assert myLinkedList.len() == 1
    assert myLinkedList.head == n5
    assert myLinkedList.tail == n5
    myLinkedList.insert(n5, n6)
    assert myLinkedList.len() == 2
    assert myLinkedList.head == n5
    assert myLinkedList.tail == n6
