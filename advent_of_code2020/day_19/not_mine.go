package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"
	"time"
)

// Computer of the Advent of code 2020 Day 19
type Computer struct {
	messages []string
	AddLoops bool
}

type ruleReference int
type andRuleReference []ruleReference
type orRuleReference []andRuleReference

type charRule struct {
	char string
}

type rule interface {
	validate(value string) (bool, int) // if true, returns the length of the matched string
}

type Input []string
type Result string

var rules map[ruleReference]rule
var rulesRegex map[string]string

func (d *Computer) Part1(input Input) (Result, error) {
	d.parseInput(input)
	count := 0

	for _, message := range d.messages {
		ok, length := rules[0].validate(message)
		if ok && length == len(message) {
			count++
			// // // fmt.Printf("%s is valid\n", message)
		} else {
			// // // fmt.Printf("%s is invalid\n", message)
		}
	}

	return Result(fmt.Sprint(count)), nil
}

// Part2 of Day 19
func (d *Computer) Part2(input Input) (Result, error) {
	regexp0 := d.parseInputAsRegexes(input)

	count := 0

	for _, message := range d.messages {
		// ok, length := rules[0].validate(message)
		// if ok && length == len(message) {
		if regexp0.MatchString(message) {
			count++
			// // // fmt.Printf("%s is valid against %s\n", message, createRegex(rules[0]))
		} else {
			// fmt.Printf("%s is invalid against %v\n", message, regexp0)
		}
	}

	return Result(fmt.Sprint(count)), nil
}

func (d *Computer) parseInputAsRegexes(input Input) *regexp.Regexp {
	rulesRegex = map[string]string{}
	d.messages = []string{}

	for _, line := range input {
		if isRule(line) {
			ref, parsedRule := parseRuleAsRegex(line)
			rulesRegex[ref] = parsedRule
		} else if isMessage(line) {
			d.messages = append(d.messages, line)
		}
	}

	rulesRegex["8"] = "42 +"
	rulesRegex["11"] = "42 (?: 42 (?: 42 (?: 42 (?: 42 (?: 42 (?: 42 (?: 42 (?: 42 (?: 42 (?: 42 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31 )? 31"

	numberReplaceRegex := regexp.MustCompile(`\d+`)

	for {
		done := true

		for k := range rulesRegex {
			rulesRegex[k] = numberReplaceRegex.ReplaceAllStringFunc(rulesRegex[k], func(val string) string {
				done = false
				return rulesRegex[val]
			})
		}

		if done {
			break
		}
	}

	return regexp.MustCompile("^" + strings.ReplaceAll(strings.ReplaceAll(rulesRegex["0"], "\"", ""), " ", "") + "$")
}

func parseRuleAsRegex(line string) (string, string) {
	keyValue := strings.Split(line, ":")
	return keyValue[0], fmt.Sprintf("( %s )", strings.TrimSpace(keyValue[1]))
}

func isMessage(line string) bool {
	res, _ := regexp.MatchString("^(a|b)+$", line)
	return res
}

func isRule(line string) bool {
	res, _ := regexp.MatchString("\\d+: .+", line)
	return res
}

func (r charRule) validate(value string) (bool, int) {
	if value == r.char {
		return true, 1
	}

	return false, -1
}

func (r orRuleReference) validate(value string) (bool, int) {
	for _, rr := range r {
		check, length := rr.validate(value)
		if check {
			return true, length
		}
	}

	return false, -1
}

func (r andRuleReference) validate(value string) (bool, int) {
	fullLength := 0

	for _, rr := range r {
		check, length := rules[rr].validate(value[fullLength : len(value)-fullLength])
		if !check {
			return false, -1
		}

		fullLength += length
	}

	return true, fullLength
}

/*
"0: 4 1 3":     rule0,
"1: 4 4 | 3 3": rule1,
"2: 4 3 | 3 4": rule2,
"3: \"a\"":     rule3,
"4: \"b\"":     rule4,
*/
func (d *Computer) parseInput(input Input) {
	rules = map[ruleReference]rule{}
	d.messages = []string{}

	for _, line := range input {
		if isRule(line) {
			ref, parsedRule := parseRule(line)
			rules[ref] = parsedRule
		} else if isMessage(line) {
			d.messages = append(d.messages, line)
		}
	}
}

func parseRule(line string) (ruleReference, rule) {
	keyValue := strings.Split(line, ":")

	key, _ := strconv.Atoi(keyValue[0])
	value := strings.TrimSpace(keyValue[1])

	var parsedRule rule

	charCheck, _ := regexp.MatchString("^\"a|b\"$", value)

	if charCheck {
		parsedRule = charRule{value[1:2]}
	} else if strings.Contains(value, "|") {
		rules := strings.Split(value, "|")
		parsedRule = orRuleReference{
			parseAndRulesReferences(rules[0]),
			parseAndRulesReferences(rules[1]),
		}
	} else {
		parsedRule = parseAndRulesReferences(value)
	}

	return ruleReference(key), parsedRule
}

func parseAndRulesReferences(ruleset string) andRuleReference {
	refs := andRuleReference{}

	for _, ref := range strings.Split(strings.TrimSpace(ruleset), " ") {
		numericRef, _ := strconv.Atoi(ref)
		refs = append(refs, ruleReference(numericRef))
	}

	return refs
}

func ReadInput(fPath string) Input {
	file, err := os.Open(fPath)
	if err != nil {
		log.Fatal(err)
	}

	defer file.Close()

	res := []string{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		res = append(res, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return res
}

func main() {
	start := time.Now()

	today := &Computer{}

	input := ReadInput("d19input.txt")

	res_pt1, err := today.Part1(input)

	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("\n%s\n", res_pt1)

	// res_pt2, err := today.Part2(input)
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Printf("\n%s\n", res_pt2)

	elapsed := time.Since(start)
	fmt.Printf("\nExecution took %s\n", elapsed)
}
