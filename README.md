# PyAction
### Python-based CLI tool
<br>

![Workflow Status](https://img.shields.io/github/workflow/status/varun-charan/pyaction/build-push-pyaction-package?label=build-push-pyaction-package)
![Latest Release](https://img.shields.io/github/v/release/varun-charan/pyaction?label=latest%20release)
![Release Date](https://img.shields.io/github/release-date/varun-charan/pyaction)
[![GitHub issues](https://img.shields.io/github/issues/varun-charan/pyaction)](https://github.com/varun-charan/pyaction/issues)
[![Open Pull Requests](https://img.shields.io/github/issues-pr-raw/varun-charan/pyaction)](https://github.com/varun-charan/pyaction/pulls)


## Usage
```yaml
jobs:
  exec_command:
    runs-on: ubuntu-latest
    steps:
    - name: Test pyaction with exec devops cli command
      uses: varun-charan/pyaction@v0.3.0
      with:
        index_url_pip: ${{ secrets.INDEX_URL_PIP }}
        command: "exec"
        args: "python3 --version"

  non_exec_command:
    runs-on: ubuntu-latest
    steps: 
    - name: Test pyaction with non-exec devops cli command
      uses: varun-charan/pyaction@v0.3.0
      with:
        index_url_pip: ${{ secrets.INDEX_URL_PIP }}
        command: "cheeseshop"
        subcommand: "server-up"
        args: "-t devops"
        
  non_exec_command_output:
    runs-on: ubuntu-latest
    outputs:
      stdout: ${{ steps.pyaction_capture_cmd_output.outputs.stdout }}
    steps:
    - name: Test pyaction with non-exec devops cli command
      id: pyaction_capture_cmd_output
      uses: varun-charan/pyaction@v0.4.0
      env:
        VAULT_ADDR: ${{ secrets.VAULT_ADDR }}
        VAULT_TOKEN: ${{ secrets.VAULT_TOKEN }}
      with:
        index_url_pip: ${{ secrets.INDEX_URL_PIP }}
        export_list: "VAULT_ADDR=${{ env.VAULT_ADDR }}, VAULT_TOKEN=${{ env.VAULT_TOKEN }}"
        command: "vault"
        subcommand: "get"
        args: "prd/devops/newreleases automation_api_key"
```

## Development
- All source code is kept under `src/devops` folder.
- Workflow to create the latest package version and push it to private Python index: `.github/workflows/build-publish.yaml`.
