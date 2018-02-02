class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fnc_name, typ, time = log.split(':')
            fnc_name, time = int(fnc_name), int(time)

            if typ == 'start':
                if stack:
                    ans[stack[-1]] += time - prev_time
                stack.append(fnc_name)
                prev_time = time
            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans