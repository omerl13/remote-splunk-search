# Remote Splunk Search
## Search over a remote Splunk server
This app lets you run a Splunk search on a remote Splunk server within your own Splunk server

## Examples

Basic usage:
```
| remote host="mysplunk2.com" query="index=main | head 50 | table _time host _raw"
```

## Options
- <b>`host`</b> <i>(required)</i>: Remote Splunk hostname
- <b>`query`</b> <i>(required)</i>: SPL query to run on the remote server
- <b>`username`</b> <i>(required)</i>: Username for authentication
- <b>`password`</b> <i>(required)</i>: Password for authentication
- <b>`port`</b> <i>(optional)</i>: Splunk API port (Default to 8089)
