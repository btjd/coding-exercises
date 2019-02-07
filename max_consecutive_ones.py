def max_consecutive_ones(nums):
    if nums == []:
        return 0
    else:
        sequence_lengths = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                i += 1
            else:
                cons_count = 0
                while i < len(nums) and nums[i] == 1:
                    cons_count += 1
                    i += 1
                sequence_lengths.append(cons_count)
        if not sequence_lengths:
            return 0
        else:
            return max(sequence_lengths)

def test_max_consecutive_ones():
    assert max_consecutive_ones([1,0,1,1,0,1]) == 2
    assert max_consecutive_ones([]) == 0
    assert max_consecutive_ones([0,0]) == 0
    assert max_consecutive_ones([1,1,0,1,1,1]) == 3