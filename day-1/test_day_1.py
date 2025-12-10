import pytest
import day_1

@pytest.mark.parametrize("initial_number, dail_rotation, expected_position", [
    (50, "L68", 82),
    (82, "L30", 52),
    (52, "R48", 0),
    (0, "L5", 95),
    (95, "R60", 55),
    (55, "L55", 0),
    (0, "L1", 99),
    (99, "L99", 0),
    (0, "R14", 14),
    (14, "L82", 32),
]) 
def test_dail_turning(initial_number, dail_rotation, expected_position):

    new_position = day_1.rotate(initial_number, dail_rotation)

    assert new_position == expected_position