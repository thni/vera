# No trailing whitespace
import re

strictMode = vera.getParameter("strict-trailing-space", "0")

for sourceFileName in vera.getSourceFileNames():
    lineNumber = 1
    previousIndent = ""
    for line in vera.getAllLines(sourceFileName):
        if re.compile("^.*\r$").match(line):
          vera.report(sourceFileName, lineNumber, "CRLF line ending")
          line = line[:-1]
        if re.compile("^.*\s+$").match(line):
            if strictMode or line.strip() or line != previousIndent:
                vera.report(sourceFileName, lineNumber, "trailing whitespace")

        obj = re.compile("^(?P<previousIndent>\s*).*$").match(line)
        previousIndent = obj.groupdict()["previousIndent"]
        lineNumber += 1
