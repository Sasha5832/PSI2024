from unittest.mock import Mock

mock5 = Mock()

mock5.get_data.return_value = "dane"
mock5.get_data.return_value = 123
mock5.get_data.return_value = True
mock5.get_data.side_effect = ["dane", 123, True]

# Automatyczne tworzenie zagnieżdżonych mocków
nested_mock = Mock()
nested_mock.outer.inner.method.return_value = "zagnieżdżona wartość"
# Konfiguracja wielu atrybutów jednocześnie
complex_mock = Mock()
complex_mock.configure_mock(
**{
'attr1': "wartość 1",
'attr2.method1.return_value': "wynik metody 1",
'attr2.method2.side_effect': [10, 20, 30]
}
)
