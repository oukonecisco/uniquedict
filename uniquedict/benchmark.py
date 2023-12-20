import random
import timeit
from typing import Dict

from uniquedict.remove_duplicates import remove_duplicates


def generate_user(_id: int) -> Dict[str, object]:
    """Generates a user dictionary with some random and some fixed data."""
    return {
        "id": _id,
        "name": "User" + str(random.randint(1, 700)),
        "email": f"user{_id}@example.com",
        "age": random.randint(18, 100),
        "is_active": random.choice([True, False]),
        "address": {
            "street": "Street" + str(random.randint(1, 500)),
            "city": "City" + str(random.choice([1, 2, 3])),
            "state": "State" + str(random.randint(1, 50)),
            "zip_code": str(random.randint(10000, 99999)),
        },
    }


def run_benchmark(dataset_size: int, num_duplicates: int):
    # Generate the dataset
    users = [generate_user(i) for i in range(dataset_size)]

    # Introduce duplicates
    if num_duplicates > 0 and num_duplicates <= dataset_size:
        duplicates = random.sample(users, num_duplicates)
        users.extend(duplicates)
    else:
        raise ValueError(
            "Number of duplicates must be between 0 and dataset_size"
        )

    # Measure the execution time using timeit
    stmt = lambda: remove_duplicates(users, "id")
    execution_time = timeit.timeit(stmt, number=1)

    print(
        f"Time taken to remove duplicates from dataset: {execution_time:.4f} seconds"
    )
    print(f"Original users count: {len(users)}")
    print(
        f"Count after removing duplicates: {len(remove_duplicates(users, 'id'))}"
    )


if __name__ == "__main__":
    # Example usage
    run_benchmark(10000000, 300)
