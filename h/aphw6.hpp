template<class T1,class T2>
T1 convert(T2 _container)
{
    T1 container(std::make_move_iterator(_container.begin()),std::make_move_iterator(_container.end()));
    return container;
}

template<class T>
void show(T  _container)
{
    typename T::iterator it; 
    for(it =  _container.begin(); it !=  _container.end(); ++it) 
        std::cout << it->id << "  "; 
    std::cout << '\n';
}

bool sort_avg(const Student& a, const Student& b){ return a.avg > b.avg; }

/* I get the compiler error so I can't have both of them in one function so I create two functions
template<class T>
T getRanks(T _container)
{
    if( decltype(_container) == std::list<Student> )
        _container.sort(sort_avg);
    else
        std::sort(_container.begin(), _container.end(), sort_avg);  
    return _container;
}
*/

template<class T>
T getRanks(T _container)
{
    std::sort(_container.begin(), _container.end(), sort_avg);  
    return _container;
}

std::list<Student> getRanks(std::list<Student> _list)
{
    _list.sort(sort_avg);
    return _list;
}

bool sort_units(const Student& a, const Student& b){ return a.units > b.units; }

/*
template<class T>
T getInterns(T _container)
{
    if( typeid(_container) == typeid(std::list<Student>) )
        _container.sort(sort_units);
    else
        std::sort(_container.begin(), _container.end(), sort_units);  
    return _container;
}
*/

template<class T>
T getInterns(T _container)
{
    std::sort(_container.begin(), _container.end(), sort_units);  
    return _container;
}

std::list<Student> getInterns(std::list<Student> _list)
{
    _list.sort(sort_units);  
    return _list;
}


template<class T>
auto findRank(T _container , size_t n)
{
    T container = _container;
    container = getRanks(container);
    return container[n-1];
}

