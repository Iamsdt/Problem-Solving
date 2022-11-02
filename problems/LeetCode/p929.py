class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for i in emails:
            if i in unique:
                continue

            email = i.split("@")
            name = email[0]
            name = name.replace(".", "")
            final_name = name.split("+")[0]
            final_mail = final_name+"@"+email[1]
            unique.add(final_mail)


        return len(unique)

    # but what if, we need to solve it manually
    def numUniqueEmails2(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for e in emails:
            i, local = 0, ""
            while e[i] not in ["@", "+"]:
                if e[i] != ".":
                    local += e[i]
                i += 1

            while e[i] != "@":
                i += 1

            domain = e[i+1:]
            unique.add((local, domain))

        return len(unique)


if __name__ == "__main__":
    print(Solution().numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))

