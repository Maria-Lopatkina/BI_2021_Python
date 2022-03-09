"""
Решила добавить проверку того, чем мы инициализируем экземпляр класса
(проверять нуклеотиды в составе последовательности). Но, поскольку методы
класса ДНК используются экземплярами класса РНК с помощью composition,
то возникала пробела: те последовательности, которые прошли проверку как
РНК - проходили повторную проверку как ДНК, и, если там был урацил -
возникала ошибка.

Я вижу несколько решений в данной ситуации:
1) не наследоваться и не использовать делегирование совсем;
2) не инициировать строкой, а задать с помощью "set...", и там выполнить
проверку. Но тогда у нас уже будет создан какой-то "пустой" экземпляр класса;
3) не делать проверку (не хотелось бы);
4) воспользоваться костылем: ввести дополнительный аргумент по умолчанию
"rna = False" для экземпляра класса ДНК и "rna = True" - для РНК. Когда
будет создан экземпляр класса РНК, мы обратимся к методам класса ДНК через
"self.obj_dna = Dna(sequence, rna=True)", и проверка в __init__ в классе
ДНК проведена не будет.

Хотя теперь я думаю, это как-то странно использовать __hash__ другого класса,
но использовать свой __eq__ (аналогично с чужим __next__ и своим __iter__)
"""

from typing import Any


class Dna:
    def __init__(self, sequence, rna=False):
        self.init_sequence = sequence
        self.sequence = sequence.upper()
        self.cur_index = 0
        self.stop = len(sequence)
        dna_bases = ["A", "T", "G", "C", "N"]
        if not rna:
            for el in range(len(sequence)):
                if self.sequence[el] not in dna_bases:
                    print(f"'{self.init_sequence}' is not a DNA sequence")
                    raise Exception("Unknown sequence")

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_index < self.stop:
            temp = self.init_sequence[self.cur_index]
            self.cur_index += 1
            return temp
        raise StopIteration

    def __eq__(self, other: Any):
        if not isinstance(other, Dna):
            return NotImplemented
        return self.sequence == other.sequence

    def __hash__(self):
        return hash(self.sequence)

    def gc_content(self):
        counter = 0
        n_counter = 0
        for el in self.sequence:
            if el == "C" or el == "G":
                counter += 1
            if el == "N":
                n_counter += 1
        gc_cont = round(counter / len(self.sequence), 2)
        if n_counter > 0:
            return "Unable to calculate GC-content: of N-bases existence"
        else:
            return f"GC-content of {self.init_sequence} is {gc_cont}"

    def reverse_complement(self):
        rev_seq = self.sequence[::-1]
        rev_init_seq = self.init_sequence[::-1]
        rev_com_seq = []
        bases = {"A": ["T", "t"],
                 "T": ["A", "a"],
                 "G": ["C", "c"],
                 "C": ["G", "g"],
                 "U": ["A", "a"],
                 "N": ["N", "n"]}
        for el in range(len(self.sequence)):
            for base in bases.keys():
                if rev_seq[el] == base:
                    if rev_init_seq[el].isupper():
                        rev_com_seq.append(bases[base][0])
                    else:
                        rev_com_seq.append(bases[base][1])
        rev_com_seq = "".join(rev_com_seq)
        return f"Reverse complement of {self.init_sequence} is {rev_com_seq}"

    def transcribe(self):
        tran_seq = []
        bases = {"A": ["U", "u"],
                 "T": ["A", "a"],
                 "G": ["C", "c"],
                 "C": ["G", "g"],
                 "N": ["N", "n"]}
        for el in range(len(self.sequence)):
            for base in bases.keys():
                if self.sequence[el] == base:
                    if self.init_sequence[el].isupper():
                        tran_seq.append(bases[base][0])
                    else:
                        tran_seq.append(bases[base][1])
        tran_seq = "".join(tran_seq)
        return Rna(tran_seq, rna=True)


class Rna:
    def __init__(self, sequence, rna=True):
        self.obj_dna = Dna(sequence, rna=True)
        self.init_sequence = sequence
        self.sequence = sequence.upper()
        self.cur_index = 0
        self.stop = len(sequence)
        rna_bases = ["A", "U", "G", "C", "N"]
        if rna:
            for el in range(len(sequence)):
                if self.sequence[el] not in rna_bases:
                    print(f"'{self.init_sequence}' is not an RNA sequence")
                    raise Exception("Unknown sequence")

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj_dna.__next__()

    def __eq__(self, other: Any, rna=True):
        if not isinstance(other, Rna):
            return NotImplemented
        return self.sequence == other.sequence

    def __hash__(self):
        return self.obj_dna.__hash__()

    def gc_content(self):
        return self.obj_dna.gc_content()

    def reverse_complement(self):
        return self.obj_dna.reverse_complement()


"""
# Test DNA sequences
# dseq1 = Dna("Hello!")

dseq2 = Dna("ccATCG")
dseq3 = Dna("CCATCG")
dseq4 = Dna("accnn")

assert iter(dseq2) is dseq2

print(next(dseq2))
print(next(dseq2))
print(next(dseq2))
print(next(dseq2))
print(next(dseq2))
print(next(dseq2))
# print(next(dseq2))

print(dseq2 == dseq3)
print(dseq2 == dseq4)

dna_seq_set = set()
dna_seq_set.add(dseq2)
dna_seq_set.add(dseq3)
dna_seq_set.add(dseq4)
print(len(dna_seq_set))

print(dseq2.gc_content())

print(dseq2.reverse_complement())


dseq5 = Dna("AAACCC")
rseq5 = dseq5.transcribe()
print(rseq5.sequence)

# Test RNA sequences
# rseq1 = Rna("Hello!")

rseq2 = Rna("AUAUcgg")
rseq3 = Rna("auaucgg")
rseq4 = Rna("auucgg")

assert iter(rseq2) is rseq2

print(next(rseq2))
print(next(rseq2))
print(next(rseq2))
print(next(rseq2))
print(next(rseq2))
print(next(rseq2))
print(next(rseq2))

print(rseq2 == rseq3)
print(rseq2 == rseq4)

dna_seq_set = set()
dna_seq_set.add(rseq2)
dna_seq_set.add(rseq3)
dna_seq_set.add(rseq4)
print(len(dna_seq_set))

print(rseq2.gc_content())

print(rseq2.reverse_complement())
"""
