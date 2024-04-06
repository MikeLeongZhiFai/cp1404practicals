#include "Person.h"

Person::Person(std::string firstName, std::string lastName)
    : Person{std::move(firstName), std::move(lastName),
             firstName.substr(0, 1) + lastName.substr(0, 1)}
{
}

Person::Person(std::string firstName, std::string lastName, std::string initials)
    : m_firstName{std::move(firstName)}, m_lastName{std::move(lastName)}, m_initials{std::move(initials)}
{
}

const std::string &Person::getFirstName() const
{
    return m_firstName;
}
void Person::setFirstName(std::string firstName)
{
    m_firstName = std::move(firstName);
}

const std::string &Person::getLastName() const
{
    return m_lastName;
}

void Person::setLastName(std::string lastName)
{
    m_lastName = std::move(lastName);
}

const std::string &Person::getInitials() const
{
    return m_initials;
}

void Person::setInitials(std::string initials)
{
    m_initials = std::move(initials);
}

bool Person::operator==(const Person &other) const
{
    return (m_firstName == other.m_firstName) &&
           (m_lastName == other.m_lastName) &&
           (m_initials == other.m_initials);
}

bool Person::operator<(const Person &other) const
{
    if (m_lastName != other.m_lastName)
    {
        return m_lastName < other.m_lastName;
    }
    if (m_firstName != other.m_firstName)
    {
        return m_firstName < other.m_firstName;
    }
    return m_initials < other.m_initials;
}

bool Person::operator>(const Person &other) const
{
    return other < *this;
}

std::ostream &operator<<(ostream &os, const Person &person)
{
    os << "First name: " << person.getFirstName() << " ,Last name: " << person.getLastName() << " ,Initials: " << person.getInitials();
    return os;
}