package main

import (
	"fmt"
)

const (
	width  = 800
	height = 800
	maxIter = 255
)

func main() {
	for y := 0; y < height; y++ {
		for x := 0; x < width; x++ {
			c := complex(-2.0+float64(x)/width*3.0, -1.5+float64(y)/height*3.0)
			z := complex(0, 0)
			iter := 0
			for ; iter < maxIter && real(z)*real(z)+imag(z)*imag(z) < 4; iter++ {
				z = z*z + c
			}
			fmt.Printf("%d ", iter)
		}
		fmt.Println()
	}
}