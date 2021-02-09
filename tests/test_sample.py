import os


def test_sample():
    env_var_sample = os.environ["ENV_TEST"]

    print(env_var_sample)

    assert env_var_sample == "test"
