## Setup

```bash
# Run the docker compose file
docker compose up
```

> Now go to localhost:3000 and create a new user and login.
> Now you will see the Langfuse dashboard.
> Create a new project and add the following environment variables in the env file from the project settings page:
> - LANGFUSE_SECRET_KEY
> - LANGFUSE_PUBLIC_KEY
> - LANGFUSE_HOST

### Required Files

We have to make a json file called `questions.json` with the following format:

```json
[
    <List of Questions>
]
```
example:

```json
[
    "What is the capital of France?",
    "What is the capital of Germany?"
]
```


Now create a new file called `guidelines.txt` and add the guidelines for the llm answer for the questions in the `questions.json` file:

Example:
```txt
- The answer should not be more than 100 words.
- The answer should be always in an authoritative tone.
```

## Run the tests

```bash
python3 runner.py
```

Now go to the Langfuse dashboard and you will see the test run.
Click on the test run and you will see the questions and the llm answers.
You can also see the evaluation of the answers by the evaluator.

### Evaluation

The evaluation is done by the `evaluator.py` file.
The evaluator uses the LLM to evaluate the answers.

You will see the evaluation prompt in that file which can always be changed according to the requirements.

Evaluations returns a boolean value(0-1) and a reason for the evaluation.

### Problems

- The evaluator is not always correct.
- There is no sdk function to delete a dataset.
- The dataset name is hardcoded in the `runner.py` file.