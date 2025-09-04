class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for i in range(0,len(address),1):
            if(address[i] == "."):
                ans += "[.]"
            else:
                ans += address[i]
        return ans
        