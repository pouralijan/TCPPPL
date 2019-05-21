#include <cstdlib>
#include <iostream>
#include "Vector.h"

int main()
{
	static_assert(3 <= sizeof(int), "int are too small");
	
	MyCode::Vector v(10);
	std::cout << v[1] << std::endl;
	v.size();
	
	return EXIT_SUCCESS;
}
