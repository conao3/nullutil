"""Nullutil: nullutil for Python."""


# Null Coalesce
# This means:
#     lhs ?? rhs
def qq(lhs, rhs):
    return lhs if lhs is not None else rhs


# Safty Access
# This means:
#     instance?.member
#     instance?.member(*params)
def q_(instance, member, params=None):
    if instance is None:
        return None
    else:
        m = getattr(instance, member)
        if params is None:
            return m
        elif isinstance(params, dict):
            return m(**params)
        elif isinstance(params, list) or isinstance(params, tuple):
            return m(*params)
        else:
            return m(params)
# This means:
#     instance?[index]
def qL7(collection, index):
    return collection[index] if collection is not None else None


# Safety Evalate (do Syntax)
# This means:
#     params?.let{expression}
#     do
#         p0 <- params[0]
#         p1 <- params[1]
#         ...
#         return expression(p0, p1, ...)
def q_let(params, expression):
    if isinstance(params, dict):
        for param in params.values():
            if param is None:
                return None
        return expression(**params)
    elif isinstance(params, list) or isinstance(params, tuple):
        for param in params:
            if param is None:
                return None
        return expression(*params)
    else:
        return expression(params) if params is not None else None
