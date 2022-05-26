from functools import lru_cache


class Solution:

    def __init__(self):
        self.a = ""
        self.b = ""

    def LCS(self, s1: str, s2: str) -> str:
        # write code here
        self.a = s1
        self.b = s2
        ans = self.dfs(len(s1) - 1, len(s2) - 1)
        if len(ans) == 0:
            ans = "-1"
        return ans

    @lru_cache(None)
    def dfs(self, l1, l2):
        if l1 < 0 or l2 < 0:
            return ""
        c1 = self.a[l1]
        c2 = self.b[l2]

        if c1 == c2:
            res = self.dfs(l1 - 1, l2 - 1) + c1
        else:
            res1 = self.dfs(l1 - 1, l2)
            res2 = self.dfs(l1, l2 - 1)
            res = res1 if len(res1) > len(res2) else res2

        return res


if __name__ == '__main__':
    s = Solution()
    a = "1A2C3D4B56"
    b = "B1D23A456A"
    a = "JGIHa76X06Mx330MtfiNafgpQfj0sJVop2nrMb7Gx2i3RIA72UIIXWA2NoPjRN1jwMNVawJrsn3obxhKDINaHLMJT4JnxHo43xf7CUjh77Pae1UUi3GIiH4ponfV6HRzbk1pp7ehACa2ephI6kVb46FR0irx4tVmDjpks0VRonMe3keeVJ83Z8N2eUJoIN4WGd0GQWDn1jnM4MsojgFIbXs7Nu3jnFHrWi3fbNiWRIfxUzr23yb4NGrj1XhkJMbj42DXeUAeifpMNHFx6AGu962ATDV3kkJfAjeJj4Xs0oxq4pGxm2xrrZf4MGJfin4boMzhNFrYGf3sRpafUXIOUAkfU7bas2pHkViihorlhwd7njxefBMpnCWR4rqX76GrW27R1HIna09Dhkfirtpn1F6A2Gr4rbc3MFrtzVrfCxntVh3nHra0I4xNaWi7bVphjoIiGWhIzoiAfkMMdzyVfQoHAw4Gr4M6CC4TGar118GhJS6GfR6HIopGDpzxmkS11nC4sXxoeaA77bAzWsJJ9W10Xnae4Vk2zIHUxUVJiGr62J1B45NhHp41A726WqJNaI7UbjRr1GkX0jChibFW6Chn1i3boIBpfVAf4Wa37sX4J9CjWrhG174rXixexFs9JAn3NVWGnWokWnCs1jfRI36xiIWfCXUj7bsbKeJtpxri2AzsskRJhUVzaNNA2iHR6iGHI0er34n6axnbrWis6o4H70VipGy7CH5fTqJakNI3MnuRvqbskBX8kXHpAbVNHN07ooGnrPrUCItRoRH1bco4VUVXrxHIoqM6ahzjGFh1h37ibpoXhX00b3iGaxG6XfVVeAVJoKfFVieI6zWrairpCRNRniVr0HWGKNWFRxTxRRGN1xBNXgrreeaNFWpz7637joijexGRAspXnRnQoU6bab4R7afC3C1k3NxiRX72kjARUGeMRMaR6k0wNxHj2kzHWH0XjtkrxJM0IhU4eaohWF8UCpCGjhXeAUse1piLGFl7x2J3VkVVnMr6UhR9nzUF473TNFXip35j3sR4nNws4hzU7p6IWWIR4Nf2Q3yFRf1RUz2sRhJG1aSxaffQAz7apoxIXJaX0nXa6Ffj3IkV0zxjUTVdkGUx"
    b = "K8dqDTE5Z5lgtvv9m9Qg8ugmYu9qDwaDgtKl5vylPLyLPLwlKETQ8v5YvTMwBKQKyT3Pl8tuKvmqgwEOQlx5vZLKgT5ABdw7yqPdZPmcuugDqOZwtNYgLcwBgTrEqlhKummLgmZDcHwcmm5LvmTvDLxlQyttK7DPgTucUq5DdlmKiSE8mBt93tOgTQKTGhCPBDudBLmgPtLvYTuydmcqD5EtEQZmwmmBLc5SEd89TyOlDYdwol8lDZl8cucOB9ggldm5QZPuPl58qttLQDP1TELyMtgggdutTuy9wZL8YwZqvw8EtgqqYK5LvK4yYwjBXSODNcDQHmEE8uvdZP9lQutwPcYyvQSwTLD8PcdgKE5DE89ZqdPBycc5wmQgLZT2B8ZE9wBzE58P9EOqYLTw5OUrSlTQPOqOTqtZBvwOv5yDwSddQY9BTqT8DY59BYQy9gPEl9gLZtEdvLuLByOB9S79DgrBtvZQqmyBr98y9tqc5cTcvP3mt9VE5mtEZuBaivBywYSO59YZEBgyISBYqBl8TZd8vSOETQZy8Qwl8g9BTvKBvS8LQSvYLqD9ZmYgTSQOdStmlqtTROYuOQDPuEuuS8gm5BlmPuEcZSydCc9tggu8cQmmXOxSTEvmBDKtd59LbqLlTPd9EcSKEwVIy58wgBDlwlQxTBTc5KmB8uZSqdjBLBYtmqlmGQKigTcdOmZKgOB9quvgcOWqBwuZmtw5KPZE9LlvtdluoS1SBRZuKQKlmtlsKgw85KuuOBqdKmYcgD8cQPtZLBvtugY5TrEqkvBTllqy5tEiuTZPvTPw7855L9diqEDyygCtmZ5BODKY8OuZSLEuwETZuLQqvTqODuKSy8qDvuRwqS8vEmYmEwmuQqEB8YcdAZEdovySPL8qOt1cKlc9ZluQEctPoLYYw9wOwgEqaZ9uLhuicQxKKEFYEzPc5y5tQdDm8qgODEOPBHDKcFwxTxYtdTBDEcE8yQgqQKggvrOtEjpEPcB9l5LDcPcQbDyyQyTDuwBBtDL5CqS5Ecdg3qTtDDuwmtBdEtLv0ulDOK8EKZiL8wuquS8Zqlmm85wyKSPQmv9uw99PKUQvPTumvdZ5gcLugv95PEcyl88wOtEQBQKZlyPgyY5cgvKvEBRDZcddww8lqSTP9LuPwlSdWymfZQEy2qPDQGvlyumDdSfQgmtOtBEmLvuYww7EKZTZEwumaBSmqP9ga83dTE9LlLEBBdugEvTSKYBDL8ugSy"
    print(s.LCS(a, b))



