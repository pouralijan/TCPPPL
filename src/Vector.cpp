#include "Vector.h"
#include <stdexcept>

MyCode::Vector::Vector(int s)
{
	if(s<0)
		throw std::length_error{"size error ... :("};
	elem = new double[s];
	sz = s;
}

double& MyCode::Vector::operator[](int i)
{
	if(i<0 || size()<=i)
		throw std::out_of_range("Vector::operator[]."); // index between 0 and(%d.", size());
	return elem[i];
}

int MyCode::Vector::size()
{
	return sz;
}
