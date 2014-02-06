CC=gcc

all: map_construct

map_construct:	map_construct.o
	gcc -o $@ $^ -g

map_construct.o: map_construct.c
	gcc -c $<

clean:
	rm *.out
