# lolc0ded
This challenge requires participants to identify the existence of a relative path traversal vulnerability caused by poor implementation of a relative path traversal prevention filter.

## Question Text
```
$ curl http://play.spgame.site:13337/README.lol
HAI 1.337
    CAN HAS STDIO?
    I HAS A file ITZ I IZ STDIO'Z OPEN YR "README.lol" AN YR "r" MKAY
    VISIBLE I IZ STDIO'Z LUK YR file AN YR 13337 MKAY

    OBTW
       Flag is at /home/lolc0ded/flag.lol.
    TLDR
KTHXBYE
```
The service is running at http://play.spgame.site:13337/.
Feel free to check out http://play.spgame.site:13337/index.lol to learn more about lolc0ded.

*Creator -  Ngo Wei Lin (@Creastery)*

## Setup Guide
Docker image is available in the [./service](./service) directory.
Simply execute `./dockerbuild.sh && ./dockerrun.sh`, and service will be available on port `13337`.

## Solution
From the hints in the changelog of http://play.spgame.site:13337/index.lol, HTTP requests can be crafted to gather more information about how the server handle the requests.  
When fuzzing the error pages, it is clear that the URL displayed in the webpage may sometimes differ from the original URL requested.

The below observations can be drawn from the path requested displayed in HTTP 404 and HTTP 405 errors.
> 1. Trailing slash in the path requested is not permitted.
(e.g.: http://play.spgame.site:13337//home/lolc0ded/flag.lol will not yield the flag)
> 2. `../` sequence appears to be filtered
(e.g.: http://play.spgame.site:13337/../ causes the path requested to displayed on the error page as `/`)
> 3. URL decoding is not performed on the path requested
(e.g.: http://play.spgame.site:13337/%3Cscript%3E causes the path requested to displayed on the error page as `/%3Cscript%3E`)

Absolute path traversal is prevented by forbidding trailing slash in the path requested, and the absence of URL decoding implies that double decoding attacks do not work in assisting in relative path traversal.

However, the `../` sequence filter does not appear to be applied recursively, allowing the user to obtain `../` in the resulting string after the filter is applied by placing the `../` sequence within itself (i.e.: `....//` becomes `../` after filtering).

Below is a sample HTTP request to obtain the flag.

```
$ nc 127.0.0.1 13337
GET /....//....//....//home/lolc0ded/flag.lol HTTP/1.1
HTTP/1.3337 200 OK
Connection: close
Server: lolc0ded/1.3337 (Ubuntu) lci/0.11.2
X-Powered-By: lci/0.11.2
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Content-Type: text/html; charset=UTF-8
Content-Length: 40

GCTF{d0nT_c0d3_L0nG_COd3_uS1Ng_L0LcOd3}
```