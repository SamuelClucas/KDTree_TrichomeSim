CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2

SRC = src/main.cpp
OBJ = $(SRC:.cpp=.o)
EXEC = kdtree_exec

all: $(EXEC)

$(EXEC): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(EXEC) $(OBJ)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)
