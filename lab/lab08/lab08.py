# ???x
def duplicate_link(link, val):
    """Mutates `link` such that if there is a linked list
    node that has a first equal to value, that node will
    be duplicated. Note that you should be mutating the
    original link list.

    >>> x = Link(5, Link(4, Link(3)))
    >>> duplicate_link(x, 5)
    >>> x
    Link(5, Link(5, Link(4, Link(3))))
    >>> y = Link(2, Link(4, Link(6, Link(8))))
    >>> duplicate_link(y, 10)
    >>> y
    Link(2, Link(4, Link(6, Link(8))))
    >>> z = Link(1, Link(2, (Link(2, Link(3)))))
    >>> duplicate_link(z, 2) # ensures that back to back links with val are both duplicated
    >>> z
    Link(1, Link(2, Link(2, Link(2, Link(2, Link(3))))))
    """
    "*** YOUR CODE HERE ***"
    if link == Link.empty or link.rest == Link.empty:
        return
    elif link.first == val:
        remaining = link.rest
        link.rest = Link(val, remaining)
        duplicate_link(remaining, val)
        # return link
    else:
        duplicate_link(link.rest, val)
        # return link

    ''' Official Solution
    if link is Link.empty:
        return
    elif link.first == val:
        remaining = link.rest
        link.rest = Link(val, remaining)
        duplicate_link(remaining, val)
    else:
        duplicate_link(link.rest, val)
    '''
    ''' My old solution
    if link == Link.empty or link.rest == Link.empty:
        return
    elif link.first == val:
        # 這個方法行不通，因為題目說到要 mutate，但是下面這行的指令確是建立一個新的 link ，所以答案會是錯的
        link = Link(val, link)
        duplicate_link(link.rest.rest, val)
        # return link
    else:
        duplicate_link(link.rest, val)
        # return link
    '''


def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    # iteration
    lst = []
    # 如果 link 是 empty，則 return [] 一開始寫錯的地方是把 link 寫成 link.rest
    while link != Link.empty:
        lst.append(link.first)
        link = link.rest
    return lst

    # recursive
    # if link == Link.empty:
    #    return []
    # else:
    #    return [int(link.first)] + convert_link(link.rest)


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3))
    >>> b = Link(5, Link(4))
    >>> p1 = multiply_lnks([a, b])
    >>> p1
    Link(10, Link(12))

    >>> c = Link(2, Link(3, Link(5)))
    >>> d = Link(6, Link(4, Link(2)))
    >>> e = Link(4, Link(1, Link(0, Link(2))))
    >>> p2 = multiply_lnks([c, d, e])
    >>> p2
    Link(48, Link(12, Link(0)))
    """
    # 1. How can i multiply all of the First nodes together?
    # 2. How should I use PRODUCT?
    # 3. What is my recursive call? (i.e. how cna i build the rest of the linked list?)
    # 4. How should I handle linked lists with different lengths? Could this server as a base case?
    product = 1
    for lnk in lst_of_lnks:
        if lnk == Link.empty:
            return Link.empty
        product *= lnk.first
    # 要取 lnk.rest，可以用下方的 code 操作
    lst_of_lnks_rests = [lnk.rest for lnk in lst_of_lnks]
    return Link(product, multiply_lnks(lst_of_lnks_rests))


class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
