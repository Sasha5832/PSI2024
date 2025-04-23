from unittest.mock import Mock

mock1 = Mock(name="Mock1")
mock1.get_data.return_value = "dane"
result = mock1.get_data("user")
#print(result)
result2 = mock1.get_data(123)
mock1.get_data.assert_called_with(123)
print(mock1.get_data.called)
print(mock1.get_data.call_args)
print(mock1.get_data.call_args_list)
