# Aye-P

## Description

Aye-P takes in one file of line seperated IPv4 adresses and sorts it to one file of single IP addresses per line.

Aye-P can take the following format of IP addresses:
- 127.0.0.1 (singular)
- 127.0.0.1/32 (CIDR)
- 127.0.0.1-127.0.0.255 (Range)

I made this due to recieving a number of IP ranges in various formats for jobs that were a bit ridiculous. This will help speed up future jobs if this occurs again.

---

## Usage

### The following file is an example of the inputs Aye-P can take in:

[![IP Address File Start](https://i.imgur.com/hkmTLOJ.png)]()

### The following shows the program running:

![imgur GIF](https://i.imgur.com/SuIhjKY.gif)

### The following shows the output file:

[![IP Address File Complete](https://i.imgur.com/Mfu9Xd9.png)]()

---

## Requirements

- Python3 (unix system)
- Uses the following modules which are built in to Python3: ipaddress, os and re.

---

## Disclaimer

- Im terrible at coding in general
- This works for what I need it to do
- Can it be improved? 110%
- Hopefully it helps some of you (If anyone ever uses it)
