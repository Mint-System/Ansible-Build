Read the `AGENTS.md` and `README.md` to get an understanding of the project.

I want you to create new role "Open WebUI". Use the `posgres` role as template. 
Configure the Docker image `ghcr.io/open-webui/open-webui:v0.7.0`. Ensure at least these variables can be configured:

- `image`
- `description`
- `hostname`
- `volume_name`

Create variables for these env vars:

- `OAUTH_CLIENT_ID`
- `OAUTH_CLIENT_SECRET`
- `OPENID_PROVIDER_URL`

---

I want you deploy the container to localhost. Update the `inventory` and the `localhost.yml` playbook. Checkout the `task` script. Run the `task play` command to deploy to localhost. Create a new hostname `chatgpt.local` and setup a nginx config.
