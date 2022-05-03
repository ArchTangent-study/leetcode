# type: ignore
class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        iter_limit = n + 1

        for i in range(0, min(4, iter_limit)):
            count = 0
            # Inner copy of i for use in the loop
            inner_i = i  
            while inner_i != 0:
                count += inner_i & 1 
                inner_i >>= 1

            answer.append(count)

        for i in range(4, min(8, iter_limit)):
            answer.append(answer[i - 4] + 1)

        for i in range(8, min(16, iter_limit)):
            answer.append(answer[i - 8] + 1)

        for i in range(16, min(32, iter_limit)):
            answer.append(answer[i - 16] + 1)

        for i in range(32, min(64, iter_limit)):
            answer.append(answer[i - 32] + 1)

        for i in range(64, min(128, iter_limit)):
            answer.append(answer[i - 64] + 1)

        for i in range(128, min(256, iter_limit)):
            answer.append(answer[i - 128] + 1)

        for i in range(256, min(512, iter_limit)):
            answer.append(answer[i - 256] + 1)

        for i in range(512, min(1024, iter_limit)):
            answer.append(answer[i - 512] + 1)

        for i in range(1024, min(2048, iter_limit)):
            answer.append(answer[i - 1024] + 1)

        for i in range(2048, min(4096, iter_limit)):
            answer.append(answer[i - 2048] + 1)

        for i in range(4096, min(8192, iter_limit)):
            answer.append(answer[i - 4096] + 1)

        for i in range(8192, min(16384, iter_limit)):
            answer.append(answer[i - 8192] + 1)        

        for i in range(16384, min(32768, iter_limit)):
            answer.append(answer[i - 16384] + 1)

        for i in range(32768, min(65536, iter_limit)):
            answer.append(answer[i - 32768] + 1)

        for i in range(65536, min(131072, iter_limit)):
            answer.append(answer[i - 65536] + 1)

        return answer  
    