def convert_link(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """

    # iterative approach
    # unlinked = []
    # while link:
    #     unlinked += [link.first]
    #     link = link.rest
    # return unlinked

    # recursive approach
    # base case - link is empty
    if link is Link.empty:
        return []
    # recursive case - link is not empty
    else:
        return [link.first] + convert_link(link.rest)


def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    # base case - n has only digit - ie we've reached the end!
    if n < 10:
        return Link(n)

    # recursive case - n has > 1 digit - ie more to go still
    else:
        power = 1
        while n // (power * 10) > 0:
            power *= 10

        return Link(n // power, rest = store_digits(n % power))


def every_other(link):
    """Mutates a linked list so that all the odd-indexed elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    # base case - link has 'length' 0 or 1 - do nothing, you're done!
    if link is Link.empty or link.rest is Link.empty:
        return
    # recursive case - else - 'skip' (make link.rest = link.rest.rest) and recur new link.rest
    else:
        if link.rest is not Link.empty:
            link.rest = link.rest.rest
        return every_other(link.rest)

def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> link1
    Link(9, Link(Link(16), Link(25, Link(36))))
    """
    # if link.first is Link, recur
    if isinstance(link.first, Link):
        deep_map_mut(fn, link.first)
    # else, apply fn to first, then recur
    else:
        link.first = fn(link.first)
        deep_map_mut(fn, link.rest)


class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
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
