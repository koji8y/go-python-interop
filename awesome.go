package main

import "C"

import (
    "fmt"
    "math"
    "sort"
    "sync"
)

var count int
var mtx sync.Mutex

//export Add
func Add(a, b int) int { return a + b }

//export Cosine
func Cosine(x float64) float64 { return math.Cos(x) }

//export Sort
func Sort(vals []int) { sort.Ints(vals) }

//export Log
func Log(msg string) int {
  mtx.Lock()
  defer mtx.Unlock()
  fmt.Println(msg)
  count++
  return count
}

//export Log2
func Log2(msg *C.char) int {
  return Log(C.GoString(msg))
}

//export GetGreeting
func GetGreeting(name string) *C.char {
  return C.CString("Hi, " + name)
}

//export GetGreeting2
func GetGreeting2(name *C.char) *C.char {
  return GetGreeting(C.GoString(name))
}

func check() {
  s := []int{1, 5, 3, 2, 4}
  Sort(s)
  fmt.Println(s)
  for _, e := range s {
     fmt.Println(e)
  }
  //fmt.Println(GetGreeting("Foo"))
}

//func main() { check() }
func main() {}
