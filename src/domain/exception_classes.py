class IdAlreadyInRepositoryException(Exception):
    pass

class IdNotInRepositoryException(Exception):
    pass

class DuplicateKeyException(Exception):
    pass

class ElementNotInListException(Exception):
    pass

class CannotUndoException(Exception):
    pass

class CannotRedoException(Exception):
    pass
