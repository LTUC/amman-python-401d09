from randomizer import GameLogic
import pytest

# def test_role_dice_one():
#     actual = GameLogic.role_dic(1)
#
#     assert len(actual) == 1
#
#     for i in actual:
#         assert 1 <= i <= 6
#
# def test_role_dice_two():
#     actual = GameLogic.role_dic(2)
#
#     assert len(actual) == 2
#
#     for i in actual:
#         assert 1 <= i <= 6
#
# def test_role_dice_three():
#     actual = GameLogic.role_dic(3)
#
#     assert len(actual) == 3
#
#     for i in actual:
#         assert 1 <= i <= 6

@pytest.mark.parametrize(
    "test_input, expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ]
)
def test_role_dice(test_input, expected):
    actual = GameLogic.role_dic(test_input)

    assert len(actual) == expected

    for i in actual:
        assert 1 <= i <= 6