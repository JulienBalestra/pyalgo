class Link:
    """
    typedef     s_list
    {
        void    *value;
        s_list  *next;
    }           t_list;
    """
    def __init__(self, elt):
        self.value = elt
        self.next = None


class LinkedList:
    def __init__(self):
        self.first_elt = None

    def is_empty(self):
        return self.first_elt is None

    def insert_start(self, elt):
        new_link = Link(elt)
        new_link.next = self.first_elt
        self.first_elt = new_link

    def insert_end(self, elt):
        new_link = Link(elt)
        if not self.is_empty():
            current = self.first_elt
            while current.next is not None:
                current = current.next
            current.next = new_link
        else:
            self.first_elt = new_link

    def insert_index(self, elt, i):
        new_link = Link(elt)
        current = self.first_elt
        cpt = 0
        if i == 0:
            new_link.next = current
            self.first_elt = new_link
        elif not self.is_empty():
            while cpt != i - 1:
                current = current.next
                cpt += 1
                if current is None:
                    return False
            if current.next is not None:
                new_link.next = current.next
            current.next = new_link

    def delete(self, i):
        current = self.first_elt
        cpt = 0
        if self.is_empty():
            return False
        elif i == 0:
            self.first_elt = self.first_elt.next
            current.next = None
        else:
            while cpt != i - 1:
                current = current.next
                cpt += 1
                if current.next is None:
                    return False
            trash = current.next
            current.next = trash.next
            trash.next = None

    def get_value(self, i):
        current = self.first_elt
        cpt = 0
        if self.is_empty():
            return False
        else:
            while cpt != i:
                current = current.next
                cpt += 1
                if current is None:
                    return False
            return current.value

    def show(self):
        current = self.first_elt
        while current is not None:
            print current.value
            current = current.next