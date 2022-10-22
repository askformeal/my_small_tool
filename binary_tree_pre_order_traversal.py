def pre_order_traversal(head):
    if head is None:
        return []

    return [head.name]+pre_order_traversal(head.left)+pre_order_traversal(head.right)
