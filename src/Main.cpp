#include <cstdlib>
#include <iostream>
#include "Vector.h"

int main()
{
	static_assert(0 <= sizeof(int), "int are too small");
	
	MyCode::Vector v(10);
	for(int i=0; i<v.size(); i++)
		std::cout << v[i] << std::endl;
	v.size();
	
	return EXIT_SUCCESS;
}
