# Regex

## Symbols
| Symbol | Description |
| ------ | ----------- |
| \d     | Matches digit characters |
| \D     | Matches non digit characters |

## Modifiers
| Modifier | Description |
| -------- | ----------- |
| re.I     | Case Insensitive Matching |
| re.L     | Interprets according to current locale. Affects \w, \W, \b, \B |
| re.M     | Makes $ and ^ match the beginning and end of lines instead of strings |
| re.S     | Makes the period symbol match any character including newline characters |
| re.U     | Interpretes accoring to Unicode character set. Affects \w, \W, \b, \B |
| re.X     | Beautifies regex syntax. Ignores white space unless inside of [] or when escaped with a backslash and treats unescaped # as a comment marker.|

## Look Ahead
```python
regex = r'\d* (?=\s*Hour)'
text = "7 Hours"
re.findall(regex, txt)
> ['7']
```
