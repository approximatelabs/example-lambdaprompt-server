# example-lambdaprompt-server

This is a minimal example of a server repo that can host prompts made with lambdaprompt

This repo only contains 20 lines of python! That's how easy it is~

## How to use

1. Clone this repo
2. `cp .env.example .env` and fill in the API keys
3. Run `pip install -r requirements.txt`
4. Run `./run.sh`
5. Browse to `http://localhost:1234/docs` to see the API docs for the prompts!

Use the prompts using your favorite way to send requests!

Direct browser, `curl`, postman, `requests`, `fetch`, etc.


## How to add a prompt

1. Create a new file in the `prompts` directory
Add any prompts using `lambdaprompt`

