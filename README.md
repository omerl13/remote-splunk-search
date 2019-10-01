# Remote Splunk Search
## Search over a remote Splunk server
This app lets you run a Splunk search on a remote Splunk server within your own Splunk server

## Examples

### Using credentials:
```
| remote host="mysplunk2.com" query="index=main | head 50 | table _time host _raw" username="user" password="changeme"
```

### Using token:
```
| remote host="mysplunk2.com" query="index=main | head 50 | table _time host _raw" token="sometokengeneratedbysplunkstartingv7.3"
```

### Using a generating command
```
| remote host="mysplunk2.com" query="| makeresults count=10" token="sometokengeneratedbysplunkstartingv7.3"
```

## Options
- <b>`host`</b> <i>(required)</i>: Remote Splunk hostname
- <b>`query`</b> <i>(required)</i>: SPL query to run on the remote server
- <b>`username`</b> <i>(optional)</i>: Username for authentication
- <b>`password`</b> <i>(optional)</i>: Password for authentication
- <b>`token`</b> <i>(optional)</i>: Splunk token for authentication
- <b>`port`</b> <i>(optional)</i>: Splunk API port (Default to 8089)

* NOTE: Credentials should be supplied as `username` & `password` OR `token`