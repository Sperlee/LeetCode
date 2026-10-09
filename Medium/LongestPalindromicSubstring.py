
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        inicio = 0
        tamanho_max = 1

        for i in range(len(s)):
            esquerda = i
            direita = i

            while (
                esquerda >= 0
                and direita < len(s)
                and s[esquerda] == s[direita]
            ):
                tamanho = direita - esquerda + 1

                if tamanho > tamanho_max:
                    inicio = esquerda
                    tamanho_max = tamanho

                esquerda -= 1
                direita += 1


            esquerda = i
            direita = i + 1

            while (
                esquerda >= 0
                and direita < len(s)
                and s[esquerda] == s[direita]
            ):
                tamanho = direita - esquerda + 1

                if tamanho > tamanho_max:
                    inicio = esquerda
                    tamanho_max = tamanho

                esquerda -= 1
                direita += 1

        return s[inicio:inicio + tamanho_max]