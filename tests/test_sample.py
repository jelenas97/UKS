import os


def test_sample():
    env_var_sample = os.environ["SQL_USER"]

    print(env_var_sample)

    assert env_var_sample == "uks_tim_10"
