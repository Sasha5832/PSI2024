from unittest.mock import Mock, MagicMock

mock4 = Mock()
magic_mock = MagicMock()


print(hasattr(mock4, "__str__"))
print(hasattr(magic_mock, "__str__"))

print(hasattr(mock4, "__len__"))
print(hasattr(magic_mock, "__len__"))

print(hasattr(mock4, "__add__"))
print(hasattr(magic_mock, "__add__"))

print(hasattr(mock4, "__getitem__"))
print(hasattr(magic_mock, "__getitem__"))

magic_mock.__len__.return_value = 5
magic_mock.__add__.return_value = "wynik dodawania"
magic_mock.__getitem__.side_effect = lambda key: f"wartość dla {key}"
magic_mock.__str__.return_value = "to jest magiczny mock"

print(len(magic_mock))
print(magic_mock + 7)
print(magic_mock[5])


mock_context = MagicMock()
mock_context.__enter__.return_value = "wartość wewnątrz kontekstu"
mock_context.__exit__.return_value = False

with mock_context as context:
    print(context)