import pytest
from GeneticA.individual import Individual


class TestGeneticA:

    @pytest.mark.parametrize('lb', [[0, 0], [0, 0, 0]])
    def test_init(self, lb):

        test_ub = [10, 10]

        if lb == [0, 0]:
            individual = Individual(lb, test_ub)

            assert isinstance(individual.position, list)
            assert len(individual.position) == len(lb) == len(test_ub)
            for i in range(0, len(individual.position)):
                assert individual.position[i] >= lb[i]
                assert individual.position[i] <= test_ub[i]

        elif lb == [0, 0, 0]:
            with pytest.raises(ValueError):
                individual = Individual(lb, test_ub)
