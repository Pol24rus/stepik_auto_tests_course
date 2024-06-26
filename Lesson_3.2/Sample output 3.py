# def test_input_text(expected_result, actual_result):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}'

def test_substring(full_string, substring):
    # в случае несовпадения, предоставляет исчерпывающее сообщение об ошибке.
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"