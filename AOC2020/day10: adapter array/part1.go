package main

import (
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, _ := ioutil.ReadFile("input.txt")
	arr_str := strings.Split(string(file), "\n")
	arr_int := make([]int, len(arr_str))
	for i, v := range arr_str {
		arr_int[i], _ = strconv.Atoi(v)
	}
	arr_int = append(arr_int, 0)
	sort.Ints(arr_int[:])
	arr_int = append(arr_int, arr_int[len(arr_int)-1]+3)
	dif1, dif3 := 0, 0
	for i := 1; i < len(arr_int); i++ {
		if arr_int[i]-arr_int[i-1] == 1 {
			dif1++
		} else if arr_int[i]-arr_int[i-1] == 3 {
			dif3++
		}
	}
	_ = ioutil.WriteFile("part1.txt", []byte(strconv.Itoa(dif1*dif3)), 0644)
}
