#include "Vector.h"
#include <stdexcept>

MyCode::Vector::Vector(int s)
{
	if(s<0)
		throw std::length_error{"index error ... :("};
	elem = new double[s];
	sz = s;
}

double& MyCode::Vector::operator[](int i)
{
	return elem[i];
}

int MyCode::Vector::size()
{
	return sz;
}
