"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Compute all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    FIXME: do you want more tests here?
    """
    return [x[i:i+k] for i in range(0, len(x) - k+1)]


def unique_kmers(x: str, k: int) -> list[str]:
    """
    Compute all unique k-mers of x.
    >>> unique_kmers("agtagtcg", 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']
    
    FIXME: do you want more tests here?
    """
    unique_kmers = {}
    for i in range(0, len(x) - k+1):
        unique_kmers[(x[i:i+k])] = 1
    return list(unique_kmers)


def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Compute all k-mers of x and count how often they appear.
    >>> count_kmers("agtagtcg", 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}

    FIXME: do you want more tests here?
    """
    kmers_dict = {}
    for i in range(0, len(x) - k+1):
        if x[i:i+k] not in kmers_dict:
            kmers_dict[(x[i:i+k])] = 1
        else:
            kmers_dict[(x[i:i+k])] += 1
    return dict(sorted(kmers_dict.items(), key = lambda val:val[1], reverse = True))
