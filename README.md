# DeadDNS
**DNS hijacking** via **dead records** automation tool

Tool is based on the *dig* command and it works by:
```
1) Dig provided subdomains file for dead DNS records.
2) Dig the found dead DNS records for any interesting CNAME's. 
3) Show which dead record points to the given CNAME.
```

## Installation:

Simple and quick installation:
```
$ git clone https://github.com/DreyAnd/DeadDNS.git
$ cd DeadDNS
$ pip3 install -r requirements.txt
$ python3 dead_records.py -h
```

## Usage:

```
$ python3 dead_records.py -w subdomains.txt
```
This will return all output to stdout without saving it.

To save all output:

```
$ python3 dead_records.py -w subdomains.txt -o1 found-dead.txt -o2 found-cnames.txt
```

## TO DO:

Make the script run faster :( 
*multithreading here we go*
