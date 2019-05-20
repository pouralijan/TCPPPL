#ifndef MY_VECTOR_H
#define MY_VECTOR_H

namespace MyCode{
	class Vector{
		public:
			Vector(int s);
			double& operator[](int i);
			int size();
		private:
			double* elem;
			int sz;

	};
}

#endif
