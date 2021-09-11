#ifndef STUDENT_H
#define STUDENT_H

#include <iostream>

class Student{
    public:
        long id{};
        double avg{};
        size_t units{50};
        Student (long _id, double _avg, size_t _units):id{_id},avg{_avg},units{_units}{}
        // bool operator<(const Student& student){ return avg<student.avg; }
};

#endif