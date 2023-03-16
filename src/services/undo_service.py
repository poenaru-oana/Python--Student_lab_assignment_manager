from domain.exception_classes import *


class UndoableOperation:
    def __init__(self, undo_function, redo_function):
        self.undo_function = undo_function
        self.redo_function = redo_function


class UndoService:
    __undo_stack = []
    __undo_pointer = 0

    @staticmethod
    def register_operation(operation):
        UndoService.clear_redo_operations()
        UndoService.__undo_stack.append(operation)
        UndoService.__undo_pointer += 1

    @staticmethod
    def clear_redo_operations():
        while len(UndoService.__undo_stack) != UndoService.__undo_pointer:
            UndoService.__undo_stack.pop()

    @staticmethod
    def undo():
        if UndoService.__undo_pointer == 0:
            raise CannotUndoException("No operations to undo")
        UndoService.__undo_pointer -= 1
        UndoService.__undo_stack[UndoService.__undo_pointer].undo_function()

    @staticmethod
    def redo():
        if UndoService.__undo_pointer == len(UndoService.__undo_stack):
            raise CannotRedoException("No operations to redo")
        UndoService.__undo_stack[UndoService.__undo_pointer].redo_function()
        UndoService.__undo_pointer += 1
