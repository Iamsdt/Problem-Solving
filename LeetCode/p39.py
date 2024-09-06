from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        di = {}
        prefix_sum = [0] * len(candidates)
        for i, v in enumerate(candidates):
            if i == 0:
                prefix_sum[i] = v
            else:
                prefix_sum[i] = v + prefix_sum[i - 1]

        print("Prefix sum", prefix_sum)
        for i in range(len(prefix_sum)):
            if prefix_sum[i] not in di:
                di[prefix_sum[i]] = [i]
            else:
                di[prefix_sum[i]].append(i)

        answer = []
        for key, value in di.items():
            if len(value) > 1 or key == 0:
                if key == target:
                    for val in value:
                        answer.append((0, val))

                    for j in range(len(value)):
                        for k in range(j + 1, len(value)):
                            answer.append((value[j] + 1, value[k]))
                else:
                    for j in range(len(value)):
                        for k in range(j + 1, len(value)):
                            answer.append((value[j] + 1, value[k]))

        return answer


if __name__ == "__main__":
    print(Solution().combinationSum(candidates=[2, 3, 6, 7], target=7))
