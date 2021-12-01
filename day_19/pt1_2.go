package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func parseInput(filename string) ([]string, []string, error) {

	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return []string{}, []string{}, err
	}

	splitten := strings.Split(string(data), "\n\n")
	msgs := strings.Split(splitten[0], "\n")
	rules := strings.Split(splitten[1], "\n")

	return msgs, rules, nil
}

func main() {
	fmt.Println("Hello world!")

	msgs, rules, err := parseInput("d19input.txt")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(msgs, "\n", rules)
}
