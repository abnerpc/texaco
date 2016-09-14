import pytest

from mock import patch

from texaco.core import manager
from texaco.core.exception import ValidateFileLinesFormatException


class TestManager(object):

    @pytest.mark.parametrize('line', [
        ['a'],
        ['1'],
        ['4', 'a'],
        ['4', '1:0'],
        ['4', '-1:0'],
        ['-1', '1:0'],
        ['1', '1:0', '2:1'],
    ])
    def test_invalid_line_is_valid(self, line):
        is_valid = manager.line_is_valid(line)
        assert not is_valid

    @pytest.mark.parametrize('line', [
        ['1', '1:9'],
        ['2', '1:9', '0:0'],
        ['4', '1:9', '3:2', '0:3', '4:6'],
    ])
    def test_valid_line_is_valid(self, line):
        is_valid = manager.line_is_valid(line)
        assert is_valid

    @patch.object(manager, 'line_is_valid')
    def test_validate_file_reader(self, line_is_valid, fake_reader):
        line_is_valid.side_effect = [True, True, True]
        lines = manager.validate_file_reader(fake_reader())
        assert len(lines) == 3

        line_is_valid.reset_mock()
        line_is_valid.side_effect = [True, False, True]
        with pytest.raises(ValidateFileLinesFormatException):
            lines = manager.validate_file_reader(fake_reader())

    @pytest.mark.parametrize('points,start_idx,expected', [
        ([(2, 2), (3, 1)], 1, True),
        ([(1, 3), (2, 5)], 0, False),
        ([(1, 4), (5, 2)], 0, False),
        ([(1, 4), (5, 2)], 1, True),
        ([(1, 2), (1, 2), (3, 1)], 0, False),
        ([(1, 2), (1, 2), (3, 1)], 1, False),
        ([(1, 2), (1, 2), (3, 1)], 2, True),
    ])
    def test_follow_path(self, points, start_idx, expected):
        result = manager.follow_path(points, start_idx)
        assert result == expected

    @pytest.mark.parametrize('entries,expected', [
        (['1:2', '1:3'], 'impossible'),
        (['1:4', '5:2'], '2'),
        (['1:2', '1:2', '3:1'], '3'),
    ])
    def test_get_best_route(self, entries, expected):
        result = manager.get_best_route(entries)
        assert result == expected

    @patch.object(manager, 'get_best_route')
    @patch.object(manager, 'validate_file_reader')
    def test_get_routes_results(self,
                                validate_file_reader,
                                get_best_route,
                                fake_reader):
        get_best_route.side_effect = ['foo', 'bar', 'baz']
        validate_file_reader.return_value = []

        result = manager.get_routes_results([])
        assert result == []
        validate_file_reader.assert_called_with([])
        get_best_route.assert_not_called()

        validate_file_reader.return_value = ['a', 'e', 'i']
        result = manager.get_routes_results(fake_reader())
        assert len(result) == 3
        assert result == ['foo', 'bar', 'baz']
