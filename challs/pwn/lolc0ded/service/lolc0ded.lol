HAI 1.3337
    CAN HAS STDIO?
    CAN HAS STRING?

    I HAS A request ITZ ""
    I HAS A requestMethod ITZ ""
    I HAS A requestURL ITZ ""
    I HAS A filepath ITZ ""
    I HAS A response ITZ ""
    I HAS A responseStatusCode ITZ 404
    I HAS A responseStatusName
    I HAS A responseStatusDesc
    I HAS A responseContent ITZ ""

    HOW IZ I toUpper YR char
        char, WTF?
            OMG "a"
                FOUND YR "A"
            OMG "b"
                FOUND YR "B"
            OMG "c"
                FOUND YR "C"
            OMG "d"
                FOUND YR "D"
            OMG "e"
                FOUND YR "E"
            OMG "f"
                FOUND YR "F"
            OMG "g"
                FOUND YR "G"
            OMG "h"
                FOUND YR "H"
            OMG "i"
                FOUND YR "I"
            OMG "j"
                FOUND YR "J"
            OMG "k"
                FOUND YR "K"
            OMG "l"
                FOUND YR "L"
            OMG "m"
                FOUND YR "M"
            OMG "n"
                FOUND YR "N"
            OMG "o"
                FOUND YR "O"
            OMG "p"
                FOUND YR "P"
            OMG "q"
                FOUND YR "Q"
            OMG "r"
                FOUND YR "R"
            OMG "s"
                FOUND YR "S"
            OMG "t"
                FOUND YR "T"
            OMG "u"
                FOUND YR "U"
            OMG "v"
                FOUND YR "V"
            OMG "w"
                FOUND YR "W"
            OMG "x"
                FOUND YR "X"
            OMG "y"
                FOUND YR "Y"
            OMG "z"
                FOUND YR "Z"
            OMGWTF
                FOUND YR char
        OIC
    IF U SAY SO

    HOW IZ I escapeString YR unescapedString
        I HAS A unescapedStringLength ITZ I IZ STRING'Z LEN YR unescapedString MKAY
        I HAS A escapedString ITZ ""

        IM IN YR loop UPPIN YR index TIL BOTH SAEM index AN unescapedStringLength
            I HAS A currentChar ITZ I IZ STRING'Z AT YR unescapedString AN YR index MKAY

            currentChar, WTF?
                OMG "<"
                    escapedString R SMOOSH escapedString AN "&lt;" MKAY
                    GTFO
                OMG ">"
                    escapedString R SMOOSH escapedString AN "&gt;" MKAY
                    GTFO
                OMGWTF
                    escapedString R SMOOSH escapedString AN currentChar MKAY
            OIC
        IM OUTTA YR loop

        FOUND YR escapedString
    IF U SAY SO

    HOW IZ I sanitiseFilepath YR url
        BOTH SAEM url AN "/", O RLY?, YA RLY, responseStatusCode R 200, FOUND YR "", OIC
        BOTH SAEM url AN "//", O RLY?, YA RLY, responseStatusCode R 400, FOUND YR "", OIC

        I HAS A urlLength ITZ I IZ STRING'Z LEN YR url MKAY

        DIFFRINT urlLength AN BIGGR OF urlLength AN 3, O RLY?, YA RLY, FOUND YR I IZ STRING'Z AT YR url AN YR 1 MKAY, OIC

        BTW prevent explicit absolute path traversal
        BOTH SAEM I IZ STRING'Z AT YR url AN YR 1 MKAY AN "/", O RLY?, YA RLY, responseStatusCode R 400, FOUND YR "", OIC

        BTW prevent relative path traversal
        I HAS A sanitisedURL ITZ ""
        IM IN YR loop UPPIN YR index TIL BOTH SAEM index AN BIGGR OF index AN urlLength
            BOTH SAEM index AN 0, O RLY?, YA RLY, index R 1, OIC

            I HAS A firstChar  ITZ I IZ STRING'Z AT YR url AN YR index MKAY
            I HAS A secondChar ITZ I IZ STRING'Z AT YR url AN YR SUM OF index AN 1 MKAY
            I HAS A thirdChar  ITZ I IZ STRING'Z AT YR url AN YR SUM OF index AN 2 MKAY

            sanitisedURL R SMOOSH sanitisedURL AN firstChar MKAY

            BOTH SAEM index AN DIFF OF urlLength AN 2
            O RLY?
                YA RLY
                    sanitisedURL R SMOOSH sanitisedURL AN secondChar AN thirdChar MKAY
                    GTFO
            OIC

            ALL OF BOTH SAEM firstChar AN "." AN BOTH SAEM secondChar AN "." AN BOTH SAEM thirdChar AN "/" MKAY
            O RLY?
                YA RLY
                    index R SUM OF index AN 2

                    I HAS A sanitisedURLLength ITZ I IZ STRING'Z LEN YR sanitisedURL MKAY
                    I HAS A originalSanitisedURL ITZ ""
                    IM IN YR loop2 UPPIN YR index2 TIL BOTH SAEM index2 AN BIGGR OF index2 AN  DIFF OF sanitisedURLLength AN 1
                        I HAS A currentChar ITZ I IZ STRING'Z AT YR sanitisedURL AN YR index2 MKAY
                        originalSanitisedURL R SMOOSH originalSanitisedURL AN currentChar MKAY
                    IM OUTTA YR loop2
                    sanitisedURL R originalSanitisedURL
            OIC
        IM OUTTA YR loop

        BTW prevent implicit absolute path traversal
        I HAS A sanitisedURLLength ITZ I IZ STRING'Z LEN YR sanitisedURL MKAY
        BOTH OF DIFFRINT sanitisedURLLength AN SMALLR OF sanitisedURLLength AN 1 AN BOTH SAEM I IZ STRING'Z AT YR sanitisedURL AN YR 0 MKAY AN "/"
        O RLY?
            YA RLY
                responseStatusCode R 400
        OIC

        FOUND YR sanitisedURL
    IF U SAY SO

    HOW IZ I createResponse
        BOTH SAEM filepath AN "", O RLY?, YA RLY, filepath R I IZ sanitiseFilepath YR requestURL MKAY, OIC

        responseStatusCode, WTF?
            OMG 200
                responseStatusName R "OK"
                GTFO
            OMG 400
                responseStatusName R "Bad Request"
                responseStatusDesc R "Your browser sent a request that this server could not understand."
                GTFO
            OMG 404
                responseStatusName R "Not Found"
                I HAS A escapedRequestURL ITZ SMOOSH "/"...
                                                  AN I IZ escapeString YR filepath MKAY...
                                                MKAY
                responseStatusDesc R "The requested URL :{escapedRequestURL} was not found on this server."
                GTFO
            OMG 405
                responseStatusName R "Method Not Allowed"
                I HAS A escapedRequestMethod ITZ I IZ escapeString YR requestMethod MKAY
                I HAS A escapedRequestURL ITZ SMOOSH "/"...
                                                  AN I IZ escapeString YR filepath MKAY...
                                                MKAY
                responseStatusDesc R "The requested method :{escapedRequestMethod} is not allowed for the URL :{escapedRequestURL}."
                GTFO
        OIC

        responseStatusCode, WTF?
            OMG 400
            OMG 404
            OMG 405
                responseContent R SMOOSH "<!DOCTYPE HTML PUBLIC :"-//IETF//DTD HTML 2.0//EN:">:3:)"...
                              AN "<html><head>:3:)"...
                              AN "<title>:{responseStatusCode} :{responseStatusName}</title>:3:)"...
                              AN "</head><body>:3:)"...
                              AN "<h1>:{responseStatusName}</h1>:3:)"...
                              AN "<p>:{responseStatusDesc}</p>:3:)"...
                              AN "</body></html>"...
                            MKAY
        OIC

        I HAS A responseContentLength ITZ I IZ STRING'Z LEN YR responseContent MKAY

        response R SMOOSH "HTTP/1.3337 :{responseStatusCode} :{responseStatusName}:3:)"...
                       AN "Connection: close:3:)"...
                       AN "Server: lolc0ded/1.3337 (Ubuntu) lci/0.11.2:3:)"...
                       AN "X-Powered-By: lci/0.11.2:3:)"...
                       AN "X-Frame-Options: DENY:3:)"...
                       AN "X-XSS-Protection: 1; mode=block:3:)"...
                       AN "Content-Type: text/html; charset=UTF-8:3:)"...
                     MKAY

        BOTH OF BOTH SAEM responseStatusCode AN 200 AN BOTH SAEM requestMethod AN "OPTIONS"
        O RLY?
            YA RLY
                response R SMOOSH response AN "Allow: GET,HEAD,POST,OPTIONS:3:)" MKAY
        OIC

        response R SMOOSH response AN "Content-Length: :{responseContentLength}:3:):3:)" AN ":{responseContent}" MKAY

        FOUND YR response
    IF U SAY SO

    HOW IZ I parse YR request
        I HAS A requestMethodFound ITZ FAIL
        I HAS A requestLength      ITZ I IZ STRING'Z LEN YR request MKAY

        BOTH SAEM requestLength AN 0, O RLY?, YA RLY, FOUND YR FAIL, OIC

        IM IN YR loop UPPIN YR index TIL BOTH SAEM index AN requestLength
            I HAS A currentChar ITZ I IZ STRING'Z AT YR request AN YR index MKAY

            ALL OF BOTH SAEM currentChar AN " " AN requestMethodFound AN DIFFRINT requestURL AN "" MKAY, O RLY?, YA RLY, GTFO, OIC

            BOTH OF NOT requestMethodFound AN DIFFRINT currentChar AN " "
            O RLY?,
                YA RLY
                    currentChar R I IZ toUpper YR currentChar MKAY
                    requestMethod R SMOOSH requestMethod AN currentChar MKAY
            OIC

            ALL OF requestMethodFound AN BOTH SAEM requestURL AN "" AN DIFFRINT currentChar AN "/" MKAY, O RLY?, YA RLY, GTFO, OIC

            requestMethodFound, O RLY?, YA RLY, requestURL R SMOOSH requestURL AN currentChar MKAY, OIC

            BOTH OF NOT requestMethodFound AN BOTH SAEM currentChar AN " "
            O RLY?,
                YA RLY
                    requestMethodFound R WIN
            OIC
        IM OUTTA YR loop

        BOTH SAEM requestURL AN "", O RLY?, YA RLY, responseStatusCode R 400, FOUND YR FAIL, OIC
        DIFFRINT I IZ STRING'Z AT YR requestURL AN YR 0 MKAY AN "/", O RLY?, YA RLY, responseStatusCode R 400, FOUND YR FAIL, OIC

        requestMethod, WTF?
            OMG "HEAD"
            OMG "OPTIONS"
                responseStatusCode R 200
                FOUND YR FAIL
                GTFO
            OMG "GET"
            OMG "POST"
                GTFO
            OMGWTF
                responseStatusCode R 405
                FOUND YR FAIL
                GTFO
        OIC

        filepath R I IZ sanitiseFilepath YR requestURL MKAY

        BOTH SAEM responseStatusCode AN 400, O RLY?, YA RLY, FOUND YR FAIL, OIC

        I HAS A file ITZ I IZ STDIO'Z OPEN YR filepath AN YR "r" MKAY
        I IZ STDIO'Z DIAF YR file MKAY
        O RLY?
            YA RLY
                responseStatusCode R 404
                FOUND YR FAIL
            NO WAI
                responseContent R I IZ STDIO'Z LUK YR file AN YR 13337 MKAY
                I IZ STDIO'Z CLOSE YR file MKAY

                responseStatusCode R 200
                FOUND YR FAIL
        OIC
    IF U SAY SO

    GIMMEH request
    I IZ parse YR request MKAY
    I IZ createResponse MKAY
    VISIBLE response
KTHXBYE

