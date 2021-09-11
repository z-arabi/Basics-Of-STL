#ifndef HW6_H
#define HW6_H

#include <iostream>
#include <algorithm>
#include <list>
#include <typeinfo>

template<class T1,class T2>
T1 convert(T2 _container);

template<class T>
void show(T _container);

template<class T>
T getRanks(T _container);

std::list<Student> getRanks(std::list<Student> _container);

template<class T>
T getInterns(T _container);

std::list<Student> getInterns(std::list<Student> _container);

template<class T>
auto findRank(T _container , size_t n);

#include "aphw6.hpp"

#endif