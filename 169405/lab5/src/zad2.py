from unittest.mock import Mock


mock2 = Mock(autospec=True, name="Mock2")
#mock2.get_data.return_value = "dane"
#mock2.get_data.return_value = 123
#mock2.get_data.return_value = True
mock2.get_data.side_effect = ["dane", 123, True]

print(mock2.get_data(234))
print(mock2.get_data(1232))
print(mock2.get_data(True))


def modify(args):
    return args*2

mock2.get_data.side_effect = modify

print(mock2.get_data(44))
print(mock2.get_data("xewfg"))
mock2.error_method.side_effect = ValueError("Something went wrong")