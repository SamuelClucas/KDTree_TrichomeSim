# KDTree Legacy Project 
This repository contains my first ever project written in C++, developed during a month-long internship in the Nédélec group at the [Sainsbury Laboratory, University of Cambridge](https://www.slcu.cam.ac.uk/) (2023).

## Overview 
The work took place during the summer between my 2nd and 3rd year of undergraduate study. I was beginning to develop a curiosity for computational thinking and how it might support biological research. This project was my first experience with systems-level coding, and I was particularly interested in pointer manipulation and memory layout.

## Project Goal 
Implement a custom k-d tree data structure with nearest neighbour search (NNS)

Apply it to spatial mesh point data generated from TrichomeSim, a cell geometry simulator for plant trichomes

The simulation used a dense 3D point cloud to represent cortical microtubule arrays. Brute-force search methods proved computationally expensive, prompting me to explore spatial partitioning techniques as a way of reducing complexity.

## Rationale 
My postdoc supervisor was developing TrichomeSim, a simulator for microtubule behavior on realistic plant cell surfaces. The simulator generated tens of thousands of 3D mesh points, which required efficient search methods to map microtubule positions and orientations.

This project explored whether a k-d tree implementation could improve query performance — or at least build intuition for how such structures behave.

## Outcomes 
Implemented from scratch a recursive k-d tree in C++ with:
- Pointer-based node creation 
- Median splitting and hyperplane partitioning 
- Simple nearest-neighbour query 

- Presented a [poster](./academic_poster.pdf) on the work at the Gatsby Plant Science Network Conference, Oxford (Sept 2023) 

## Funding 
This internship was funded by The Gatsby Charitable Foundation under the Sainsbury Undergraduate Studentship Scheme.

## About 
A hand-coded, pointer-driven spatial search tool built as my first exploration of algorithmic thinking in C++. Not optimised, but deeply formative.

