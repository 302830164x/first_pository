from unittestzero import Assert


class AssertUtils:

    def assert_contains(self, actual, expected):
        """
        断言实际值是否包含预期值
        :param actual:
        :param expected:
        :return:
        """
        if isinstance(expected, tuple) or isinstance(expected, list):
            for val in expected:
                assert val in actual
        else:
            assert expected in actual

    def assert_equals(self, actual, expected):
        """
        判断实际值是否等于预期值
        :param actual:
        :param expected:
        :return:
        """
        assert actual == expected

    def assert_contains_one(self, actual, expected):
        """
        判断实际值是否等于预期值中的一个
        :param actual:
        :param expected:
        :return:
        """
        if isinstance(expected, tuple) or isinstance(expected, list):
            exp = str(expected)
            for val in expected:
                if val in actual:
                    exp = val
            assert exp in str(actual)
        else:
            assert expected in str(actual)

    def assert_greater_equal(self, first, second):
        """断言前面一个数值是否大于等于后面一个数值"""
        Assert.greater_equal(int(first), int(second), f"断言失败，输入参数有误,{first}不大于等于{second}")

    def assert_greater(self, first, second):
        """断言前面一个数值是否大于后面一个数值"""
        Assert.greater(int(first), int(second), f"断言失败，输入参数有误,{first}不大于{second}")

    def assert_less_equal(self, first, second):
        """断言前面一个数字是否小于等于后面一个数值"""
        Assert.less_equal(int(first), int(second), f"断言失败，输入参数有误,{first}不小于等于{second}")

    def assert_less(self, first, second):
        """断言前面一个数字是否小于后面一个数值"""
        Assert.less(int(first), int(second), f"断言失败，输入参数有误,{first}不小于{second}")

    def assert_between_equal(self, first, second, third):
        """断言区间"""
        Assert.greater_equal(int(first), int(second), f"断言失败，输入参数有误,{first}不大于等于{second}")
        Assert.less_equal(int(first), int(third), f"断言失败，输入参数有误,{first}不小于等于{third}")

    def assert_between(self, first, second, third):
        """断言区间"""
        Assert.greater(int(first), int(second), f"断言失败，输入参数有误,{first}不大于{second}")
        Assert.less(int(first), int(third), f"断言失败，输入参数有误,{first}不小于{third}")


assertUtils = AssertUtils()

if __name__ == '__main__':
    assertUtils.assert_between(6, 6, 5)
