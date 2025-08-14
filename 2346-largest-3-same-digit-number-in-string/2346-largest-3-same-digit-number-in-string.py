class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        max_num = ""
        for i in range(len(num) - 2):
            substring = num[i:i+3]
            if substring[0] == substring[1] == substring[2]:
                if substring > max_num :
                    max_num = substring
        
        return max_num