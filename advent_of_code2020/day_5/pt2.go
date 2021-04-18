package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"strings"
)

//  ROW  COL
// XXXXX YYY

type Seat struct {
	row, col int
}

func (s Seat) calcSeatID() int {
	return s.row*8 + s.col
}

func Find(slice []int, val int) bool {
	for _, sval := range slice {
		if val == sval {
			return true
		}
	}

	return false
}

func generateAllIds() []int {
	allIds := make([]int, 0)

	for row := 0; row < 128; row++ {
		for col := 0; col < 8; col++ {
			allIds = append(allIds, row*8+col)
		}
	}

	return allIds
}

func getMax(intLst []int) (highest int) {
	for _, val := range intLst {
		if val > highest {
			highest = val
		}
	}

	return
}

func bin_search(pos []string, chars []string, upperB float64) float64 {
	var lowerB float64

	for _, c := range chars {
		switch c {
		case pos[0]:
			lowerB = (lowerB + upperB) / 2
		case pos[1]:
			upperB = (lowerB + upperB) / 2
		default:
			fmt.Println("\n", c, "?")
		}
	}

	if chars[len(chars)-1] == pos[0] {
		return math.Round(upperB)
	} else {
		return math.Round(lowerB)
	}
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	seatIDS := make([]int, 0)
	cols_pos := []string{"R", "L"}
	rows_pos := []string{"B", "F"}

	dat, err := ioutil.ReadFile("input.txt")
	check(err)

	seatsCode := strings.Split(string(dat), "\n")

	for _, code := range seatsCode[:len(seatsCode)-1] {
		code_b := strings.Split(code, "")

		seatIDS = append(seatIDS, Seat{row: int(bin_search(rows_pos, code_b[:7], 127)), col: int(bin_search(cols_pos, code_b[7:], 7))}.calcSeatID())
	}
	fmt.Println(getMax(seatIDS))

	code_b := []string{"B", "F", "F", "F", "B", "B", "F", "R", "R", "R"}
	// code_b := []string{"F", "F", "F", "B", "B", "B", "F", "R", "R", "R"}
	s := Seat{row: int(bin_search(rows_pos, code_b[:7], 127)), col: int(bin_search(cols_pos, code_b[7:], 7))}
	fmt.Println(s)

	// allIds := generateAllIds()
	// emptySeats := make([]int, 0)

	// for _, id := range allIds {
	// 	if ok := Find(seatIDS, id); !ok {
	// 		emptySeats = append(emptySeats, id)
	// 	}
	// }

	// sort.Ints(seatIDS)
	// fmt.Println(seatIDS)

	// for i, val := range seatIDS {
	// 	if i < len(emptySeats)-2 {
	// 		if seatIDS[i+1]-val == 2 {
	// 			fmt.Println(seatIDS[i+1], val)
	// 		}
	// 	}
	// }
}
